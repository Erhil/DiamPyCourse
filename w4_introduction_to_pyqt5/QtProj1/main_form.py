#!-*-coding:utf-8-*-
import sys

# import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

(Ui_MainWindow, QMainWindow) = uic.loadUiType('main_form.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.lineEdit.grabKeyboard()

    def __del__(self):
        self.ui = None

    def keyPressEvent(self, Event):
        if Event.key() == Qt.Key_Return:
            command = self.ui.lineEdit.text()
            if command != "":
                self.ui.listWidget.addItem(command)
                self.ui.lineEdit.setText("")
            self.ui.listWidget.addItem(QListWidgetItem())

    def eventFilter(self, Object, Event):  # Mouse listener
        try:
            if Event.type() == QEvent.MouseButtonDblClick:
                if self.ui.listWidget.currentItem():
                    self.ui.lineEdit.setText(self.ui.listWidget.currentItem().text())
        except:
            pass
        return QWidget.eventFilter(self, Object, Event)

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('qt_test')

    # create widget
    w = MainWindow()
    w.setWindowTitle('qt_test')
    w.show()

    app.installEventFilter(w)


    # execute application
    sys.exit(app.exec_())