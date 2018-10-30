# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Aula\estagio\projeto\pCAT\mainwindow.ui'
#
# Created: Tue Jun  5 16:59:06 2018
#      by: pyside2-uic  running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 391)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 728, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuNew_Project = QtWidgets.QMenu(self.menuFile)
        self.menuNew_Project.setObjectName("menuNew_Project")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionQt_License = QtWidgets.QAction(MainWindow)
        self.actionQt_License.setObjectName("actionQt_License")
        self.actionPySide2 = QtWidgets.QAction(MainWindow)
        self.actionPySide2.setObjectName("actionPySide2")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuNew_Project.addAction(self.actionImport)
        self.menuFile.addAction(self.menuNew_Project.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionQt_License)
        self.menuAbout.addAction(self.actionPySide2)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionVersion)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "pCAT", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuNew_Project.setTitle(QtWidgets.QApplication.translate("MainWindow", "New Project or File", None, -1))
        self.menuTools.setTitle(QtWidgets.QApplication.translate("MainWindow", "Tools", None, -1))
        self.menuAbout.setTitle(QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.actionImport.setText(QtWidgets.QApplication.translate("MainWindow", "Import...", None, -1))
        self.actionQt_License.setText(QtWidgets.QApplication.translate("MainWindow", "Qt License", None, -1))
        self.actionPySide2.setText(QtWidgets.QApplication.translate("MainWindow", "PySide2", None, -1))
        self.actionHelp.setText(QtWidgets.QApplication.translate("MainWindow", "Documentation", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionVersion.setText(QtWidgets.QApplication.translate("MainWindow", "Version", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))



    