# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 311)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 160, 88))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.periodbtn = QtWidgets.QButtonGroup(MainWindow)
        self.periodbtn.setObjectName("periodbtn")
        self.periodbtn.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.periodbtn.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.periodbtn.addButton(self.radioButton_3)
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.periodbtn.addButton(self.radioButton_4)
        self.verticalLayout.addWidget(self.radioButton_4)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(180, 80, 160, 111))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temp = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.temp.setObjectName("temp")
        self.parambtn = QtWidgets.QButtonGroup(MainWindow)
        self.parambtn.setObjectName("parambtn")
        self.parambtn.addButton(self.temp)
        self.verticalLayout_2.addWidget(self.temp)
        self.cloud = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.cloud.setObjectName("cloud")
        self.parambtn.addButton(self.cloud)
        self.verticalLayout_2.addWidget(self.cloud)
        self.pressure = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.pressure.setObjectName("pressure")
        self.parambtn.addButton(self.pressure)
        self.verticalLayout_2.addWidget(self.pressure)
        self.wind = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.wind.setObjectName("wind")
        self.parambtn.addButton(self.wind)
        self.verticalLayout_2.addWidget(self.wind)
        self.all = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.all.setObjectName("all")
        self.parambtn.addButton(self.all)
        self.verticalLayout_2.addWidget(self.all)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 180, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_5.setObjectName("radioButton_5")
        self.viewbtn = QtWidgets.QButtonGroup(MainWindow)
        self.viewbtn.setObjectName("viewbtn")
        self.viewbtn.addButton(self.radioButton_5)
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_6.setObjectName("radioButton_6")
        self.viewbtn.addButton(self.radioButton_6)
        self.verticalLayout_3.addWidget(self.radioButton_6)
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(290, 240, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.setcity = QtWidgets.QLineEdit(self.centralwidget)
        self.setcity.setGeometry(QtCore.QRect(20, 10, 131, 20))
        self.setcity.setObjectName("setcity")
        self.setcountry = QtWidgets.QLineEdit(self.centralwidget)
        self.setcountry.setGeometry(QtCore.QRect(220, 10, 113, 20))
        self.setcountry.setObjectName("setcountry")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Погода для народа"))
        self.radioButton_2.setText(_translate("MainWindow", "В данный момент"))
        self.radioButton.setText(_translate("MainWindow", "На сегодня"))
        self.radioButton_3.setText(_translate("MainWindow", "На завтра"))
        self.radioButton_4.setText(_translate("MainWindow", "На неделю"))
        self.temp.setText(_translate("MainWindow", "Температура"))
        self.cloud.setText(_translate("MainWindow", "Облачность"))
        self.pressure.setText(_translate("MainWindow", "Давление"))
        self.wind.setText(_translate("MainWindow", "Ветер"))
        self.all.setText(_translate("MainWindow", "Все показатели"))
        self.radioButton_5.setText(_translate("MainWindow", "Столбик"))
        self.radioButton_6.setText(_translate("MainWindow", "График"))
        self.btnOK.setText(_translate("MainWindow", "Показать"))
        self.setcity.setText(_translate("MainWindow", "Введите город"))
        self.setcountry.setText(_translate("MainWindow", "Введите страну"))

