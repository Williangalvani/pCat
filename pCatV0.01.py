from PySide2 import QtGui, QtWidgets
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

    def on_import_button_clicked(self):
        filepath, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Select file to import', dir='.',
                                                                 filter='matlab files (*.mat)')
        if filepath:
            print(filepath)
            matdata = sio.loadmat(filepath)
            print(matdata.keys())
            # self.emit(QtCore.Signal("openVariableSelectionWindow(str)"), filepath)
            self.openVariableSelectionWindow.emit(filepath)


class VariableSelection(QtWidgets.QDialog, variableSelection.Ui_variableSelection):
    """docstring for VariableSelection"""

    def __init__(self, parent):
        super(VariableSelection, self).__init__(parent)
        self.setupUi(self)
        self.toolButton.clicked.connect(self.move_right)
        self.toolButton_2.clicked.connect(self.move_left)

    @Slot(str)
    def receive_filepath(self, filepath):
        self.populate(filepath)
        self.show()

    def populate(self, filepath):
        lists = sio.loadmat(filepath).keys()
        for item in lists:
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


app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
sys.exit(app.exec_())
