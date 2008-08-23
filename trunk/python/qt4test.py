#!/usr/bin/python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        QMessageBox.warning(self, "Hola",  "Este es un mensaje")
    
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
