#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import sys, getpass
from kamlib import *
from os import system
version = "0.7"
gui = 1
mail = None
passw = None
cookie = None

def login(self):
  global mail, passw
  try:
    mail, mailok = QInputDialog.getText(self, "QInputDialog.getText()", "Email:", QLineEdit.Normal)
    if mailok:
      passw, passok = QInputDialog.getText(self, "QInputDialog.getText()", "Password:", QLineEdit.Password)
    if not mailok or not passok:
      return None, None
  except:
    mail = raw_input("Email: ")
    passw = getpass.getpass(prompt="Password: ")
  if mail == "" or passw == "":
    return None, None
  return mail, passw

def work(self,video): #Debug only
  global cookie
  flvlink = ""
  validyt = video.find("ube.com/watch?v=")
  validnico = video.find("o.jp/watch/")
  validredtube = video.find("edtube.com/")
  if validyt != -1: #If is youtube...
    flvlink = youtube(video, validyt)
  elif validnico != -1: #If is niconico
    if cookie is None:
      login(self)
    flvlink, cookie = niconico(video, validnico, mail, passw, cookie)
  else:
    print "Bad video url"
    return "fail"
      
  if flvlink == "badlogin":
    cookie = None
    return "badlogin"
  if flvlink == "disabled":
    return "disabled"
  mplayercommand = "/usr/bin/env mplayer " + flvlink
  print mplayercommand
  system(mplayercommand)
  return 1
  
try:
  from PyQt4.QtCore import *
  from PyQt4.QtGui import *
  print "Nice, i can use PyQt4 =D"
  class Form(QDialog):
  
    def __init__(self, parent=None):
      super(Form, self).__init__(parent)
      #QDialog.__init__(self, parent)
      #Objetos
      label = QLabel("Video Address:")
      self.box = QLineEdit("http://www.youtube.com/watch?v=iW87vxM11tw")
      self.button = QPushButton("&Watch it!",self)
      
      #Opciones
      self.box.selectAll()
      self.setWindowTitle("Kamiltube " + version)
      #Layouts
      grid = QGridLayout()
      grid.addWidget(label,0,0)
      grid.addWidget(self.box,1,0)
      grid.addWidget(self.button,1,1)
      self.setLayout(grid)
     
      #Acciones
      self.connect(self.button, SIGNAL("clicked()"), self.response)     
    
    def response(self):
      self.box.selectAll()
      self.box.setEnabled(0)
      self.button.setEnabled(0)
      try:
	k = work(self,str(self.box.text()))
	if k == "fail":
		QMessageBox.critical(self, "Error", "Ha habido un error en la url.\nModo de uso: http;//www.youtube.com/watch?v=a3f4faa3", QMessageBox.Ok)
	#Sigo necesitando un ícono
	if k == "disabled":
	      QMessageBox.information(self, "Informacion", "Funcion aun no implementada\nPor favor, espere a una nueva version.", QMessageBox.Ok)
	if k == "badlogin":
	  QMessageBox.warning(self, "Advertencia", "Email o clave erronea o nula\nIntenta nuevamente", QMessageBox.Ok)
      except urllib2.URLError:
	QMessageBox.critical(self, "Error", "Not connected to internet", QMessageBox.Ok)
      self.box.setEnabled(1)
      self.button.setEnabled(1)
except:
  gui = 0
  print "Kamiltube Version " + version
  while 1:
    ask = raw_input("Video Address: ")
    if ask == "exit":
      break
    k = work(None, ask)
    if k == "badlogin":
      print "* Invalid mail or password *"
    if k == "disabled":
      print "* This function was disabled for now *"
    print "Write exit for quit of the application"
  print "Thanks for use Kamiltube"
if gui == 1:
  app = QApplication(sys.argv)
  form = Form()
  form.show()
  app.exec_()
