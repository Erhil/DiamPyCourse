#!-*-coding:utf-8-*-
import sys
 
# import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic
 
( Ui_MainWindow, QMainWindow ) = uic.loadUiType( '${Form_file}.ui' )
 
class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""
 
    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
 
    def __del__ ( self ):
        self.ui = None
 
#-----------------------------------------------------#
if __name__ == '__main__':
 
    # create application
    app = QApplication( sys.argv )
    app.setApplicationName( '${PROJECT_NAME}' )
 
    # create widget
    w = MainWindow()
    w.setWindowTitle( '${PROJECT_NAME}' )
    w.show()
    
    app.installEventFilter(w)
 
    # execute application
    sys.exit( app.exec_() )
