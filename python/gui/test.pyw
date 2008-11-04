#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Form(QWidget):
  def __init__(self, parent=None):
    super(Form, self).__init__(parent)
    self.lineedit = QLineEdit("Esto es una prueba")
    self.lineedit.selectAll()
    layout = QVBoxLayout()
    layout.addWidget(self.lineedit)
    self.setLayout(layout)
    self.lineedit.setFocus()
    #self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
    self.setWindowTitle("Test")
  
  #def updateUi(self):
    #try:
    
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
     
