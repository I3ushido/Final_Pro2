# BattlePass
import PyQt5
import numpy as np
import cv2
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utilsV2
import webcolors
import time

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

nclass = 4
model = None
# nclass_logo = 10
# model_logo = None
fileName = None
position = None
Hide = 2
start_time = time.time()


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
        color_name = ''
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
    path_image = 'Save\\' + path_location
    a = cv2.imread(path_image)
    print("source : {}".format(path_image))
    # cv2.imshow('read', a)
    height = 80
    width = 50
    dim = (width, height)
    b = cv2.resize(a, dim, interpolation=cv2.INTER_AREA)
    # cv2.imshow('read', b)
    # print(b)
    tmp = b.flatten()
    testX = tmp.reshape([-1, 80, 50, 1])
    # print('This is testX : ', testX)
    result = model.predict(testX)
    print("This is Result 0 : ", result[0])
    x = np.array(result[0])
    # print('X', x)
    idx = np.argmax(x)
    print(idx)
    if idx == 0:
        print("Car_Type_1")
    elif idx == 1:
        print("Car_Type_2")
    elif idx == 2:
        print("Car_Type_3")
    elif idx == 3:
        print("other_Car")
    else:
        print("Missing Data...")


def load_model_logos():
    nclass_logos = 10
    model_logos = None
    networks = input_data(shape=[None, 128, 128, 3], name='input')
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
    model_logos.load('logo_128128_150/modeltest_logo.cnn')
    print("LMLF:(Load model logos finished)")


def load_model():
    global nclass
    global model
    network = input_data(shape=[None, 80, 50, 1], name='input')
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
    model.load('model5/modeltestDataV5.cnn')
    print("LMF:(Load model finished)")
    return model


def Speed_Cal(timer):
    try:
        Speed = (9.144 * 3600) / (timer * 1000)
        return Speed
    except ZeroDivisionError:
        print(5)


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
        self.labelLocationY = QLabel('Location : Y ', self)
        self.textboxFrameX = QLineEdit(self)
        self.labelLocationX = QLabel('Location : X ', self)
        self.textbox = QLineEdit(self)
        self.button = QPushButton('Browse File', self)
        self.textboxFrameY = QLineEdit(self)
        self.title = 'Controller_v.1.3.21'
        self.left = 0
        self.top = 0
        self.width = 900
        self.height = 520
        self.initUI()
        load_model()
        # load_model_logo()
        # load_model_logos()

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
        self.labelLocationX.resize(150, 20)
        self.labelLocationX.move(370, 2)
        # Textbox Frame X
        self.textboxFrameX.setText('500')
        self.textboxFrameX.resize(70, 20)
        self.textboxFrameX.move(430, 2)
        # Label location Y
        self.labelLocationY.resize(100, 20)
        self.labelLocationY.move(510, 2)
        # Textbox Frame Y
        self.textboxFrameY.setText('470')
        self.textboxFrameY.resize(70, 20)
        self.textboxFrameY.move(570, 2)
        # Label width
        self.labelWidth.resize(100, 20)
        self.labelWidth.move(650, 2)
        # Textbox width
        self.textboxWidth.setText('375')
        self.textboxWidth.resize(70, 20)
        self.textboxWidth.move(690, 2)
        # Button ok get Value.
        self.buttonOk.move(770, 0)
        self.buttonOk.clicked.connect(self.test_Click)
        # Font
        newFont = PyQt5.QtGui.QFont("Times", 14, PyQt5.QtGui.QFont.Bold)
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
        print('Clicked')
        valueX = self.textboxFrameX.text()
        print('value FrameX ', valueX)
        valueY = self.textboxFrameY.text()
        print('value FrameY ', valueY)
        valueW = self.textboxWidth.text()
        print('value Width ', valueW)
        # showData = 'Frame X : ' + valueX + ' Frame Y : ' + valueY + ' Frame Width : ' + valueW + ' '
        showData = 'Frame X : {} Frame Y : {} Frame Width : {} '.format(valueX, valueY, valueW)
        QMessageBox.question(self, 'Message.get()', 'Set_Value ' + showData, QMessageBox.Ok, QMessageBox.Ok)
        saveValue = int(valueX), int(valueY), int(valueW)
        self.get_position(saveValue)

    # todo get_position X,Y and Width in video. 21 july 2019
    def get_position(self, position):
        self.position = position
        print('set position', self.position)

    # todo 12 july. K-means checkColor.  !Slow
    def check_Color(self, pic_Color):
        self.pic_car_color = 'color_car\\' + pic_Color
        Kcolors = cv2.imread(self.pic_car_color)
        Kcolors = cv2.cvtColor(Kcolors, cv2.COLOR_BGR2RGB)
        Kcolors = Kcolors.reshape((Kcolors.shape[0] * Kcolors.shape[1], 3))
        clt = KMeans(n_clusters=2)
        clt.fit(Kcolors)
        hist = utilsV2.centroid_histogram(clt)
        print("Histogram : ", hist)
        bar = utilsV2.plot_colors(hist, clt.cluster_centers_)
        requested_colour = (bar[1], bar[2], bar[3])
        actual_name, closest_name = get_colour_name(requested_colour)
        self.label_color.setText('Color  : ' + closest_name)
        # print("Actual colour name:", actual_name, " group color : ", closest_name)
        convert_name_color = convert_color(closest_name)

        # todo write file
        f = open("data.txt", "a")
        # f.write("Color[R]: " + repr(bar[1]) + " Color[G]: " + repr(bar[2]) + " Color[B]: " + repr(bar[3]) + '\n')
        f.write("colour name : " + repr(convert_name_color) + '\n')
        f.write("colour name : " + repr(pic_Color) + '\n')
        f.write("-------------------------------------------\n")
        f.close()

    # todo Crop insert image to label. 7 july
    def image_Crop(self, locations):
        self.pic_car = locations
        print('image name : ', self.pic_car)
        self.label_name.setText('Name : ' + self.pic_car)  # location of car image
        pic_bit = 'Save\\' + self.pic_car
        self.pixmap = QPixmap(pic_bit)
        self.pixmap = self.pixmap.scaled(350, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)

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
        num = 1

        path_car = 'Save'
        path_color = 'color_car'
        data = 'car_'
        last = '.jpg'
        test = ""  # Change
        counter = 1  # Fix Coun.

        while True:
            ret, frame = cap.read()
            if not ret:
                frame = cv2.VideoCapture(filePathName)
                continue
            if ret:
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

                for i in range(len(contours)):
                    if hierarchy[0, i, 3] == -1:
                        area = cv2.contourArea(contours[i])
                        if minarea < area < maxarea:
                            cnt = contours[i]
                            M = cv2.moments(cnt)
                            cx = int(M['m10'] / M['m00'])
                            cy = int(M['m01'] / M['m00'])
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
                                        self.check_Color(save_file)
                                        processing(save_file)
                                        if flag == 0:
                                            cv2.imwrite(os.path.join(path_car, save_file),
                                                        vehicle_car)  # Save to Folder : Save;
                                            cv2.imwrite(os.path.join(path_color, save_file), vehicle_color)
                                            # self.image_Crop(vehicle)
                                            self.image_Crop(save_file)  # send location images. ส่งที่อยู่ไฟล์ภาพ
                                            # self.processing(save_file)
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
            image = cv2.rectangle(image, (self.position[0], self.position[1] - 260),
                                  (self.position[2] + self.position[0], self.position[1] + 220), (20, 200, 20),
                                  3)  # Black clor  # xy มุมบนซ้าย xyล่างขวา
            image = cv2.line(image, (self.position[0], self.position[1]),
                             (self.position[0] + self.position[2], self.position[1]), (0, 0, 255),
                             2)  # Line white color

            # image = cv2.rectangle(image, (540, 320), (540 + 310, 320 + 370), (0, 255, 0),2)
            # cv2.rectangle(image, (840, 360), (840 + 420, 360 + 460), (0, 255, 0), 2)
            # image = cv2.rectangle(image, (500, 212), (875, 690), (255, 0, 0), 2)  # xy มุมบนซ้าย xyล่างขวา
            # image = cv2.line(image, (540, 542), (850, 542), (0, 0, 255), 2)  # Line
            # image = cv2.line(image, (500, 470), (875, 470), (0, 140, 255), 2)  # Line  Orenge       BGR RGB
            # todo line positions x
            linePosition = cv2.line(image, (200, 0), (200, 720), 1)
            linePosition = cv2.putText(image, '200', (200, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (400, 0), (400, 720), 1)
            linePosition = cv2.putText(image, '400', (400, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (600, 0), (600, 720), 1)
            linePosition = cv2.putText(image, '600', (600, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (800, 0), (800, 720), 1)
            linePosition = cv2.putText(image, '800', (800, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (1000, 0), (1000, 720), 1)
            linePosition = cv2.putText(image, '1000', (1000, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (1200, 0), (1200, 720), 1)
            linePosition = cv2.putText(image, '1200', (1200, 15), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            # todo line positions y
            linePosition = cv2.line(image, (0, 200), (1280, 200), 1)
            linePosition = cv2.putText(image, '200', (2, 200), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (0, 400), (1280, 400), 1)
            linePosition = cv2.putText(image, '400', (2, 400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)
            linePosition = cv2.line(image, (0, 600), (1280, 600), 1)
            linePosition = cv2.putText(image, '600', (2, 600), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, 2)

            image = cv2.imshow("Detection : Pro2", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
