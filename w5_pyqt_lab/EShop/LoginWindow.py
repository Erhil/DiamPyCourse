#!-*-coding:utf-8-*-
import sys

# import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

(Ui_MainWindow, QMainWindow) = uic.loadUiType('LoginWindow.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Load data from database
        with open("data.txt") as file:
            self.users = {login: password for
                          login, password
                          in map(lambda x: x.strip().split(),
                                    file.readlines()
                                )
                          }

        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.register)

    def login(self):
        if (self.ui.lineEdit.text() == ""
                or self.ui.lineEdit_2.text() == ""):
            self.ui.label_4.setText("Field is empty")
        elif self.ui.lineEdit.text() not in self.users:
            self.ui.label_4.setText("No such user!")
        elif self.ui.lineEdit_2.text() != self.users[self.ui.lineEdit.text()]:
            self.ui.label_4.setText("Wrong password!")
        else:
            self.ui.label_4.setText("OK")

    def register(self):
        if (self.ui.lineEdit.text() == ""
                or self.ui.lineEdit_2.text() == ""):
            self.ui.label_4.setText("Field is empty")
        elif self.ui.lineEdit.text() in self.users:
            self.ui.label_4.setText("Such user exists!")
        else:
            self.users[self.ui.lineEdit.text()] = self.ui.lineEdit_2.text()
            with open("data.txt", "w") as file:
                for user in self.users:
                    file.write(f'{user} {self.users[user]}\n')
            self.ui.label_4.setText("User added")

    def __del__(self):
        self.ui = None


#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('week5')

    # create widget
    w = MainWindow()
    w.setWindowTitle('week5')
    w.show()

    app.installEventFilter(w)

    # execute application
    sys.exit(app.exec_())