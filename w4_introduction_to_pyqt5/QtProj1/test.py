#!-*-coding:utf-8-*-
import sys

# import PyQt4
from PyQt5.QtWidgets import *
from PyQt5 import uic

import pickle

(Ui_MainWindow, QMainWindow) = uic.loadUiType('test_form.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        with open("logins.dat", "rb") as f:
            self.users = pickle.load(f)

        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.__button_pressed)

    def __button_pressed(self):
        login = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        if not (login and passwd):
            self.ui.label_2.setText("Логин и пароль не могут быть пустыми!")
        elif (login in self.users) and self.users[login][0] == passwd:
            args["data"] =  self.users[login][1]
            self.ui.label_2.setText("Вход успешно выполнен")
            self.close()
        else:
            self.ui.label_2.setText("Введен неверный логин или пароль!")


    def __del__(self):
        self.ui = None
        return 42



#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    args = dict()
    app = QApplication(sys.argv)
    app.setApplicationName('qt_test')

    # create widget
    w = MainWindow()
    w.setWindowTitle('qt_test')
    w.show()

    app.installEventFilter(w)

    app.exec_()

    if "data" in args:
        print(args["data"])