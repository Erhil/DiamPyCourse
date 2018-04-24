import pyqtgraph as pg
from pyqtgraph.Qt import QtCore
import numpy as np

app = pg.mkQApp()
plt = pg.PlotWidget()
plt.show()
t = np.linspace(0, 2*np.pi, 1000)
i = 0

def update():
    global i
    plt.clear()
    i += 0.1
    x = np.sin(3 * t + 1 + i / 10)
    y = np.cos(5 * t)
    plt.addItem(pg.PlotCurveItem(x, y))

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(10)

if __name__ == '__main__':
    app.exec_()
