#!-*-coding:utf-8-*-
import sys

# import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np


(Ui_MainWindow, QMainWindow) = uic.loadUiType('GraphForm.ui')


class MainWindow(QMainWindow):
    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.create_surface()

        self.gr = gl.GLViewWidget()
        self.p4 = gl.GLSurfacePlotItem(x=self.x[:, 0], y=self.y[0, :],
                                       shader='normalColor',smooth=False)
        self.gr.addItem(self.p4)

        md = gl.MeshData.sphere(rows=10, cols=20)
        self.sphere = gl.GLMeshItem(meshdata=md, shader="normalColor")
        self.gr.addItem(self.sphere)

        layout = QVBoxLayout()
        layout.addWidget(self.gr)
        self.ui.graph_widget.setLayout(layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)

        self.index = 0

    def create_surface(self):
        self.x = np.linspace(-50, 50, 100).reshape(100, 1)
        self.y = np.linspace(-50, 50, 100).reshape(1, 100)
        self.surface = np.zeros((100, 100))

        points = np.random.randint(0, 100, size=(50, 3))
        zero_points = points[:3, :2]

        for i in points:
            i[2] = min(self.distance(i, zero_points[0]),
                       self.distance(i, zero_points[1]),
                       self.distance(i, zero_points[2]))

        for i in range(100):
            for j in range(100):
                nearest = np.argmin([self.distance([i,j], pt) for pt in points])
                self.surface[i,j] = points[nearest, 2]




    def update(self):
        self.index = (self.index + 1) % 1000
        self.p4.setData(z=(self.surface))

    def __del__(self):
        self.ui = None

    def distance(self, point, other):
        return np.sqrt((point[0] - other[0])*(point[0] - other[0]) +
                        (point[1] - other[1])*(point[1] - other[1]))

#-----------------------------------------------------#
if __name__ == '__main__':
    # create application
    app = QApplication(sys.argv)
    app.setApplicationName('week6')

    # create widget
    w = MainWindow()
    w.setWindowTitle('week6')
    w.show()

    app.installEventFilter(w)

    w.timer.start(30)

    sys.exit(app.exec_())