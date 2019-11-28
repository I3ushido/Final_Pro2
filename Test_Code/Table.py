import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot



imagePath = "G:\MyProject_Python\Test_Code\\batman.png"
class ImgWidget1(QLabel):

    def __init__(self, parent=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QPixmap(imagePath)
        self.setPixmap(pic)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createTable()

        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('batman.png')
        label.setPixmap(pixmap)
        # self.resize(pixmap.width(), pixmap.height())


        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setColumnWidth(20000, 200000)
        self.tableWidget.setColumnWidth(20000, 20000)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        # self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.setCellWidget(3,1 , ImgWidget1(self))
        self.tableWidget.move(0, 0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())