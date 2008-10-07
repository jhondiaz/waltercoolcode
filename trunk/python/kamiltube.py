#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import urllib2
import sys
from os import system

gui = 0

def work(video): #Debug only
    valid = video.find("watch?v=") 
    if valid == -1:
      print "Bad video url"
      return 0
    video = "http://www.youtube.com/" + video[valid:]
    resp = urllib2.urlopen(video).read()
    cut1 = resp[resp.find("video_id="):]
    video_id = cut1[:cut1.find("&")]
    #print "Video ID= " + video_id
    cut2 = cut1[cut1.find("&t=")+1:]
    video_t = cut2[:cut2.find("&")]
    #print "Video T= " + video_t
    mplayercommand = "/usr/bin/env mplayer \"http://www.youtube.com/get_video?" + video_id + "&" + video_t + "\""
    #print mplayercommand
    system(mplayercommand)
    return 1    
try:
  from PyQt4.QtCore import *
  from PyQt4.QtGui import *
  print "Nice, i can use PyQt4 =D"
  gui = 1
  class Form(QWidget):
  
    def __init__(self, parent=None):
      super(Form, self).__init__(parent)
    
      #Objetos
      label = QLabel("Video Address:")
      self.box = QLineEdit("http://www.youtube.com/watch?v=iW87vxM11tw", self)
      self.button = QPushButton("&Watch it!",self)
      
      #Opciones
      self.box.selectAll()
      self.setWindowTitle("Kamiltube")
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
	k = work(str(self.box.text()))
	if k == 0:
		QMessageBox.critical(self, "Error", "Ha habido un error en la url.\nModo de uso: http;//www.youtube.com/watch?v=a3f4faa3", QMessageBox.Ok)
	#Sigo necesitando un ícono
      except urllib2.URLError:
	QMessageBox.critical(self, "Error", "Not connected to internet", QMessageBox.Ok)
      self.box.setEnabled(1)
      self.button.setEnabled(1)

except ImportError:
  print "Console only support"
  video = raw_input("Write the youtube link here: ")
  work(video)
except:
  print "Strange error, please, report it with that info:"
  sys.exc_info()
  raise
  sys.exit(0)

if gui == 1:
  app = QApplication(sys.argv)
  form = Form()
  form.show()
  app.exec_()
