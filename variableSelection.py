# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'variableSelection.ui'
#
# Created: Fri Sep 21 14:54:53 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QStandardItemModel


class Ui_variableSelection(object):
    def setupUi(self, variableSelection):
        variableSelection.setObjectName("variableSelection")
        variableSelection.resize(409, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(variableSelection)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.list_left = QtWidgets.QListView(variableSelection)
        self.list_left.setGeometry(QtCore.QRect(30, 40, 161, 191))
        self.list_left.setObjectName("listView")
        self.verticalScrollBar = QtWidgets.QScrollBar(variableSelection)
        self.verticalScrollBar.setGeometry(QtCore.QRect(170, 50, 20, 171))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(variableSelection)
        self.commandLinkButton.setGeometry(QtCore.QRect(190, 120, 31, 41))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.list_right = QtWidgets.QListView(variableSelection)
        self.list_right.setGeometry(QtCore.QRect(230, 40, 151, 191))
        self.list_right.setObjectName("listView_2")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(variableSelection)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(359, 49, 21, 171))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")

        self.retranslateUi(variableSelection)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), variableSelection.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), variableSelection.reject)
        QtCore.QMetaObject.connectSlotsByName(variableSelection)

        self.model_left = QStandardItemModel(self)
        self.list_left.setModel(self.model_left)
        self.model_right = QStandardItemModel(self)
        self.list_right.setModel(self.model_right)


    def retranslateUi(self, variableSelection):
        variableSelection.setWindowTitle(QtWidgets.QApplication.translate("variableSelection", "Dialog", None, -1))

