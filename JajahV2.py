# BattlePass
import PyQt5
import numpy as np
import cv2
import os
from sklearn.cluster import KMeans
import webcolors
import time
import datetime
from time import perf_counter

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, \
    QFileDialog, QAction, QMessageBox, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression
from tensorflow import Graph, Session


from PIL import Image
import glob
import base64
import requests as reqs
from io import BytesIO

# nclass = 4
model = None
# nclass_logos = 10
model_logo = None

fileName = None
position = None
Hide = 2





def centroid_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)
    hist = hist.astype("float")
    hist /= hist.sum()
    return hist


def plot_colors(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0
    color = None
    color_detec = None
    c1 = 0
    c2 = 0
    c3 = 0
    # print("Max : {:.3f}".format(max(hist)))
    for (percent, color) in zip(hist, centroids):  # True
        # print("color is : ",color)
        # print("percent ", percent, "total color ", len(color), "color[0]",color[0], "color[1]", color[1], "color[2]", color[2])
        if percent > 0.4:
            c1 = int(color[0])
            c2 = int(color[1])
            c3 = int(color[2])
            # print("Color[1]:{:d} | Color[2]:{:d} | Color[3]:{:d}".format(c1,c2,c3)) #disable
            return [bar, c1, c2, c3]

        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
        startX = endX


def load_logo():
    graph1 = Graph()
    with graph1.as_default():
        session1 = Session()
        with session1.as_default():
            nclass_logos = 10
            global model_logos
            networks = input_data(shape=[None, 100, 100, 1], name='input')
            networks = conv_2d(networks, 32, 3, activation='relu', regularizer="L2")
            networks = max_pool_2d(networks, 2)

            networks = local_response_normalization(networks)
            networks = conv_2d(networks, 64, 3, activation='relu', regularizer="L2")
            networks = max_pool_2d(networks, 2)

            networks = local_response_normalization(networks)
            networks = conv_2d(networks, 128, 3, activation='relu', regularizer="L2")
            networks = max_pool_2d(networks, 2)

            networks = local_response_normalization(networks)
            networks = conv_2d(networks, 256, 3, activation='relu', regularizer="L2")
            networks = max_pool_2d(networks, 2)

            networks = local_response_normalization(networks)
            networks = fully_connected(networks, 512, activation='tanh')
            networks = dropout(networks, 0.8)
            networks = fully_connected(networks, 4092, activation='tanh')
            networks = dropout(networks, 0.8)
            networks = fully_connected(networks, nclass_logos, activation='softmax')
            networks = regression(networks, optimizer='SGD', learning_rate=0.01,
                                  loss='categorical_crossentropy', name='target')

            model_logos = tflearn.DNN(networks, tensorboard_verbose=0)
            model_logos.load('Model_Logos_MetaV1/Meta_v1.cnn')
            print("LMLF:(Load model logos finished)")
            return model_logos


def load_model():
    graph2 = Graph()
    with graph2.as_default():
        session2 = Session()
        with session2.as_default():
            nclass = 4
            global model
            network = input_data(shape=[None, 100, 100, 1], name='input')
            network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 128, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = conv_2d(network, 256, 3, activation='relu', regularizer="L2")
            network = max_pool_2d(network, 2)

            network = local_response_normalization(network)
            network = fully_connected(network, 512, activation='tanh')
            network = dropout(network, 0.8)
            network = fully_connected(network, 4092, activation='tanh')
            network = dropout(network, 0.8)
            network = fully_connected(network, nclass, activation='softmax')
            network = regression(network, optimizer='SGD', learning_rate=0.01,
                                 loss='categorical_crossentropy', name='target')
            model = tflearn.DNN(network, tensorboard_verbose=0)
            model.load('Model_Type_MetaV1/Meta_Type_v1.cnn')
            print("LMF:(Load model finished)")
            print(graph2)
            return model


def convert_color(color_code):
    # Check color from web color : http://wow.in.th/PptJ
    color = color_code
    color_name = ''
    red_color = ['INDIANRED', 'LIGHTCORAL', 'SALMON', 'DARKSALMON', 'LIGHTSALMON', 'CRIMSON', 'RED', 'FIREBRICK',
                 'DARKRED']
    pink_color = ['PINK', 'LIGHTPINK', 'HOTPINK', 'DEEPPINK', 'MEDIUMVIOLETRED', 'PALEVIOLETRED']
    orenge_color = ['LIGHTSALMON', 'CORAL', 'TOMATO', 'ORANGERED', 'DARKORANGE', 'ORANGE']
    yellow_color = ['GOLD', 'YELLOW', 'LIGHTYELLOW', 'LEMONCHIFFON', 'LIGHTGOLDENRODYELLOW', 'PAPAYAWHIP', 'MOCCASIN',
                    'PEACHPUFF', 'PALEGOLDENROD', 'KHAKI', 'DARKKHAKI']
    purple_color = ['THISTLE', 'PLUM', 'VIOLET', 'ORCHID', 'FUCHSIA', 'MAGENTA', 'MEDIUMORCHID', 'MEDIUMPURPLE',
                    'REBECCAPURPLE', 'BLUEVIOLET', 'DARKVIOLET', 'DARKORCHID', 'DARKMAGENTA', 'PURPLE', 'INDIGO',
                    'SLATEBLUE', 'DARKSLATEBLUE', 'MEDIUMSLATEBLUE']
    green_color = ['GREENYELLOW', 'CHARTREUSE', 'LAWNGREEN', 'LIME', 'LIMEGREEN', 'PALEGREEN', 'LIGHTGREEN',
                   'MEDIUMSPRINGGREEN', 'SPRINGGREEN', 'MEDIUMSEAGREEN', 'SEAGREEN', 'FORESTGREEN', 'GREEN',
                   'DARKGREEN', 'YELLOWGREEN', 'OLIVEDRAB', 'OLIVE', 'DARKOLIVEGREEN', 'MEDIUMAQUAMARINE',
                   'DARKSEAGREEN', 'LIGHTSEAGREEN', 'DARKCYAN', 'TEAL']
    blue_color = ['AQUA', 'CYAN', 'LIGHTCYAN', 'PALETURQUOISE', 'AQUAMARINE', 'TURQUOISE', 'MEDIUMTURQUOISE',
                  'DARKTURQUOISE', 'CADETBLUE', 'STEELBLUE', 'LIGHTSTEELBLUE', 'POWDERBLUE', 'LIGHTBLUE', 'SKYBLUE',
                  'LIGHTSKYBLUE', 'DEEPSKYBLUE', 'DODGERBLUE', 'CORNFLOWERBLUE', 'MEDIUMSLATEBLUE', 'ROYALBLUE', 'BLUE',
                  'MEDIUMBLUE', 'DARKBLUE', 'NAVY', 'MIDNIGHTBLUE']
    brown_color = ['CORNSILK', 'BLANCHEDALMOND', 'BISQUE', 'NAVAJOWHITE', 'WHEAT', 'BURLYWOOD', 'TAN', 'ROSYBROWN',
                   'SANDYBROWN', 'GOLDENROD', 'DARKGOLDENROD', 'PERU', 'CHOCOLATE', 'SADDLEBROWN', 'SIENNA', 'BROWN',
                   'MAROON']
    white_color = ['LAVENDER', 'WHITE', 'SNOW', 'HONEYDEW', 'MINTCREAM', 'AZURE', 'ALICEBLUE', 'GHOSTWHITE',
                   'WHITESMOKE', 'SEASHELL', 'BEIGE', 'OLDLACE', 'FLORALWHITE', 'IVORY', 'ANTIQUEWHITE', 'LINEN',
                   'LAVENDERBLUSH', 'MISTYROSE']
    gray_color = ['GAINSBORO', 'LIGHTGRAY', 'SILVER', 'DARKGRAY', 'GRAY', 'DIMGRAY', 'LIGHTSLATEGRAY', 'SLATEGRAY',
                  'DARKSLATEGRAY', 'BLACK']

    if color.upper() in red_color:
        print('RED')
        color_name = 'RED'
        return color_name
    elif color.upper() in pink_color:
        print('PINK')
        color_name = 'PINK'
        return color_name
    elif color.upper() in orenge_color:
        print('ORANGE')
        color_name = 'ORANGE'
        return color_name
    elif color.upper() in yellow_color:
        print('YELLOW')
        color_name = 'YELLOW'
        return color_name
    elif color.upper() in purple_color:
        print('PURPLE')
        color_name = 'PURPLE'
        return color_name
    elif color.upper() in green_color:
        print('GREEN')
        color_name = 'GREEN'
        return color_name
    elif color.upper() in blue_color:
        print('BLUE')
        color_name = 'BLUE'
        return color_name
    elif color.upper() in brown_color:
        print('BROWN')
        color_name = 'BROWN'
        return color_name
    elif color.upper() in white_color:
        print('WHITE')
        color_name = 'WHITE'
        return color_name
    elif color.upper() in gray_color:
        print('GRAY')
        color_name = 'GRAY'
        return color_name
    else:
        print('ai cant find color ...')
        color_name = 'Unknown'
        return color_name


# todo K-means Webcolors
def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def processing(path_location):
    global model
    type_car = ''
    path_image = 'Save\\' + path_location
    a = cv2.imread(path_image)
    print("source : {}".format(path_image))
    try:
        height = 100
        width = 100
        dim = (width, height)
        b = cv2.resize(a, dim, interpolation=cv2.INTER_AREA)
        img_tmp = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        tmp = img_tmp.flatten()
        testX = tmp.reshape([-1, 100, 100, 1])
        # print('This is testX : ', testX)
        result = model.predict(testX)
        print("This is Result 0 : ", result[0])
        x = np.array(result[0])
        idx = np.argmax(x)
        print(idx)
        if idx == 0:
            type_car = "Car_Type_1"
            print("Car_Type_1")
        elif idx == 1:
            type_car = "Car_Type_2"
            print("Car_Type_2")
        elif idx == 2:
            type_car = "Car_Type_3"
            print("Car_Type_3")
        elif idx == 3:
            type_car = "other_Car"
            print("other_Car")
        else:
            print("Missing Data...")
    except:
        print('Cant Prediction')
        # model = load_model()

    # # todo write file
    # f = open("data_type.txt", "a")
    # f.write("image : " + repr(path_image) + '\n')
    # f.write("Type : " + repr(type_car) + '\n')
    # f.write("-------------------------------------------\n")
    # f.close()


# noinspection PyArgumentList
class App(QWidget):
    global fileName
    global position

    def __init__(self):
        super().__init__()
        self.Hide = 0
        self.label_color = QLabel(self)
        self.label_Center = QLabel(self)
        self.label_name = QLabel(self)
        self.label = QLabel(self)
        self.buttonOk = QPushButton('Ok', self)
        self.textboxWidth = QLineEdit(self)
        self.labelWidth = QLabel('Width : ', self)
        self.labelLocationY = QLabel('Location : Y', self)
        self.textboxFrameX = QLineEdit(self)
        self.labelLocationX = QLabel('Location : X', self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Browse File', self)
        self.textboxFrameY = QLineEdit(self)
        self.title = ': Project 2'
        self.left = 0
        self.top = 0
        self.width = 530
        self.height = 520
        self.setWindowIcon(PyQt5.QtGui.QIcon('dai.png'))
        self.initUI()
        load_logo()
        load_model()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(100, 100, 1400, 900)
        self.center()
        ##################################################################################################
        # Button
        self.button.setToolTip('Button browse file video.')
        self.button.move(0, 0)
        self.button.clicked.connect(self.on_click)
        # Textbox
        self.textbox.move(80, 2)
        self.textbox.resize(280, 20)
        # Label location X
        self.labelLocationX.resize(100, 20)
        self.labelLocationX.move(370, 60)
        # Textbox Frame X
        self.textboxFrameX.setText('500')
        self.textboxFrameX.resize(70, 20)
        self.textboxFrameX.move(450, 60)
        # Label location Y
        self.labelLocationY.resize(100, 20)
        self.labelLocationY.move(370, 90)
        # Textbox Frame Y
        self.textboxFrameY.setText('470')
        self.textboxFrameY.resize(70, 20)
        self.textboxFrameY.move(450, 90)
        # Label width
        self.labelWidth.resize(100, 20)
        self.labelWidth.move(370, 120)
        # Textbox width
        self.textboxWidth.setText('375')
        self.textboxWidth.resize(70, 20)
        self.textboxWidth.move(450, 120)
        # Button ok get Value.
        self.buttonOk.move(370, 3)
        self.buttonOk.resize(150, 50)
        self.buttonOk.clicked.connect(self.test_Click)
        # Font
        newFont = PyQt5.QtGui.QFont("Times", 10, PyQt5.QtGui.QFont.Bold)
        # newFont = PyQt5.QtGui.QFont('Hammer Thin', 16, PyQt5.QtGui.QFont.Bold)

        # Label = Picture Car
        self.label.resize(350, 400)
        self.label.move(10, 25)
        # Label - namePicture.
        self.label_name.setFont(newFont)
        self.label_name.setText('No name of images.      ')
        self.label_name.move(10, 420)

        # Label - name_Color.
        self.label_color.setFont(newFont)
        self.label_color.setText('Color                          ')
        self.label_color.move(10, 440)

        # speed line
        self.speed_line = QLabel('Speed_Line', self)
        self.speed_line.resize(100, 20)
        self.speed_line.move(370, 150)
        self.speed_box = QLineEdit(self)
        self.speed_box.setText('230')
        self.speed_box.resize(70, 20)
        self.speed_box.move(450, 150)
        # Distance
        self.distance = QLabel('Distance', self)
        self.distance.resize(100, 20)
        self.distance.move(370, 180)

        self.distance_box = QLineEdit(self)
        self.distance_box.setText('6')
        self.distance_box.resize(70, 20)
        self.distance_box.move(450, 180)

        self.button_upload = QPushButton('Upload Images', self)
        self.button_upload.resize(150, 50)
        self.button_upload.move(370, 210)
        self.button_upload.clicked.connect(self.test_Click)

        #Label Type
        self.label_type = QLabel(self)
        self.label_type.setFont(newFont)
        self.label_type.setText('Prediction Type                          ')
        self.label_type.move(10, 460)  #+60

        # Label Type Logos
        self.label_logos = QLabel(self)
        self.label_logos.setFont(newFont)
        self.label_logos.setText('Prediction Logo                          ')
        self.label_logos.move(10, 480)  # +60

        # Label Type Speed
        self.label_speed = QLabel(self)
        self.label_speed.setFont(newFont)
        self.label_speed.setText('Prediction Speed                          ')
        self.label_speed.move(10, 500)  # +60


        # #todo CheckBox 23 july
        # self.checkBox = QCheckBox('Show Threadshow', self)
        # self.checkBox.stateChanged.connect(self.clickBox)
        # self.checkBox.move(10, 430)
        # self.checkBox.resize(320, 40)

        ##################################################################################################
        self.show()
        ##################################################################################################

    def clickBox(self, state):
        if state == PyQt5.QtCore.Qt.Checked:
            print('Checked :', (int(state)))
            self.Hide = 2
        else:
            print('Unchecked :', (int(state)))

    # todo Crop_Box 21 july 2019

    def test_Click(self):
        valueX = self.textboxFrameX.text()
        print('value FrameX ', valueX)
        valueY = self.textboxFrameY.text()
        print('value FrameY ', valueY)
        valueW = self.textboxWidth.text()
        print('value Width ', valueW)
        value_speed_line = self.speed_box.text()
        print('Speed Line ', value_speed_line)
        value_distance = self.distance_box.text()
        # showData = 'Frame X : ' + valueX + ' Frame Y : ' + valueY + ' Frame Width : ' + valueW + ' '
        showData = 'Frame X : {} Frame Y : {} Frame Width : {} Speed Line : {} Distance : {}'.format(valueX, valueY,
                                                                                                     valueW,
                                                                                                     value_speed_line,
                                                                                                     value_distance)
        QMessageBox.question(self, 'Message.get()', 'Set_Value ' + showData, QMessageBox.Ok, QMessageBox.Ok)
        saveValue = int(valueX), int(valueY), int(valueW), int(value_speed_line), float(value_distance)
        self.get_position(saveValue)

    # todo get_position X,Y and Width in video. 21 july 2019
    def get_position(self, position):
        self.position = position
        print('set position', self.position)

    # todo 12 july. K-means checkColor.  !Slow
    def check_Color(self, pic_color):
        logo_name = ''  # Brand_Car
        pic_car_color = 'color_car\\' + pic_color
        # print('pic_car_color : ', pic_car_color)
        Kcolors = cv2.imread(pic_car_color)
        Kcolors = cv2.cvtColor(Kcolors, cv2.COLOR_BGR2RGB)
        Kcolors = Kcolors.reshape((Kcolors.shape[0] * Kcolors.shape[1], 3))
        clt = KMeans(n_clusters=2)
        clt.fit(Kcolors)
        hist = centroid_histogram(clt)
        print("Histogram : ", hist)
        bar = plot_colors(hist, clt.cluster_centers_)
        requested_colour = (bar[1], bar[2], bar[3])
        actual_name, closest_name = get_colour_name(requested_colour)
        # self.label_color.setText('Color  : ' + closest_name)
        # print("Actual colour name:", actual_name, " group color : ", closest_name)
        convert_name_color = convert_color(closest_name)
        self.label_color.setText('Color  : ' + convert_name_color)
        # model_logo
        im = cv2.imread(pic_car_color)
        width = 100
        height = 100
        dim = (width, height)
        b = cv2.resize(im, dim, interpolation=cv2.INTER_AREA)
        img_tmp = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        tmp = img_tmp.flatten()
        testX = tmp.reshape([-1, 100, 100, 1])
        result = model_logos.predict(testX)
        # result = model_logos.predict(im)
        # print("This is Result 0 : ", result[0])
        x = np.array(result[0])
        x = ['{:01.4f}'.format(n) for n in x]
        x = [float(i) for i in x]
        idx = np.argmax(x)
        print('result[0] : ', result[0])
        print('model_logo: ', idx)
        if idx == 0:
            logo_name = 'TOYOTA'
        elif idx == 1:
            logo_name = 'HONDA'
        elif idx == 2:
            logo_name = 'MISZUBISHI'
        elif idx == 3:
            logo_name = 'NISSAN'
        elif idx == 4:
            logo_name = 'MAZDA'
        elif idx == 5:
            logo_name = 'CHEVRORET'
        elif idx == 6:
            logo_name = 'FORD'
        elif idx == 7:
            logo_name = 'SUZUKI'
        elif idx == 8:
            logo_name = 'ISUZU'
        elif idx == 9:
            logo_name = 'OTHER'

        # todo write file
        f = open("data_logo.txt", "a")
        f.write("image : " + repr(pic_car_color) + '\n')
        f.write("logo : " + repr(logo_name) + '\n')
        f.write("-------------------------------------------\n")
        f.close()
        # # Call back API
        # im = cv2.imread(pic_car_color)
        # im = cv2.imencode('.jpg', im)[1]
        # imgbase = str(base64.b64encode(im))
        # x = imgbase.split("'")
        # try:
        #     str_data = x[1]
        #     data = {'logo': str_data}
        #     response = reqs.post('http://127.0.0.1:5000/logo', json=data)
        #     print('call back : ', response.text)
        # except:
        #     print('Exiting API.')
        # todo write file
        f = open("data.txt", "a")
        # f.write("Color[R]: " + repr(bar[1]) + " Color[G]: " + repr(bar[2]) + " Color[B]: " + repr(bar[3]) + '\n')
        f.write("colour name : " + repr(convert_name_color) + '\n')
        f.write("colour name : " + repr(pic_color) + '\n')
        f.write("-------------------------------------------\n")
        f.close()

    # todo Crop insert image to label. 7 july
    def image_Crop(self, locations):
        pic_car = locations
        # print('image name : ', pic_car)
        self.label_name.setText('Name : ' + pic_car)  # location of car image
        pic_bit = 'Save\\' + pic_car
        pixmap = QPixmap(pic_bit)
        pixmap = pixmap.scaled(350, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)

    # @pyqtSlot()
    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File : ", "",
                                                  "All Files (*);;Video Files (*.MOV)", options=options)
        if fileName:
            print(fileName)
        self.textbox.setText(fileName)
        QMessageBox.question(self, 'Message.get()', 'Run Video : ' + fileName, QMessageBox.Ok, QMessageBox.Ok)
        self.test_Click()  # call Function get Position.
        self.play_Video(fileName)
        return fileName

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def play_Video(self, name):
        global flag
        # self.path = name
        filePathName = name
        # filePathName = (self.path)  # path_video
        cap = cv2.VideoCapture(filePathName)
        frames_count, fps, width, height = cap.get(cv2.CAP_PROP_FRAME_COUNT), cap.get(cv2.CAP_PROP_FPS), cap.get(
            cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # cap2 = cv2.VideoCapture(filePathName)

        width = int(width)
        height = int(height)
        print(cap, frames_count, fps, width, height)

        sub = cv2.createBackgroundSubtractorMOG2()
        ret, frame = cap.read()
        ratio = 1
        image = cv2.resize(frame, (0, 0), None, ratio, ratio)
        # original = cv2.resize(frame, (0, 0), None, ratio, ratio)
        width2, height2, channels = image.shape

        path_car = 'Save'
        path_color = 'color_car'
        data = 'car_'
        last = '.png'
        test = ""  # Change
        counter = 1  # Fix Coun.

        start_time = time.time()
        start = datetime.datetime.now()
        timer = []
        count_frame = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                frame = cv2.VideoCapture(filePathName)
                continue
            if ret:
                t1_start = 0
                t1_stop = 0

                image = cv2.resize(frame, (1280, 720), None, ratio, ratio)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                fgmask = sub.apply(gray)
                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
                opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
                dilation2 = cv2.dilate(opening, kernel, iterations=2)
                retvalbin, bins = cv2.threshold(dilation2, 160, 255, cv2.THRESH_BINARY)  # Disable
                # cv2.imshow("Bins", bins)  # bins is threshold. Disable

                contours, hierarchy = cv2.findContours(bins, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Fixed openCV 4.0
                minarea = 36000  # minarea = 500
                maxarea = 350000  # maxarea = 30000
                cxx = np.zeros(len(contours))
                cyy = np.zeros(len(contours))

                # t1_start = perf_counter()
                for i in range(len(contours)):

                    if hierarchy[0, i, 3] == -1:
                        area = cv2.contourArea(contours[i])
                        if minarea < area < maxarea:
                            cnt = contours[i]
                            M = cv2.moments(cnt)
                            cx = int(M['m10'] / M['m00'])
                            cy = int(M['m01'] / M['m00'])
                            # Speed_check ############################################
                            # self.position[0] == X
                            # self.position[1] == Y
                            # self.position[2] == W
                            # self.position[3] == speed_line Y angle
                            # self.position[4] == distance
                            sed_time = 0

                            if cx >= self.position[0] and cx <= self.position[0] + self.position[2] and cy >= \
                                    self.position[3]:
                                # timer.append(count_frame)
                                t1_start = perf_counter()
                            # Speed_check ############################################

                            if 500 <= cx <= 950:  # cx 1200 if cx >= 500 and cx <= 950:
                                if cy < 400:  # 600
                                    flag = 0
                                    # if (cx > 540) and (cx < 540 + 310):
                                if self.position[0] <= cx <= self.position[0] + 375:  # if (cx >= 500) and (cx <= 875):
                                    x, y, w, h = cv2.boundingRect(cnt)
                                    if self.position[1] < cy < self.position[1] + 30:  # Line Capture;
                                        vehicle_car = image[y - 30: y + h + 30, x - 30: x + w]
                                        vehicle_color = image[y + 150: y + h - 60, x + 50: x + w - 60]
                                        # vehicle_color = image[y + 120: y + h - 10, x + 50: x + w - 60] #original
                                        # cv2.imshow('Detect', vehicle)  # Config  #disable show in gui.
                                        save_file = ('%s%d%s' % (data, counter, last))
                                        # self.check_Color(save_file)
                                        processing(save_file)
                                        if flag == 0:
                                            cv2.imwrite(os.path.join(path_car, save_file),
                                                        vehicle_car)
                                            cv2.imwrite(os.path.join(path_color, save_file), vehicle_color)
                                            self.image_Crop(save_file)  # send location images. ส่งที่อยู่ไฟล์ภาพ
                                            # self.processing(save_file)
                                            self.check_Color(save_file)
                                            ######################### Time
                                            t1_stop = perf_counter()
                                            time_lock = t1_stop - t1_start
                                            print("time lock", time_lock)
                                            # print('Speed : ', self.position[4] / (time_lock-(0.037*(timer[-1] - timer[0]-2))))
                                            print('Speed : ',
                                                  self.position[4] / (time_lock) + 35)
                                            # print('Stop Frame', count_frame)
                                            # print('FPS-ST: ', timer[0], 'FPS-last: ', timer[-1], ' Total Frame : ', timer[-1] - timer[0])
                                            # timer.clear()
                                            ######################### Time
                                            flag = 1
                                            counter += 1
                                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),
                                                cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 0, 255), 1)
                                    cv2.drawMarker(image, (cx, cy), (0, 255, 255), cv2.MARKER_CROSS, markerSize=8,
                                                   thickness=3,
                                                   line_type=cv2.LINE_8)

            # todo test draw position. 22 july Finished !
            # draw = self.get_position()
            # print('Draw position ',draw)
            # print('posision is ', self.position)
            # self.position[0] == X
            # self.position[1] == Y
            # self.position[2] == W
            # self.position[3] == speed_line Y angle
            image = cv2.rectangle(image, (self.position[0], self.position[1] - 260),
                                  (self.position[2] + self.position[0], self.position[1] + 220), (20, 200, 20),
                                  3)  # Black clor  # xy มุมบนซ้าย xyล่างขวา
            image = cv2.line(image, (self.position[0], self.position[1]),
                             (self.position[0] + self.position[2], self.position[1]), (0, 0, 255),
                             2)  # Line white color

            cv2.line(image, (self.position[0], self.position[3]),
                     (self.position[0] + self.position[2], self.position[3]), (30, 30, 220), 3)

            # image = cv2.rectangle(image, (540, 320), (540 + 310, 320 + 370), (0, 255, 0),2)
            # cv2.rectangle(image, (840, 360), (840 + 420, 360 + 460), (0, 255, 0), 2)
            # image = cv2.rectangle(image, (500, 212), (875, 690), (255, 0, 0), 2)  # xy มุมบนซ้าย xyล่างขวา
            # image = cv2.line(image, (540, 542), (850, 542), (0, 0, 255), 2)  # Line
            # image = cv2.line(image, (500, 470), (875, 470), (0, 140, 255), 2)  # Line  Orenge       BGR RGB
            # todo line positions x
            # linePosition = cv2.line(image, (200, 0), (200, 720), 1)
            # linePosition = cv2.putText(image, '200', (200, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            linePosition = cv2.line(image, (400, 0), (400, 720), 1)
            linePosition = cv2.putText(image, '400', (400, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            linePosition = cv2.line(image, (600, 0), (600, 720), 1)
            linePosition = cv2.putText(image, '600', (600, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (800, 0), (800, 720), 1)
            linePosition = cv2.putText(image, '800', (800, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            # linePosition = cv2.line(image, (1000, 0), (1000, 720), 1)
            # linePosition = cv2.putText(image, '1000', (1000, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            #
            # linePosition = cv2.line(image, (1200, 0), (1200, 720), 1)
            # linePosition = cv2.putText(image, '1200', (1200, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            # todo line positions y
            linePosition = cv2.line(image, (0, 200), (1280, 200), 1)
            linePosition = cv2.putText(image, '200', (2, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            linePosition = cv2.line(image, (0, 400), (1280, 400), 1)
            linePosition = cv2.putText(image, '400', (2, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            linePosition = cv2.line(image, (0, 600), (1280, 600), 1)
            linePosition = cv2.putText(image, '600', (2, 600), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            # cv2.line(image, (500, 230), (500 + 375, 230), (30, 30, 220), 3)

            image = cv2.imshow("Pro2", image)

            # print('Time : ', start, 'Start Time', start_time)
            # elapsed_time = time.time() - start_time
            # end = datetime.datetime.now()
            # elapsed = end - start
            # print('ori:', elapsed_time, 'Time:',
            #       time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
            #       ' microseconds: ', elapsed.microseconds)
            # print("TIME : ")

            count_frame += 1
            # print('fps', count_frame, frames_count)
            if cv2.waitKey(1) & 0xFF == ord('q') or count_frame >= frames_count:
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
