# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'status_info_display.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.label_motion = QtWidgets.QLabel(self.groupBox)
        self.label_motion.setGeometry(QtCore.QRect(12, 32, 731, 17))
        self.label_motion.setObjectName("label_motion")
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_security = QtWidgets.QLabel(self.groupBox_2)
        self.label_security.setGeometry(QtCore.QRect(10, 40, 721, 17))
        self.label_security.setObjectName("label_security")
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_pcan = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_pcan.setObjectName("pushButton_pcan")
        self.gridLayout_2.addWidget(self.pushButton_pcan, 0, 0, 1, 1)
        self.pushButton_vcan = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_vcan.setObjectName("pushButton_vcan")
        self.gridLayout_2.addWidget(self.pushButton_vcan, 0, 1, 1, 1)
        self.pushButton_serial = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_serial.setObjectName("pushButton_serial")
        self.gridLayout_2.addWidget(self.pushButton_serial, 0, 2, 1, 1)
        self.pushButton_status = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_status.setObjectName("pushButton_status")
        self.gridLayout_2.addWidget(self.pushButton_status, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "运动反馈"))
        self.label_motion.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "安全反馈"))
        self.label_security.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "测试初始化"))
        self.pushButton_pcan.setText(_translate("MainWindow", "初始化pcan"))
        self.pushButton_vcan.setText(_translate("MainWindow", "初始化vcan"))
        self.pushButton_serial.setText(_translate("MainWindow", "初始化serial"))
        self.pushButton_status.setText(_translate("MainWindow", "显示状态"))
