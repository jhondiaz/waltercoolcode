#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

from PyQt4.QtGui import *
import sys
class Form(QWidget):
  def __init__(self,parent=None):
    super(Form,self).__init__(parent)
    
    gbox = QGroupBox()
    gbox2 =
    QGroupBox()
    boton = QRadioButton("Hola")
    boton2 = QRadioButton("Chao")
    boton3 = QRadioButton(":D")
    boton4 = QRadioButton("Hola!")
    hola = QLabel("Hola, soy una prueba")
    
    hbox = QHBoxLayout()
    buttonlay = QVBoxLayout()
    buttonlay2 = QVBoxLayout()
    textlay = QVBoxLayout()
    buttonlay.addWidget(boton)
    buttonlay.addWidget(boton2)
    buttonlay2.addWidget(boton3)
    buttonlay2.addWidget(boton4)
    textlay.addWidget(hola)
    
    hbox.addLayout(buttonlay)
    hbox.addLayout(buttonlay2)
    hbox.addLayout(textlay)
    gbox.setLayout(buttonlay)
    gbox2.setLayout(buttonlay2)
    self.setLayout(hbox)
    
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
