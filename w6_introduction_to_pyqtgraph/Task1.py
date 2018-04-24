import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

plt = pg.plot()
plt.addLegend()

c1 = plt.plot([1,3,2,4], pen='r', symbol='o',
              symbolPen='b', symbolBrush=0.5,
              name='red plot')
c2 = plt.plot([2,1,4,3], pen='g', fillLevel=3,
              fillBrush=(255,0,0,30),
              name='green plot')

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()