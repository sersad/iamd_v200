# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './main_wnd.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 398)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(807, 398))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 781, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.TrackName = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.TrackName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.TrackName.setObjectName("TrackName")
        self.verticalLayout.addWidget(self.TrackName)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LocalButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.LocalButton.setChecked(True)
        self.LocalButton.setObjectName("LocalButton")
        self.RadioBtnGroup = QtWidgets.QButtonGroup(MainWindow)
        self.RadioBtnGroup.setObjectName("RadioBtnGroup")
        self.RadioBtnGroup.addButton(self.LocalButton)
        self.horizontalLayout_2.addWidget(self.LocalButton)
        self.RadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.RadioButton.setObjectName("RadioButton")
        self.RadioBtnGroup.addButton(self.RadioButton)
        self.horizontalLayout_2.addWidget(self.RadioButton)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setMaximumSize(QtCore.QSize(24, 24))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/img/minus.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.VolumeSlider = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.VolumeSlider.setProperty("value", 99)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayout_2.addWidget(self.VolumeSlider)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(24, 24))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui/img/plus.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.TimeLabel = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.TimeLabel.setMaximumSize(QtCore.QSize(200, 16777215))
        self.TimeLabel.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.TimeLabel.setObjectName("TimeLabel")
        self.horizontalLayout_2.addWidget(self.TimeLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OpenButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/img/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenButton.setIcon(icon)
        self.OpenButton.setObjectName("OpenButton")
        self.horizontalLayout.addWidget(self.OpenButton)
        self.StopButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton.setIcon(icon1)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout.addWidget(self.StopButton)
        self.PlayButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui/img/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayButton.setIcon(icon2)
        self.PlayButton.setObjectName("PlayButton")
        self.horizontalLayout.addWidget(self.PlayButton)
        self.PrevButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui/img/prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PrevButton.setIcon(icon3)
        self.PrevButton.setObjectName("PrevButton")
        self.horizontalLayout.addWidget(self.PrevButton)
        self.NextButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui/img/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon4)
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout.addWidget(self.NextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PlayList = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.PlayList.sizePolicy().hasHeightForWidth())
        self.PlayList.setSizePolicy(sizePolicy)
        self.PlayList.setObjectName("PlayList")
        self.horizontalLayout_3.addWidget(self.PlayList)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.ImageLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImageLabel.sizePolicy().hasHeightForWidth())
        self.ImageLabel.setSizePolicy(sizePolicy)
        self.ImageLabel.setMaximumSize(QtCore.QSize(150, 150))
        self.ImageLabel.setText("")
        self.ImageLabel.setPixmap(QtGui.QPixmap("../docs/no-image.jpg"))
        self.ImageLabel.setScaledContents(True)
        self.ImageLabel.setObjectName("ImageLabel")
        self.horizontalLayout_3.addWidget(self.ImageLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.Errorlabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Errorlabel.sizePolicy().hasHeightForWidth())
        self.Errorlabel.setSizePolicy(sizePolicy)
        self.Errorlabel.setText("")
        self.Errorlabel.setObjectName("Errorlabel")
        self.verticalLayout_2.addWidget(self.Errorlabel)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radio for amplifier I.AM.D v200"))
        self.TrackName.setText(_translate("MainWindow", "TrackName"))
        self.LocalButton.setText(_translate("MainWindow", "Local"))
        self.RadioButton.setText(_translate("MainWindow", "I.AM.D v200"))
        self.OpenButton.setText(_translate("MainWindow", "Open"))
        self.StopButton.setText(_translate("MainWindow", "Stop"))
        self.PlayButton.setText(_translate("MainWindow", "Play"))
        self.PrevButton.setText(_translate("MainWindow", "Prev"))
        self.NextButton.setText(_translate("MainWindow", "Next"))

