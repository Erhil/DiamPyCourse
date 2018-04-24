from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()

x = np.linspace(-8, 8, 100).reshape(100, 1)
y = np.linspace(-8, 8, 100).reshape(1, 100)
d = (x ** 2 + y ** 2)
d2 = d/5

p4 = gl.GLSurfacePlotItem(x=x[:, 0], y=y[0, :],
                          shader='heightColor',
                          smooth=False)
w.addItem(p4)

index = 0
def update():
    global index
    index -= .1
    p4.setData(z=np.sin(d2+index))

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

if __name__ == '__main__':
    app.exec_()