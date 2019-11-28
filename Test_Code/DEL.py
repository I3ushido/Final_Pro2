from PyQt5 import QtGui, QtCore, QtWidgets
import numpy as np

#-- Table Model
class MyTableModel(QtCore.QAbstractTableModel):

    def __init__(self, data, parent=None, *args):
        super(MyTableModel, self).__init__(parent)

        # table data
        self.table_data = data
        self.rows_nr, self.columns_nr = data.shape

        # vertical & horizontal header labels
        self.hheaders = ["Head-{}".format(i) for i in range(self.columns_nr)]
        self.vheaders = ["Row-{}".format(i) for i in range(self.rows_nr)]

    # nr of rows
    def rowCount(self, parent):
        return self.rows_nr

    # nr of columns
    def columnCount(self, parent):
        return self.columns_nr

    # row and column headers
    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.hheaders[section]
            #END if

        #ELSE:
        return QtCore.QVariant()

    # display table contents
    def data(self, index, role=QtCore.Qt.DisplayRole):
        r_ = index.row()
        c_ = index.column()

        if role == QtCore.Qt.DisplayRole:
            return "{}".format(data[r_, c_])
        #ELSE:
        return QtCore.QVariant()

    # set data
    def setData(self, index, value, role):

        r_ = index.row()
        c_ = index.column()

        # editable fields
        if role == QtCore.Qt.EditRole:
            # interprete values
            self.table_data[r_,c_] = str(value)

        return True

    # view/edit flags
    def flags(self, index):
        r_ = index.row()
        c_ = index.column()

        return QtCore.Qt.ItemIsEnabled


class MyTableWidget(QtWidgets.QWidget):
    def __init__(self, data, *args):
        super(MyTableWidget, self).__init__(*args)

        #-- table model
        tablemodel = MyTableModel(data=data, parent=self)

        #-- table view
        tableview = QtWidgets.QTableView()
        tableview.setModel(tablemodel)
        tableview.verticalHeader().hide() # hide vertical/row headers

        #-- +++
        tableview.setAlternatingRowColors(True)
        tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tableview.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        tableview.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        tableview.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

        # size policy
        tableview.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        #tableview.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum) # ---
        tableview.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)# +++

        #-- layouts
        #--- buttons
        button_hlayout = QtWidgets.QHBoxLayout()
        button_hlayout.addWidget(QtWidgets.QPushButton("Button 1"))
        button_hlayout.addWidget(QtWidgets.QPushButton("Button 2"))
        button_hlayout.addWidget(QtWidgets.QPushButton("Button 3"))

        #--- table
        table_layout = QtWidgets.QVBoxLayout()
        table_layout.addLayout(button_hlayout)
        table_layout.addWidget(tableview)
        self.setLayout(table_layout)
#----------------------------------------

#-- produce sample data
x = 3
xx= 4
data = np.empty(shape=(x,xx), dtype=np.object)
for r in range(x):
    for c in range(xx):
        data[r,c] = str(list(range((r+1) * (c+1))))

app = QtWidgets.QApplication([""])
w = MyTableWidget(data=data)
w.show()
app.exec_()