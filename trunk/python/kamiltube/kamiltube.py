#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import sys, getpass, os
from kamlib import *
version = "0.7.3alpha"
gui = 1
mail = None
passw = None
cookie = None
video = ""
qual = 1

def watchVideo(flvlink):
  #ErrorCheck
  if flvlink == "No internet":
    print "* You arent on internet."
    return "No Internet"
  if flvlink == "badlogin":
    cookie = None
    print "* You got a bad login, try again!"
    return "badlogin"
  if flvlink == "disabled":
    print "* This kind of video is on development..."
    return "disabled"
  if flvlink == "Invalid link":
    print "* This video is no more on the web."
    return 0
  if flvlink == "Is a video for 18+":
    print "* This video is for 18+, i will do a solution for that..."
    return 0
  #End ErrorCheck
  opsys = sys.platform
  if opsys.find("darwin") is not -1:
    mplayeroute = "/Applications/mplayer/mplayer" #Dirty, not really implemented.
    vlcroute = "/Applications/VLC.app/Contents/MacOS"
  elif opsys.find("linux") is not -1:
    mplayeroute = "/usr/bin/mplayer"
    vlcroute = "/usr/bin/vlc"
  else:
    print "OS not Supported!"
    return 0
  if os.path.exists(mplayeroute) is True:
    watchit = mplayeroute + " " + flvlink
  elif os.path.exists(vlcroute) is True:
    watchit = vlcroute + " " + flvlink
  else:
    print "I cant find mplayer or vlc installed =("
    return 0
  print watchit
  #I need open a thread here!
  #I need open a list[], for n videos in a list!, a really good feature for next release!
  result = os.system(watchit)
  if result is not 0:
    print "Unknown error!!! Report it please!"
    return 0
  if gui is 1:
    box.setEnabled(1)
    button.setEnabled(1)
  print ""  #Nice visual2
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

def youtubequality():
  try:
    print "Here you can see youtube quality"
  except:
    print "Press 1 for high quality"
    print "Press 2 for low quality"
    return raw_input("Option: ")
  return 1
  
def login():
  try:
    global mail,passw
    #Objects
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
    mail = raw_input("Email: ")
    passw = getpass.getpass(prompt="Password: ")
    
def work(): #Debug only
  global video
  if gui is 1:
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
    if (mail is not None) and (passw is not None):
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
  
  mainapp = QWidget()
  #Objets
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
  print "Kamiltube Version " + version
  print ""
  print "Write exit for quit of the application"
  print ""
  gui = 0
  while True:
    video = raw_input("Video Address: ")
    print "" #Is nicer...
    if video == "exit":
      break
    elif video == "help":
      print "Press \"exit\" for exit of Kamiltube"
    else:
      k = work()
print "Thanks for use Kamiltube"
