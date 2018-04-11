from PyQt5.QtWidgets import QWidget, QApplication

from PyQt5.QtWidgets import QLabel, QPushButton, QCheckBox

from PyQt5.QtWidgets import QVBoxLayout

class HelloQt(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Hello World!")
        self.checkbox = QCheckBox("Quit?")
        self.checkbox.stateChanged.connect(self.change_state)

        self.button = QPushButton("Quit!")
        self.button.setEnabled(self.checkbox.isChecked())
        self.button.clicked.connect(self.quit)

        lauout = QVBoxLayout()

        lauout.addWidget(self.label)
        lauout.addWidget(self.checkbox)
        lauout.addWidget(self.button)

        self.setLayout(lauout)

        self.setWindowTitle("Hello Qt!")
        self.setGeometry(
            200, 400,
            300, 400
        )
        self.show()

    def change_state(self):
        self.button.setEnabled(self.checkbox.isChecked())

    def quit(self):
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication([])
    window = HelloQt()
    app.exec()