from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
w.setWindowTitle('pyqtgraph example: GLScatterPlotItem')

g = gl.GLGridItem()
w.addItem(g)


pos = np.random.random(size=(200000, 3))*2-1
pos *= [10, -10, 10]
pos[0] = (0, 0, 0)
color = np.ones((pos.shape[0], 4))
d2 = (pos ** 2).sum(axis=1) ** 0.5
size = np.random.random(size=pos.shape[0]) * 10
sp2 = gl.GLScatterPlotItem(pos=pos, color=(1, 1, 1, 1), size=size)
phase = 0.

w.addItem(sp2)

def update():
    global phase, sp2, d2
    s = -np.cos(d2 + phase)
    color = np.empty((len(d2), 4), dtype=np.float32)
    color[:, 3] = np.clip(s * 0.1, 0, 1)
    color[:, 0] = np.clip(s * 3.0, 0, 1)
    color[:, 1] = np.clip(s * 1.0, 0, 1)
    color[:, 2] = np.clip(s ** 3, 0, 1)
    sp2.setData(color=color)
    phase -= 0.1

t = QtCore.QTimer()
t.timeout.connect(update)
t.start(10)

if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()