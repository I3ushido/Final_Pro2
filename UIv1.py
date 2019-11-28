import sys
from PyQt5.QtWidgets import *
#import QWidget, QDesktopWidget, QApplication, *


class Example(QWidget):

    button = QPushButton('Click')

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(1280, 720)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_button_clicked():
        alert = QMessageBox()
        alert.setText('Hello !')
        alert.exec_()

    button.clicked.connect(on_button_clicked)
    button.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())