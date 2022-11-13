# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import multiprocessing
import MainProject.UI.data_input as di
import MainProject.UI.transactions_list as tl
from MainProject.Worker import Worker

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, dolphin):
        self.dolphin = dolphin
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(820, 500)
        MainWindow.setStyleSheet("QMainWindow {\n"
                                 "background: white;\n"
                                 "}\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 820, 487))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setStyleSheet("background-color: white;")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.profiles = self.dolphin.get_profiles()
        self.label = QtWidgets.QLabel(self.scrollArea)
        self.label.setText('\n'.join(['.' for i in self.profiles]))
        self.label.setObjectName("none")
        self.label.setStyleSheet("QPushButton {\n"
                                 "background-color: rgb(160, 160, 160);\n"
                                 "border-radius: 17%;\n"
                                 "color: white;\n"
                                 "}\n"
                                 "QPushButton:hover {\n"
                                 "background-color: rgb(96, 96, 96);\n"
                                 "}\n"
                                 "QLabel#none {\n"
                                 "color: white;\n"
                                 "}\n")
        self.label_1 = QtWidgets.QLabel(self.label)
        self.label_1.setGeometry(QtCore.QRect(20, 45, 300, 99999999))
        self.label_1.setFont(font)
        self.label_1.setText('\n\n'.join([profile["name"] for profile in self.profiles]))
        self.label_1.setStyleSheet("color: black;")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        y = 37
        for profile in self.profiles:
            self.button = QtWidgets.QPushButton(self.label)
            self.button.setGeometry(QtCore.QRect(300, y, 151, 35))
            self.button.setFont(font)
            self.button.setText("Основное")
            self.button.clicked.connect(lambda state, profile_id=str(profile["id"]): self.settings(profile_id))
            # ----------
            self.button = QtWidgets.QPushButton(self.label)
            self.button.setGeometry(QtCore.QRect(470, y, 151, 35))
            self.button.setFont(font)
            self.button.setText("Транзакции")
            self.button.clicked.connect(lambda state, profile_id=str(profile["id"]): self.transactions(profile_id))
            # ----------
            self.button = QtWidgets.QPushButton(self.label)
            self.button.setGeometry(QtCore.QRect(640, y, 151, 35))
            self.button.setFont(font)
            self.button.setText("Запуск")
            self.button.clicked.connect(lambda state, profile_id=str(profile["id"]): self.start(profile_id))
            y += 48
        self.scrollArea.setWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Список профилей"))

    def settings(self, profile_id: str):
        self.datainput = DataInput(profile_id)
        return self.datainput.show()

    def transactions(self, profile_id: str):
        self.transactionslist = TransactionsList(profile_id)
        return self.transactionslist.show()

    def start(self, profile_id: str):
        worker = multiprocessing.Process(target=Worker, args=(profile_id, self.dolphin))
        worker.start()

class DataInput(QtWidgets.QMainWindow, di.Ui_MainWindow):
    def __init__(self, profile_id: str):
        self.profile_id = profile_id
        super(DataInput, self).__init__()
        self.setupUi(self, profile_id)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(lambda: self.close() if self.to_close else ...)
        self.timer.start(1000)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.timer.stop()

class TransactionsList(QtWidgets.QMainWindow, tl.Ui_MainWindow):
    def __init__(self, profile_id: str):
        self.profile_id = profile_id
        super(TransactionsList, self).__init__()
        self.setupUi(self)