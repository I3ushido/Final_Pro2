#BattlePass
#Ti9
import logging
from io import StringIO

import PyQt5
import numpy as np
import cv2
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, QFileDialog , QAction, QMessageBox, QMainWindow, QCheckBox,QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize

fileName = None
position = None
Hide = 2


class App(QWidget):
    global fileName
    global position
    global Hide

    def __init__(self):
        super().__init__()
        self.title = 'Controller_v.1.3.21'
        self.left = 0
        self.top = 0
        self.width = 900
        self.height = 620
        self.initUI()
       

    def initUI(self):
        

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(100, 100, 1400, 900)
        self.center()
        ##################################################################################################
##        self.gridLayout = PyQt5.QtWidgets.QGridLayout(QWidget)   #Still don't work
##        self.gridLayout.setObjectName("gridLayout")
        ##################################################################################################
        #Button
        self.button = QPushButton('Browse File', self)
        self.button.setToolTip('Button browse file video.')
        self.button.move(0, 0)
        self.button.clicked.connect(self.on_click)
        #Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(80, 2)
        self.textbox.resize(280, 20)
        # Label location X
        self.labelLocationX = QLabel('Location : X ',self)
        self.labelLocationX.resize(150, 20)
        self.labelLocationX.move(370, 2)
        # Textbox Frame X
        self.textboxFrameX = QLineEdit(self)
        self.textboxFrameX.setText('500')
        self.textboxFrameX.resize(70, 20)
        self.textboxFrameX.move(430, 2)
        # Label location Y
        self.labelLocationY = QLabel('Location : Y ',self)
        self.labelLocationY.resize(100, 20)
        self.labelLocationY.move(510, 2)
        # Textbox Frame Y
        self.textboxFrameY = QLineEdit(self)
        self.textboxFrameY.setText('470')
        self.textboxFrameY.resize(70, 20)
        self.textboxFrameY.move(570, 2)
        # Label width
        self.labelWidth  = QLabel('Width : ', self)
        self.labelWidth.resize(100, 20)
        self.labelWidth.move(650, 2)
        # Textbox width
        self.textboxWidth = QLineEdit(self)
        self.textboxWidth.setText('375')
        self.textboxWidth.resize(70, 20)
        self.textboxWidth.move(690, 2)
        # Button ok get Value.
        self.buttonOk = QPushButton('Ok', self)
        self.buttonOk.move(770, 0)
        self.buttonOk.clicked.connect(self.test_Click)
        #Font
        newFont = PyQt5.QtGui.QFont("Times", 14, PyQt5.QtGui.QFont.Bold)
        #newFont = PyQt5.QtGui.QFont('Hammer Thin', 16, PyQt5.QtGui.QFont.Bold)

        #Label = Picture Car
        self.label = QLabel(self)
        self.label.resize(350, 400)
        self.label.move(10, 25)
        #Label - namePicture.
        self.label_name = QLabel(self)
        self.label_name.setFont(newFont)
        self.label_name.setText('No name of images.      ')
        self.label_name.move(10,420)
        #Label 2 Center
        self.label_Center = QLabel(self)
        self.label_Center.resize(400, 400)
        self.label_Center.move(430, 25)
        pixmap = QPixmap('info.jpg')
        # pixmap = QPixmap('car.jpg')
        # print(self.label_Center.width(), self.label_Center.height())
        pixmap = pixmap.scaled(self.label_Center.width(), self.label_Center.height(), Qt.KeepAspectRatio)
        # pixmap = pixmap.scaled(640,480,Qt.KeepAspectRatio)
        self.label_Center.setPixmap(pixmap)


        #todo CheckBox 23 july
        self.checkBox = QCheckBox('Show Threadshow', self)
        self.checkBox.stateChanged.connect(self.clickBox)
        self.checkBox.move(10, 430)
        self.checkBox.resize(320, 40)
        
        ##################################################################################################
        # Textbox Test Alert
        # logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
        # log_stream = StringIO()
        # logging.basicConfig(stream=log_stream, level=logging.INFO)
        #
        # logging.info('Start')
        # loggingInfo = log_stream.getvalue() + " "
        # loggingInfo.__str__()
        #
        # print(loggingInfo)

        # self.textboxAlert = QPlainTextEdit(self)
        # self.textboxAlert.insertPlainText(" "+loggingInfofa)
        # self.textboxAlert.resize(200, 100)
        # self.textboxAlert.move(10, 470)


    ##################################################################################################
        self.show()


    def clickBox(self, state):
        if state == PyQt5.QtCore.Qt.Checked:

            print('Checked :', (int(state)))
            self.Hide = 2
        else:
            self.Hide = 0
            print('Unchecked :', (int(state)))


    #todo TEST! 21 july 2019
    @pyqtSlot()
    def test_Click(self):
        valueX = self.textboxFrameX.text()
        print('value FrameX ',valueX)
        valueY = self.textboxFrameY.text()
        print('value FrameY ', valueY)
        valueW = self.textboxWidth.text()
        print('value Width ', valueW)
        showData = 'Frame X : ' + valueX + ' Frame Y : ' + valueY + ' Frame Width : ' + valueW + ' '
        QMessageBox.question(self, 'Message.get()', 'Set_Value ' + showData, QMessageBox.Ok,
                             QMessageBox.Ok)
        saveValue = int(valueX), int(valueY), int(valueW)
        self.get_position(saveValue)

    # todo TEST! 21 july 2019
    #position X,Y and Width in video.
    def get_position(self,position):
        self.position = position
        print('set position',self.position)

    #todo 12 july. K-means checkColor.  !Slow
    def check_Color(self,pic_Color):
        self.pic_car_color = 'Save\\'+pic_Color
        Kcolors = cv2.imread(self.pic_car_color)
        Kcolors = cv2.cvtColor(Kcolors, cv2.COLOR_BGR2RGB)
        Kcolors = Kcolors.reshape((Kcolors.shape[0] * Kcolors.shape[1], 3))
        clt = KMeans(n_clusters=3)
        clt.fit(Kcolors)
        hist = utils.centroid_histogram(clt)
        print("Histogram : ", hist, "\n")
        bar = utils.plot_colors(hist, clt.cluster_centers_)
        print('Check_Color.',self.pic_car_color)


    #todo 7 july Crop image insert to label.
    def image_Crop(self,locations):
        self.pic_car = locations
        print('location',self.pic_car)
        self.label_name.setText('Saved : '+self.pic_car)
        #print('text','Save\\'+self.pic_car)
        pic_bit = 'Save\\'+self.pic_car
        # cv2.imshow('Car',pic_bit)
        self.pixmap = QPixmap(pic_bit)
        #print('type',type(self.pixmap))
        self.pixmap = self.pixmap.scaled(350, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        print('image_Crop !')

    @pyqtSlot()
    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File : ", "",
                                                  "All Files (*);;Video Files (*.MOV)", options=options)
        if fileName:
            print(fileName)
        self.textbox.setText(fileName)
        QMessageBox.question(self, 'Message.get()', 'Run Video : ' + fileName, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.test_Click() #call Function get Position.
        self.play_Video(fileName)
        return  fileName

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def play_Video(self,name):
        self.path = name
        filePathName = (self.path)  # path_video
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

        path = 'Save';
        data = 'day3-5_';
        last = '.jpg';
        test = "";  # Change
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

                cv2.imshow("Bins", bins)  # bins is threshold. #Disable

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
                            if (cx >= 500 and cx <= 950):  # cx 1200
                                if (cy < 400):  # 600
                                    flag = 0;
                                    # if (cx > 540) and (cx < 540 + 310):
                                if (cx >= 500) and (cx <= 875):
                                    x, y, w, h = cv2.boundingRect(cnt)
                                    if (cy > 470 and (cy < 470 + 30)):  # Line Capture;
                                        vehicle = image[y - 30: y + h + 30, x - 30: x + w]
                                        #cv2.imshow('Detect', vehicle)  # Config  #disable show in gui.
                                        save_file = ('%s%d%s' % (data, counter, last))
                                        go_color = self.check_Color(save_file)
                                        if (flag == 0):
                                            cv2.imwrite(os.path.join(path, save_file), vehicle)  # Save to Folder : Save;
                                            #self.image_Crop(vehicle)
                                            self.image_Crop(save_file) #send location images. ส่งที่อยู่ไฟล์ภาพ
                                            flag = 1;
                                            counter += 1
                                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                                    cv2.putText(image, str(cx) + "," + str(cy), (cx + 10, cy + 10),cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 0, 255), 1)
                                    cv2.drawMarker(image, (cx, cy), (0, 255, 255), cv2.MARKER_CROSS, markerSize=8,thickness=3,line_type=cv2.LINE_8)  # print('Flag==',flag,'CX-------------------',cx,'Y----------------------',y,'Counter===',counter)
                            #print('CX : ', cx, ' CY : ', cy)  #Distance x y of Car
                            # print("sum_pix : ", sum_pix)
            # #todo test draw position. 22 july Finished !
            # draw = self.get_position()
            # print('Draw position ',draw)
            # print('posision is ', self.position)
            image = cv2.rectangle(image, (self.position[0], self.position[1]-260), (self.position[2] + self.position[0], self.position[1]+220), (0, 0, 0), 2)#Black clor  # xy มุมบนซ้าย xyล่างขวา
            image = cv2.line(image, (self.position[0], self.position[1]), (self.position[0] + self.position[2], self.position[1]), (255, 255, 255), 2)  # Line white color
            # #todo

            # image = cv2.rectangle(image, (540, 320), (540 + 310, 320 + 370), (0, 255, 0),2)  Green
            image = cv2.rectangle(image, (500, 212), (875, 690), (255, 0, 0), 2)  # xy มุมบนซ้าย xyล่างขวา
            # image = cv2.line(image, (540, 542), (850, 542), (0, 0, 255), 2)  # Line Red
            image = cv2.line(image, (500, 470), (875, 470), (0, 140, 255), 2)  # Line  Orenge       BGR RGB
            image = cv2.imshow("Day3 : Pro1", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
