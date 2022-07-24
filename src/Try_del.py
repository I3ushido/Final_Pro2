#BattlePass
import PyQt5
import numpy as np
import cv2
import os
import time
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, QFileDialog , QAction, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, Qt, QSize, QThread, pyqtSignal

class Thread(QThread):
    filePathName = ('Day3/3-5.MOV')
    print(filePathName)
    changePixmap = pyqtSignal(QImage)

    def run(self):
        cap = cv2.VideoCapture(self.filePathName)
        print('cap : ',cap)
        while True:
            ret, frame = cap.read()
            if not ret:
                frame = cv2.VideoCapture(self.filePathName)
                continue
            if ret:

                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = PyQt5.QtGui.QImage(rgbImage.data, w, h, bytesPerLine, PyQt5.QtGui.QImage.Format_RGB888)
                p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.changePixmap.emit(p)



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Video'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resize(1800, 1200)
        #create a label
        label = QLabel(self)
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        convertToQtFormat = PyQt5.QtGui.QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                         PyQt5.QtGui.QImage.Format_RGB888)
        convertToQtFormat = PyQt5.QtGui.QPixmap.fromImage(convertToQtFormat)
        pixmap = QPixmap(convertToQtFormat)
        resizeImage = pixmap.scaled(640, 480, PyQt5.QtCore.Qt.KeepAspectRatio)
        QApplication.processEvents()
        label.setPixmap(resizeImage)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    th.start()