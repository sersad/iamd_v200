# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './form_add.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(845, 398)
        Form.setMinimumSize(QtCore.QSize(700, 398))
        Form.setMaximumSize(QtCore.QSize(845, 398))
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 821, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setObjectName("formLayout")
        self.labelName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelName)
        self.lineEditName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditName.setObjectName("lineEditName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditName)
        self.labelURL = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelURL.setObjectName("labelURL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelURL)
        self.lineEditURL = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditURL.setObjectName("lineEditURL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditURL)
        self.labelBitrate = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelBitrate.setObjectName("labelBitrate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelBitrate)
        self.lineEditBitrate = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditBitrate.setObjectName("lineEditBitrate")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditBitrate)
        self.labelImage = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelImage.setObjectName("labelImage")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelImage)
        self.pushButtonAddImage = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAddImage.setObjectName("pushButtonAddImage")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pushButtonAddImage)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonAdd = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.verticalLayout_3.addWidget(self.pushButtonAdd)
        self.pushButtonDelete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonDelete.setObjectName("pushButtonDelete")
        self.verticalLayout_3.addWidget(self.pushButtonDelete)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Playlist Editor"))
        self.labelName.setText(_translate("Form", "Имя"))
        self.labelURL.setText(_translate("Form", "URL"))
        self.labelBitrate.setText(_translate("Form", "Bitrate"))
        self.labelImage.setText(_translate("Form", "Иконка"))
        self.pushButtonAddImage.setText(_translate("Form", "Добавить изображение"))
        self.pushButtonAdd.setText(_translate("Form", "Добавить"))
        self.pushButtonDelete.setText(_translate("Form", "Удалить"))
        self.tableWidget.setSortingEnabled(False)

