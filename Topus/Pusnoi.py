import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, \
    QFileDialog, QAction, QMessageBox, QMainWindow, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QSize
from keras.models import load_model
import numpy as np
import cv2
import math
from scipy.spatial import distance
import mysql.connector
class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Ai'
        self.left = 100
        self.top = 100
        self.width = 1700
        self.height = 900
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #brows pic
        self.button = QPushButton('Browse file', self)
        self.button.setToolTip('For brows file')
        self.button.resize(125, 50)
        self.button.move(10, 10)
        self.button.clicked.connect(self.on_click)

        self.label = QLabel(self)
        self.label.resize(350, 400)
        self.label.move(10, 200)

        self.img1 = QLabel(self)
        self.img1.resize(350, 400)
        self.img1.move(400, 60)
        self.n1 = QLabel(self)
        self.n1.resize(350, 400)
        self.n1.move(400, 200)

        self.img2 = QLabel(self)
        self.img2.resize(350, 400)
        self.img2.move(650, 60)
        self.n2 = QLabel(self)
        self.n2.resize(350, 400)
        self.n2.move(650, 200)

        self.img3 = QLabel(self)
        self.img3.resize(350, 400)
        self.img3.move(900, 60)
        self.n3 = QLabel(self)
        self.n3.resize(350, 400)
        self.n3.move(900, 200)
        #
        self.img4 = QLabel(self)
        self.img4.resize(350, 400)
        self.img4.move(1150, 60)
        self.n4 = QLabel(self)
        self.n4.resize(350, 400)
        self.n4.move(1150, 200)
        #
        self.img5 = QLabel(self)
        self.img5.resize(350, 400)
        self.img5.move(1400, 60)
        self.n5 = QLabel(self)
        self.n5.resize(350, 400)
        self.n5.move(1400, 200)
        #
        self.img6 = QLabel(self)
        self.img6.resize(350, 400)
        self.img6.move(400, 400)
        self.n6 = QLabel(self)
        self.n6.resize(350, 400)
        self.n6.move(400, 550)
        #
        self.img7 = QLabel(self)
        self.img7.resize(350, 400)
        self.img7.move(650, 400)
        self.n7 = QLabel(self)
        self.n7.resize(350, 400)
        self.n7.move(650, 550)
        #
        self.img8 = QLabel(self)
        self.img8.resize(350, 400)
        self.img8.move(900, 400)
        self.n8 = QLabel(self)
        self.n8.resize(350, 400)
        self.n8.move(900, 550)
        #
        self.img9 = QLabel(self)
        self.img9.resize(350, 400)
        self.img9.move(1150, 400)
        self.n9 = QLabel(self)
        self.n9.resize(350, 400)
        self.n9.move(1150, 550)
        #
        self.img10 = QLabel(self)
        self.img10.resize(350, 400)
        self.img10.move(1400, 400)
        self.n10 = QLabel(self)
        self.n10.resize(350, 400)
        self.n10.move(1400, 550)



        # pixmap = QPixmap('pic.jpg')
        # pixmap = pixmap.scaled(350, 400, Qt.KeepAspectRatio)
        # label.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())

        c_button = QPushButton('Prediction CNN', self)
        c_button.setToolTip('Prediction CNN')
        c_button.resize(125, 50)
        c_button.move(200, 10)
        c_button.clicked.connect(self._cnn)

        h_button = QPushButton('Prediction Histogram', self)
        h_button.setToolTip('Prediction Histogram')
        h_button.resize(125, 50)
        h_button.move(350, 10)
        h_button.clicked.connect(self._his)



        self.show()



    def on_click(self):

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File : ", "",
                                                  "All Files (*);;Video Files (*.PNG)", options=options)

        if fileName:
            print(fileName)
        # self.textbox.setText(fileName)
        # QMessageBox.question(self, 'Message.get()', 'Run Video : ' + fileName, QMessageBox.Ok, QMessageBox.Ok)
        pixmap = QPixmap(fileName)
        pixmap = pixmap.scaled(350, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        f = open('Path.txt', 'w')
        for i in fileName:
            f.write(str(i))
        f.close()
        # return fileName

    def _his(self):
        f = open('Path.txt', 'r')
        s = f.read()
        f.close()
        img = cv2.imread(s, 0)
        m, n = img.shape
        data = img
        data = [0] * 10
        a = math.floor(m / 3)
        b = math.floor(n / 3)
        data[0] = img[0:a, 0:b]
        data[1] = img[0:a, b:b + b]
        b = math.floor(n / 3) + math.floor(n / 3)
        data[2] = img[0:a, b:b + math.floor(n / 3)]
        data[3] = img[a:a + a, 0:math.floor(n / 3)]
        data[4] = img[a:a + a, math.floor(n / 3):b]
        b = math.floor(n / 3) + math.floor(n / 3)
        data[5] = img[a:a + a, b:b + math.floor(n / 3)]
        a = math.floor(m / 3) + math.floor(m / 3)
        b = math.floor(n / 3)
        data[6] = img[a:a + math.floor(m / 3), 0:b]
        data[7] = img[a:a + math.floor(m / 3), b:b + b]
        b = math.floor(n / 3) + math.floor(n / 3)
        data[8] = img[a:a + math.floor(m / 3), b:b + math.floor(n / 3)]
        hrgb = []
        for i in range(9):
            cout = 0
            couttt = 64
            his = cv2.calcHist([data[i]], [0], None, [256], [0, 256])
            for j in range(4):
                hrgb.append(np.sum(his[cout:couttt]))
                cout = cout + 64
                couttt = couttt + 64

        hrgb2 = []
        angidmax = sorted(hrgb, reverse=True)
        for datahrgb in hrgb:
            hrgb2.append(datahrgb / angidmax[0])

        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='dbmovie',
                                                  user='root',
                                                  password='')
        sql_select_Query = "SELECT image,his FROM movie "
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        id = []
        rangmovie = []
        Qrangmovie = []

        # to 0
        for row in records:
            item = str(row[1])
            q = item.split(" ")
            for i in range(0, 36):
                Qrangmovie.append(float(q[i]))
            dst = distance.euclidean(hrgb2, Qrangmovie)
            Qrangmovie.clear()
            rangmovie.append(dst)
            id.append(row[0])
        rangidmax = sorted(zip(rangmovie, id))

        #To 1
        # for row in records:
        #     item = str(row[1])
        #     q = item.split(" ")
        #     sum = 0
        #     pip = 0
        #     piq = 0
        #     for i in range(0, 16):
        #         q[i] = float(q[i])
        #         sum = sum + (hrgb2[i] * q[i])
        #         pip = pip + (hrgb2[i] ** 2)
        #         piq = piq + (q[i] ** 2)
        #
        #     dst = sum / (math.sqrt(pip) * math.sqrt(piq))
        #     Qrangmovie.clear()
        #     rangmovie.append(dst)
        #     id.append(row[0])
        # rangidmax = sorted(zip(rangmovie, id),reverse=True)

        print(rangidmax)
        reqmovie = []
        for zxc in range(12):
            reqmovie.append(rangidmax[zxc][1])
        f = open('rank.txt', 'w')
        for i in reqmovie:
            f.write(str(i) + " ")
        f.close()
        cursor.close()
        id.clear()
        rangmovie.clear()


    def _cnn(self):
        model = load_model('500LastNewCnn.cnn')
        f = open('Path.txt', 'r')
        s = f.read()
        f.close()
        imt = cv2.imread(s)
        imt = cv2.resize(imt, (28, 28))
        imt = cv2.cvtColor(imt, cv2.COLOR_BGR2GRAY)
        x = imt
        x = x.astype('float32') / 255.0
        x = np.reshape(x, (-1, 28, 28, 1))
        test = model.predict(x)
        fac = np.resize(test, (28, 28, 1))
        facten = []
        for i in fac:
            for j in i:
                facten.append(j)
        cnn = []
        cout = 0
        couttt = 8
        for i in range(98):
            cnn.append(np.sum(facten[cout:couttt]))
            cout = cout + 8
            couttt = couttt + 8
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='dbmovie',
                                                  user='root',
                                                  password='')
        sql_select_Query = "SELECT image,cnn FROM movie WHERE id > 3047 "
        cursor = mySQLconnection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        id = []
        rangmovie = []
        Qrangmovie = []

        for row in records:
            item = str(row[1])
            q = item.split(" ")
            for i in range(0, 98):
                Qrangmovie.append(float(q[i]))
            dst = distance.euclidean(cnn, Qrangmovie)
            Qrangmovie.clear()
            rangmovie.append(dst)
            id.append(row[0])
        rangidmax = sorted(zip(rangmovie, id))

        #TO 1
        # for row in records:
        #     item = str(row[1])
        #     q = item.split(" ")
        #     sum = 0
        #     pip = 0
        #     piq = 0
        #     for i in range(0, 16):
        #         q[i] = float(q[i])
        #         sum = sum + (hrgb2[i] * q[i])
        #         pip = pip + (hrgb2[i] ** 2)
        #         piq = piq + (q[i] ** 2)
        #
        #     dst = sum / (math.sqrt(pip) * math.sqrt(piq))
        #     Qrangmovie.clear()
        #     rangmovie.append(dst)
        #     id.append(row[0])
        # rangidmax = sorted(zip(rangmovie, id),reverse=True)

        reqmovie = []
        for zxc in range(12):
            reqmovie.append(rangidmax[zxc][1])

        f = open('rank.txt', 'w')
        for i in reqmovie:
            f.write(str(i) + " ")
        f.close()
        cursor.close()
        id.clear()
        rangmovie.clear()

    def _show(self):
        im1 = QPixmap("272.jpg")
        im1 = im1.scaled(200, 250, Qt.KeepAspectRatio)
        self.img1.setPixmap(im1)
        self.n1.setText("OK")

        im2 = QPixmap("272.jpg")
        im2 = im2.scaled(200, 250, Qt.KeepAspectRatio)
        self.img2.setPixmap(im2)
        self.n2.setText("OK")

        im3 = QPixmap("272.jpg")
        im3 = im3.scaled(200, 250, Qt.KeepAspectRatio)
        self.img3.setPixmap(im3)
        self.n3.setText("OK")

        im4 = QPixmap("272.jpg")
        im4 = im4.scaled(200, 250, Qt.KeepAspectRatio)
        self.img4.setPixmap(im4)
        self.n4.setText("OK")

        im5 = QPixmap("272.jpg")
        im5 = im5.scaled(200, 250, Qt.KeepAspectRatio)
        self.img5.setPixmap(im5)
        self.n5.setText("OK")

        im6 = QPixmap("272.jpg")
        im6 = im6.scaled(200, 250, Qt.KeepAspectRatio)
        self.img6.setPixmap(im6)
        self.n6.setText("OsdfsdfsdfK")

        im7 = QPixmap("272.jpg")
        im7 = im7.scaled(200, 250, Qt.KeepAspectRatio)
        self.img7.setPixmap(im7)
        self.n7.setText("OsdfsdfsdfK")

        im8 = QPixmap("272.jpg")
        im8 = im8.scaled(200, 250, Qt.KeepAspectRatio)
        self.img8.setPixmap(im8)
        self.n8.setText("OsdfsdfsdfK")

        im9 = QPixmap("272.jpg")
        im9 = im9.scaled(200, 250, Qt.KeepAspectRatio)
        self.img9.setPixmap(im9)
        self.n9.setText("OsdfsdfsdfK")

        im10 = QPixmap("272.jpg")
        im10 = im10.scaled(200, 250, Qt.KeepAspectRatio)
        self.img10.setPixmap(im10)
        self.n10.setText("OsdfsdfsdfK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
