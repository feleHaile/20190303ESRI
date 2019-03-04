# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'esridemo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EsriApp(object):
    def setupUi(self, EsriApp):
        EsriApp.setObjectName("EsriApp")
        EsriApp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(EsriApp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(25, 29, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        EsriApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EsriApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        EsriApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EsriApp)
        self.statusbar.setObjectName("statusbar")
        EsriApp.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(EsriApp)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(EsriApp)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(EsriApp)
        QtCore.QMetaObject.connectSlotsByName(EsriApp)

    def retranslateUi(self, EsriApp):
        _translate = QtCore.QCoreApplication.translate
        EsriApp.setWindowTitle(_translate("EsriApp", "MainWindow"))
        self.pushButton_2.setText(_translate("EsriApp", "Go"))
        self.pushButton.setText(_translate("EsriApp", "Stop"))
        self.menuFile.setTitle(_translate("EsriApp", "File"))
        self.menuEdit.setTitle(_translate("EsriApp", "Edit"))
        self.actionOpen.setText(_translate("EsriApp", "Open..."))
        self.actionQuit.setText(_translate("EsriApp", "Quit"))


