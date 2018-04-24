#!-*-coding:utf-8-*-
import sys

# import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

(Ui_MainWindow, QMainWindow) = uic.loadUiType('EShopWindow.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Добавить колонку
        self.ui.tableWidget.insertColumn(1)
        self.ui.tableWidget.setHorizontalHeaderLabels(["s1", 's2', 's3']) # Изменение названий столбцов

        # Добавить строку с данными
        self.ui.tableWidget.insertRow(0) # Добавление пустой строки в начало таблицы
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("text1")) # Заполнение ячеек
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("text2"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("text3"))

        self.ui.tableWidget.insertRow(0)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem("text4"))
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem("text5"))
        self.ui.tableWidget.setItem(0, 2, QTableWidgetItem("text6"))

        self.ui.tableWidget.cellClicked.connect(self.printer)

    def printer(self, x, y):
        print(x,y)

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