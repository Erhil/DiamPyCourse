from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()

x = np.linspace(-8, 8, 100)
y = np.linspace(-8, 8, 100)
z = 0.1 * ((x.reshape(100, 1) ** 2) - (y.reshape(1, 100) ** 2))

p2 = gl.GLSurfacePlotItem(x=x, y=y, z=z, shader='normalColor')
w.addItem(p2)

if __name__ == '__main__':
    app.exec_()