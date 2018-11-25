from PySide2 import QtGui, QtWidgets, QtCharts
from PySide2.QtCore import QObject, Signal, Slot, Property
from PySide2.QtGui import QStandardItem
from PySide2.QtGui import QStandardItemModel

from scipy.io import loadmat
import ui
import numpy as np
import scipy.io as sio
import sys
import variableSelection


class MainWindow(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    """docstring for MainWindow"""
    sendFilepath = Signal(str)
    openVariableSelectionWindow = Signal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionImport.triggered.connect(self.on_import_button_clicked)
        self.var = VariableSelection(self)
        self.openVariableSelectionWindow.connect(self.var.receive_filepath)
        self.matdata = None

    def on_import_button_clicked(self):
        filepath, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select file to import', dir='.',
                                                                 filter='matlab files (*.mat)')
        if filepath:
            print(filepath)
            matdata = sio.loadmat(filepath)
            matdata = {key: item for key, item in matdata.items() if type(item) == np.ndarray and '__' not in key}

            print(matdata.keys())
            print(matdata)
            # self.emit(QtCore.Signal("openVariableSelectionWindow(str)"), filepath)
            self.openVariableSelectionWindow.emit(filepath)
            self.matdata = matdata

    def plot(self, series):
        self.chartView.chart().addSeries(series)
        self.chartView.chart().createDefaultAxes()
        self.chartView.show()


class VariableSelection(QtWidgets.QDialog, variableSelection.Ui_variableSelection):
    """docstring for VariableSelection"""

    def __init__(self, parent):
        super(VariableSelection, self).__init__(parent)
        self.mainwindow = parent
        self.setupUi(self)
        self.toolButton.clicked.connect(self.move_right)
        self.toolButton_2.clicked.connect(self.move_left)

    @Slot(str)
    def receive_filepath(self, filepath):
        self.populate(filepath)
        self.show()

    def populate(self, filepath):
        lists = sio.loadmat(filepath)
        lists = {key: item for key, item in lists.items() if type(item) == np.ndarray and '__' not in key}
        self.matdata = lists
        for item in lists.keys():
            self.model_left.appendRow(QStandardItem(item))

    def move_right(self):
        index = self.list_left.currentIndex().row()
        item = self.model_left.takeItem(index)
        self.model_right.appendRow(item)
        self.model_left.removeRow(index)
    
    def move_left(self):
        index = self.list_right.currentIndex().row()
        item = self.model_right.takeItem(index)
        self.model_left.appendRow(item)
        self.model_right.removeRow(index)


    def plot(self):
        items = [self.model_right.item(i).text() for i in range(self.model_right.rowCount())]
        print(items)
        print(self.parent)
        series = QtCharts.QtCharts.QLineSeries()
        for item in items:
            t = self.matdata['t'][0]
            data = self.matdata[item][0]
            for x, y in list(zip(t, data)):
                print(x,y)
                series.append(x, y)

        self.variableSelection.hide()
        self.mainwindow.plot(series)


app = QtWidgets.QApplication(sys.argv)

form = MainWindow()
form.show()
sys.exit(app.exec_())
