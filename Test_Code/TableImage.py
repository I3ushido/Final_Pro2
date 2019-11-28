import sys
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, QFileDialog , QAction, QMessageBox, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush, QPen as QtGui
from PyQt5.QtCore import pyqtSlot, Qt, QSize


imagePath = "G:\MyProject_Python\Test_Code\car.jpg"

class ImgWidget1(QLabel):

    def __init__(self, parent=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QtGui.QPixmap(imagePath)
        self.setPixmap(pic)

class ImgWidget2(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ImgWidget2, self).__init__(parent)
        self.pic = QtGui.QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pic)


class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        tableWidget = QtGui.QTableWidget(10, 2, self)
        tableWidget.setCellWidget(0, 1, ImgWidget1(self))
        tableWidget.setCellWidget(1, 1, ImgWidget2(self))

if __name__ == "__main__":
    app = QtGui.QApplication([])
    wnd = Widget()
    wnd.show()
    sys.exit(app.exec_())