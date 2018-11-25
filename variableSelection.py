# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variableselection2.ui'
#
# Created: Wed Oct 31 17:05:57 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QStandardItemModel


class Ui_variableSelection(object):
    def setupUi(self, variableSelection):
        self.variableSelection = variableSelection
        variableSelection.setObjectName("variableSelection")
        variableSelection.resize(409, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(variableSelection)
        self.buttonBox.setGeometry(QtCore.QRect(230, 260, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.list_left = QtWidgets.QListView(variableSelection)
        self.list_left.setGeometry(QtCore.QRect(30, 60, 141, 191))
        self.list_left.setObjectName("listView")
        self.toolButton = QtWidgets.QToolButton(variableSelection)
        self.toolButton.setGeometry(QtCore.QRect(190, 100, 41, 31))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(QtCore.Qt.RightArrow)
        self.toolButton.setObjectName("addButton")
        self.toolButton_2 = QtWidgets.QToolButton(variableSelection)
        self.toolButton_2.setGeometry(QtCore.QRect(190, 180, 41, 31))
        self.toolButton_2.setArrowType(QtCore.Qt.LeftArrow)
        self.toolButton_2.setObjectName("removeButton")
        self.list_right = QtWidgets.QListView(variableSelection)
        self.list_right.setGeometry(QtCore.QRect(240, 60, 141, 191))
        self.list_right.setObjectName("listView_2")
        self.label = QtWidgets.QLabel(variableSelection)
        self.label.setGeometry(QtCore.QRect(40, 20, 361, 20))
        self.label.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.retranslateUi(variableSelection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.plot)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), variableSelection.reject)
        QtCore.QMetaObject.connectSlotsByName(variableSelection)

        self.model_left = QStandardItemModel(self)
        self.list_left.setModel(self.model_left)
        self.model_right = QStandardItemModel(self)
        self.list_right.setModel(self.model_right)



    def retranslateUi(self, variableSelection):
        variableSelection.setWindowTitle(QtWidgets.QApplication.translate("variableSelection", "Dialog", None, -1))
        self.toolButton.setText(QtWidgets.QApplication.translate("variableSelection", "...", None, -1))
        self.toolButton_2.setText(QtWidgets.QApplication.translate("variableSelection", "...", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("variableSelection", "Please select which variables will be plotted and add it to the right list", None, -1))

