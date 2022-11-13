# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 232)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background: white;\n"
                                 "}\n"
                                 "QPushButton {\n"
                                 "background-color: rgb(160, 160, 160);\n"
                                 "border-radius: 17%;\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgb(96, 96, 96);\n"
                                 "}\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 241, 31))
        self.lineEdit.setStyleSheet("border: none;\n"
                                    "border-bottom: 2px solid grey;\n"
                                    "color: black;\n"
                                    "padding-bottom: 7px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 100, 241, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgbaa(0, 0, 0, 0%);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid grey;\n"
                                      "color: black;\n"
                                      "padding-bottom: 7px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 141, 39))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 151, 16))
        self.label.setStyleSheet("background-color: white;\n"
                                 "color: white;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "E-mail"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        self.label.setText(_translate("MainWindow", "Неверный логин или пароль"))
