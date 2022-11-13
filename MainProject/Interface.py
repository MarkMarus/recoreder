import sys
import configparser
import multiprocessing
from PyQt5 import QtWidgets

import UI.login_menu as lm
import UI.profile_list as pl
from DolphinAPI import DolphinAPI

class LoginMenu(QtWidgets.QMainWindow, lm.Ui_MainWindow):
    def __init__(self):
        super(LoginMenu, self).__init__()
        self.setupUi(self)
        self.setFixedSize(300, 232)
        self.pushButton.clicked.connect(self.auth)

    def auth(self):
        self.config = configparser.ConfigParser()
        self.dolphin = DolphinAPI(self.config)
        if len(self.lineEdit.text()) == 0 and len(self.lineEdit_2.text()) == 0:
            resp = self.dolphin.auth()
        else:
            resp = self.dolphin.auth(self.lineEdit.text(), self.lineEdit_2.text())

        if not resp:
            return self.label.setStyleSheet("background-color: white;"
                                                 "color: grey;")
        self.dolphin = DolphinAPI(self.config)
        log.close()
        self.plist = ProfileList(self.dolphin)
        return self.plist.show()

class ProfileList(QtWidgets.QMainWindow, pl.Ui_MainWindow):
    def __init__(self, dolphin):
        super(ProfileList, self).__init__()
        self.setupUi(self, dolphin)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    log = LoginMenu()
    log.show()
    sys.exit(app.exec_())