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
version = "0.7.3alpha"
gui = 1
mail = None
passw = None
cookie = None
qual = 1

def watchVideo(flvlink):
  if flvlink == "badlogin":
    cookie = None
    return "badlogin"
  if flvlink == "disabled":
    return "disabled"
  mplayercommand = "/usr/bin/env mplayer " + flvlink
  print mplayercommand
  #I need open a thread here!
  #I need open a list[], for n videos in a list!, a really good feature for next release!
  system(mplayercommand)
  box.setEnabled(1)
  button.setEnabled(1)
  return 1
  
def response(video, valid, typevideo):
  if (typevideo == "youtube"):
    result = youtube(video, valid, qual)
  elif (typevideo == "nico"):
    global cookie
    result,cookie = niconico(video, valid, mail, passw, cj)
  else:
    result = "Nada"
    print "Is not working..."
  watchVideo(result)
      
  try:
    print "hola"
  except urllib2.URLError:
    QMessageBox.critical("Error", "Not connected to internet", QMessageBox.Ok)

def youtubequality():
  try:
    print "Here you can see youtube quality"
  except:
    raise
    print "Press 1 for high quality"
    print "Press 2 for low quality"
    return raw_input("Option: ")
  return 1
  
def login():
  try:
    #Objects
    global mail
    login = QDialog()
    login_mailtext = QLabel("Email:")
    login_mail = QLineEdit(mail)
    login_passtext = QLabel("Password:")
    login_passw = QLineEdit()
    login_passw.EchoMode = 2
    login_Ok = QPushButton("Ok")
    login_cancel = QPushButton("Cancel")
    login_grid = QGridLayout()
    
    #Connection to grid
    login_grid.addWidget(login_mailtext,0,0)
    login_grid.addWidget(login_mail,0,1)
    login_grid.addWidget(login_passtext,1,0)
    login_grid.addWidget(login_passw,1,1)
    login_grid.addWidget(login_Ok,2,0)
    login_grid.addWidget(login_cancel,2,1)
    login.setLayout(login_grid)
    
    def accept():
      global mail,passw
      mail = login_mail.text()
      passw = login_passw.text()
      login.close()
      
    
    #Signals
    login.connect(login_Ok, SIGNAL("clicked()"), accept)
    login.connect(login_cancel, SIGNAL("clicked()"), SLOT("close()") )
    
    #Options and execution
    login.setWindowTitle("NicoLogin")
    login.show()
    login.exec_()
    
  except:
    raise
    mail = raw_input("Email: ")
    passw = getpass.getpass(prompt="Password: ")
    
def work(): #Debug only
  video = str(box.text())
  global cookie, mail, passw
  flvlink = ""
  validyt = video.find("ube.com/watch?v=")
  validnico = video.find("o.jp/watch/")
  validredtube = video.find("edtube.com/")
  if validyt != -1: #If is youtube...
    qual = youtubequality() #Empty
    response(video, validyt, "youtube" ) #youtube(video, validyt, qual)
    
  elif validnico != -1: #If is niconico
    if cookie is None:
      login()
      print mail
      print passw
    if (mail is not None) and (passw is not None):
      #flvlink, cookie = niconico(video, validnico, mail, passw, cookie)
      response(video, validnico, "nico")
    else:
      	flvlink = "badlogin"
	cookie = None

  else:
    print "Bad video url"
    return "fail"
  
  return 1
  
try: #GUI
  from PyQt4.QtCore import *
  from PyQt4.QtGui import *
  app = QApplication(sys.argv)
  print "Nice, i can use PyQt4 =D"
  
  
  def boton(event):
    print "hola"
  #Objets
  mainapp = QWidget()
  label = QLabel("Video Address:")
  box = QLineEdit("http://www.youtube.com/watch?v=iW87vxM11tw")
  button = QPushButton("&Watch it!")

  #Layouts
  grid = QGridLayout()
  grid.addWidget(label,0,0)
  grid.addWidget(box,1,0)
  grid.addWidget(button,1,1)
  mainapp.setLayout(grid)
     
  #Options and execute it!
  mainapp.connect(button, SIGNAL("clicked()"), work)
  box.selectAll()
  mainapp.setWindowTitle("Kamiltube " + version)
  mainapp.show()
  
  sys.exit(app.exec_())
except: #Console only.
  raise
  print "Kamiltube Version " + version
  while 1:
    ask = raw_input("Video Address: ")
    if ask == "exit":
      break
    k = work(ask)
    if k == "badlogin":
      print "* Invalid mail or password *"
    if k == "disabled":
      print "* This function was disabled for now *"
    print "Write exit for quit of the application"
  print "Thanks for use Kamiltube"