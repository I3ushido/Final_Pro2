import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLabel, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, Qt, QSize


class App(QWidget):
    global fileName
    def __init__(self):
        super().__init__()
        self.title = 'Hello :)'
        self.left = 0
        self.top = 0
        self.width = 1360
        self.height = 900

        self.initUI()


    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # self.setGeometry(100, 100, 1400, 900)
        self.center()

        #Button
        self.button = QPushButton('Say Hi', self)
        self.button.setToolTip('Button Hello.')
        self.button.move(0, 0)
        self.button.clicked.connect(self.on_click)

        self.FilePath = self.on_click()
        print("Self Path : ",self.FilePath)
        # Create widget
        label = QLabel(self)
        label.resize(1280, 720)
        label.move(80, 0)
        #pixmap = QPixmap('img.png')
        pixmap = QPixmap(self.FilePath)
        pixmap = pixmap.scaled(1280,720,Qt.KeepAspectRatio)

        label.setPixmap(pixmap)

        #self.resize(pixmap.width(), pixmap.height())
        self.show()

    @pyqtSlot()
    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File : ", "",
                                                  "All Files (*);;Video Files (*.MOV)", options=options)
        if fileName:
            print(fileName)
        print('Hi :)')
        return  fileName

    def center(self):
        qr = self.frameGeometry()
        #cp = QDesktopWidget().availableGeometry().center()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())