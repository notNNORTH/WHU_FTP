# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/common/logo.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#MainWindow{border-image: url(:/resources/common/bg.jpg);}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgba(245, 245, 245, 150);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.clientLbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clientLbl.setFont(font)
        self.clientLbl.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 170, 255, 150);")
        self.clientLbl.setObjectName("clientLbl")
        self.verticalLayout.addWidget(self.clientLbl)
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.verticalLayout.setStretch(1, 13)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.qButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qButton.sizePolicy().hasHeightForWidth())
        self.qButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.qButton.setFont(font)
        self.qButton.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.qButton.setObjectName("qButton")
        self.verticalLayout_2.addWidget(self.qButton)
        self.upButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upButton.sizePolicy().hasHeightForWidth())
        self.upButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.upButton.setFont(font)
        self.upButton.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.upButton.setObjectName("upButton")
        self.verticalLayout_2.addWidget(self.upButton)
        self.ulButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ulButton.sizePolicy().hasHeightForWidth())
        self.ulButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.ulButton.setFont(font)
        self.ulButton.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.ulButton.setObjectName("ulButton")
        self.verticalLayout_2.addWidget(self.ulButton)
        self.dButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dButton.sizePolicy().hasHeightForWidth())
        self.dButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.dButton.setFont(font)
        self.dButton.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.dButton.setObjectName("dButton")
        self.verticalLayout_2.addWidget(self.dButton)
        self.eButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eButton.sizePolicy().hasHeightForWidth())
        self.eButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.eButton.setFont(font)
        self.eButton.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.eButton.setObjectName("eButton")
        self.verticalLayout_2.addWidget(self.eButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.serverLbl = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.serverLbl.setFont(font)
        self.serverLbl.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(128, 128, 128, 150);")
        self.serverLbl.setObjectName("serverLbl")
        self.verticalLayout_4.addWidget(self.serverLbl)
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 10, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.domainEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.domainEdit.setFont(font)
        self.domainEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.domainEdit.setObjectName("domainEdit")
        self.horizontalLayout_4.addWidget(self.domainEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 5)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.portEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.portEdit.setFont(font)
        self.portEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.portEdit.setObjectName("portEdit")
        self.horizontalLayout_5.addWidget(self.portEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 5)
        self.horizontalLayout_5.setStretch(2, 3)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.nameEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.nameEdit.setFont(font)
        self.nameEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.nameEdit.setObjectName("nameEdit")
        self.horizontalLayout_6.addWidget(self.nameEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.pwEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pwEdit.setFont(font)
        self.pwEdit.setStyleSheet("background-color: rgba(255, 255, 255, 200);")
        self.pwEdit.setObjectName("pwEdit")
        self.horizontalLayout_7.addWidget(self.pwEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_7.setStretch(0, 2)
        self.horizontalLayout_7.setStretch(1, 5)
        self.horizontalLayout_7.setStretch(2, 3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.setStretch(0, 5)
        self.horizontalLayout_2.setStretch(1, 5)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FTP Client"))
        self.clientLbl.setText(_translate("MainWindow", "文件目录列表："))
        self.qButton.setText(_translate("MainWindow", "查询"))
        self.upButton.setText(_translate("MainWindow", "上一层"))
        self.ulButton.setText(_translate("MainWindow", "上传"))
        self.dButton.setText(_translate("MainWindow", "下载"))
        self.eButton.setText(_translate("MainWindow", "退出"))
        self.serverLbl.setText(_translate("MainWindow", "远程目录列表（未连接）："))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Size"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Type"))
        self.label.setText(_translate("MainWindow", "域名："))
        self.label_2.setText(_translate("MainWindow", "端口号："))
        self.label_4.setText(_translate("MainWindow", "登录名："))
        self.label_3.setText(_translate("MainWindow", "口令："))

