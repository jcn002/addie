from PyQt4 import QtGui

from addie.ui_advanced_window import Ui_MainWindow as UiMainWindow


class AdvancedWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        self.parent = parent
        
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Advanced Window for Super User Only !")
        
    def post_processing_clicked(self):
        pass
        #if self.ui.idl_post_processing_button.isClicked():
        #    self.parent.