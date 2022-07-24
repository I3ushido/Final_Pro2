from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import sys
import cv2


class ClickableLabel(QtWidgets.QLabel):

    clicked = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        self.setAcceptDrops(True)
        self.dragstart = None
        self.x0 = self.y0 = 10
        self.x1 = self.y1 = 100

    def paintEvent(self, QPaintEvent):
        self.pt = QPainter(self)
        self.pt.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        self.pt.drawRect(self.x0, self.y0, self.x1 ,self.y1)


    def mousePressEvent(self, event):
        self.x0 = event.x()
        self.y0 = event.y()
        print('start point of x : {} and y : {}'.format(self.x0 ,self.y0))

        if event.buttons() & QtCore.Qt.LeftButton:
            self.dragstart = event.pos()
            self.clicked.emit()

    def mouseReleaseEvent(self, event):
        self.dragstart = None
        # self.x1 = event.x()
        # self.y1 = event.y()
        # print('end point of x : {} and y : {}'.format(self.x1, self.y1))
        print("End !")



    def mouseMoveEvent(self, event):
        self.x1 = event.x()
        self.y1 = event.y()
        print('end point of x : {} and y : {}'.format(self.x1, self.y1))
        # self.pt.drawRect(self.x0, self.y0, self.x1, self.y1)
        # self.label01 = cv2.rectangle(self.label01, (self.x0, self.y0), (self.x1, self.y1), (0, 255, 0), 2)
        # self.paintEvent()

        if (self.dragstart is not None and
            event.buttons() & QtCore.Qt.LeftButton and  (event.pos() - self.dragstart).manhattanLength() >  QtWidgets.qApp.startDragDistance()):
            self.dragstart = None
            drag = QtGui.QDrag(self)
            drag.setMimeData(QtCore.QMimeData())
            drag.exec_(QtCore.Qt.LinkAction)


    def dragEnterEvent(self, event):
        event.acceptProposedAction()
        if event.source() is not self:
            self.clicked.emit()


class MainWindow(QtWidgets.QMainWindow,ClickableLabel):
    img = cv2.imread('car.jpg')
    def __init__(self):
        super().__init__()
        central_widget = QtWidgets.QWidget()

        self.setFixedSize(500, 500)
        image = Image.open("car.jpg")
        image_imageqt = ImageQt(image)

        hbox = QtWidgets.QHBoxLayout()
        hbox.setSpacing(0)
        hbox.addStretch()

        label01 = ClickableLabel()
        label01.setPixmap(QtGui.QPixmap.fromImage(image_imageqt))
        label01.clicked.connect(self.print_text)
        hbox.addWidget(label01)

        # label02 = ClickableLabel()
        # label02.setPixmap(QtGui.QPixmap.fromImage(image_imageqt))
        # label02.clicked.connect(self.print_text)
        # hbox.addWidget(label02)
        #
        # label03 = ClickableLabel()
        # label03.setPixmap(QtGui.QPixmap.fromImage(image_imageqt))
        # label03.clicked.connect(self.print_text)
        # hbox.addWidget(label03)

        hbox.addStretch()

        central_widget.setLayout(hbox)

        self.setCentralWidget(central_widget)

    def print_text(self):
        print("Clicked...")

    # cv2.rectangle(img, (100, 10), (540 + 310, 320 + 370), (0, 255, 0), 2)
    # cv2.imshow('car',img)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowTitle("TEST_DRAW.")
    main_window.show()
    sys.exit(app.exec_())