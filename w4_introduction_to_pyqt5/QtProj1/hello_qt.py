from PyQt5.QtWidgets import QWidget, QApplication

from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox

from PyQt5.QtWidgets import QGridLayout, QVBoxLayout

class HelloQt(QWidget):
    def __init__(self):
        super().__init__()

        # lab1 = QLabel("Hello QT!", self)
        # lab1.move(120, 50)
        #
        # self.cbx1 = QCheckBox("Quit?", self)
        # self.cbx1.move(120, 80)
        #
        # self.btn1 = QPushButton("Quit!", self)
        # self.btn1.move(120, 120)
        #
        # self.btn1.clicked.connect(self.quit)
        #
        # self.btn1.setEnabled(False)
        #
        # self.cbx1.stateChanged.connect(self.enable_button)

        self.setGeometry(
            100, 200, # Сдвиг
            300, 300  # Размер
        )
        self.setWindowTitle('Hello world') # Заголовок
        self.show()

    # def quit(self):
    #     # if self.cbx1.isChecked():
    #         QApplication.instance().quit()
    #
    # def enable_button(self):
    #     self.btn1.setEnabled(not self.btn1.isEnabled())

class HelloQtLayout(QWidget):

    def __init__(self):
        super().__init__()

        lab1 = QLabel("Hello QT!")

        self.btn1 = QPushButton("Quit!")
        self.btn1.clicked.connect(self.quit)
        self.btn1.setEnabled(False)

        self.cbx1 = QCheckBox("Quit?")
        self.cbx1.stateChanged.connect(self.enable_button)

        self.window_layout = QVBoxLayout()

        self.window_layout.addWidget(lab1)
        self.window_layout.addWidget(self.cbx1)
        self.window_layout.addWidget(self.btn1)

        self.setLayout(self.window_layout)

        self.setGeometry(
            100, 200, # Сдвиг
            300, 300  # Размер
        )
        self.setWindowTitle('Hello world') # Заголовок
        self.show()

    def quit(self):
        QApplication.instance().quit()

    def enable_button(self):
        self.btn1.setEnabled(not self.btn1.isEnabled())


if __name__ == "__main__":
    app = QApplication([])
    window = HelloQtLayout()
    app.exec()