# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driving_information_board.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_lateral_error = QtWidgets.QLabel(self.groupBox)
        self.label_lateral_error.setObjectName("label_lateral_error")
        self.gridLayout_3.addWidget(self.label_lateral_error, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_0 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_0.setObjectName("textEdit_0")
        self.verticalLayout.addWidget(self.textEdit_0)
        self.pushButton_load = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.pushButton_ori_start = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_ori_start.setObjectName("pushButton_ori_start")
        self.verticalLayout.addWidget(self.pushButton_ori_start)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_interrupt = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_interrupt.setObjectName("pushButton_interrupt")
        self.gridLayout_2.addWidget(self.pushButton_interrupt, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "driving_information_board"))
        self.groupBox.setTitle(_translate("MainWindow", "横向误差"))
        self.label_lateral_error.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_load.setText(_translate("MainWindow", "加载左侧任务"))
        self.pushButton_ori_start.setText(_translate("MainWindow", "从0任务0点开始"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.pushButton_start.setText(_translate("MainWindow", "加载任务，开始作业"))
        self.pushButton_interrupt.setText(_translate("MainWindow", "中断任务"))
