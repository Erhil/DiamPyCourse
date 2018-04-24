import pyqtgraph as pg
import numpy as np

t = np.linspace(0, 2*np.pi, 100000)
x = np.sin(3*t + 1)
y = np.cos(5*t)

plt = pg.plot(x,y)

if __name__ == '__main__':
    pg.QtGui.QApplication.exec_()