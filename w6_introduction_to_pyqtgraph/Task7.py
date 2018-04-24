from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.show()

md = gl.MeshData.sphere(rows=10, cols=20)
sphere = gl.GLMeshItem(meshdata=md, shader="normalColor")
w.addItem(sphere)

index = 0
def update():
    global index
    index -= .1
    sphere.translate(np.sin(index),
                     np.cos(index),
                     np.sin(index))


timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(30)

if __name__ == '__main__':
    app.exec_()