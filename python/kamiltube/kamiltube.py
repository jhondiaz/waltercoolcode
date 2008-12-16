#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import sys, getpass, os, urllib2
from kamlib import *
version = "0.7.3beta1"
gui = False
mail = None
passw = None
cookie = None
usingcookie = False
video = ""
download = False

def messages(message,title):
  global gui
  if gui is True:
    QMessageBox.information(None ,title,message)
  else:
    print "* " + message
  return True

def additional(link):
  val = link.capitalize()
  if val == "Help" or val == "Info":
    messages("Use a \"d\" on the start of the video link for download the video, will saved on ~/kamiltube .\nUse in the end of youtube video &fmt=18 for best quality.\nUse update for check updates.","Information")
  elif val == "Website":
    messages("The website of this application is www.slash.cl, visit it for check updates or others","Information")
  elif val == "Update":
    webversion = (urllib2.urlopen("http://www.slash.cl/kamiltube/version").read()).split("\n")
    if webversion[1] > version:
      conclusion = "Exist a update for you, please check www.slash.cl for more info"
    elif webversion[1] == version:
      conclusion = "You are using a stable updated version"
    elif webversion[0] > version:
      conclusion = "You are using a not updated unstable version, please check www.slash.cl for more info"
    elif webversion[0] == version:
      conclusion = "You have the last unstable version."
    else:
      conclusion = "You have an edited version, check www.slash.cl, maybe your version is fake"
    messages("Last version: " + webversion[0] + "\nLast stable version: " + webversion[1] + "\nYour version: " + version + "\n" + conclusion, "Information")
  return True

def watchVideo(flvlink):
  global download, usingcookie
  #ErrorCheck
  if flvlink.find("http://") == -1:
    messages(flvlink, "Error")
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
    messages("OS not Supported!","Error")
    return 0
    
  flvlink = "\"" + flvlink +"\""
  if os.path.exists(mplayeroute) is True:
    if (usingcookie is True) and (download is False):
      flvlink = flvlink + " -cookies -cookies-file ~/.kamiltube/cookies"
    if (usingcookie is True) and (download is True):
      flvlink = flvlink + " --load-cookies=" + os.environ['HOME'] + "/.kamiltube/cookies"
    watchit = mplayeroute + " " + flvlink
  elif os.path.exists(vlcroute) is True:
    watchit = vlcroute + " " + flvlink
  else:
    messages("No mplayer or VLC detected", "Error")
    return 0
  #I need open a thread here!
  #I need open a list[], for n videos in a list!, a really good feature for next release!
  if download == True:
    print flvlink
    result = os.system("wget -O ~/.kamiltube/video " + flvlink)
    download = False
    if result is True:
      messages("Download Complete", "Information")
    else:
      messages("Download Incomplete, Canceled? No internet?", "Information")
      return False
  else:
    result = os.system(watchit)
  if result is not 0:
    messages("Unknown error with your player", "Error")
    return 0
  if gui is True:
    box.setEnabled(1)
    button.setEnabled(1)
  print ""  #Nice visual2
  return 1
  
def response(video, valid, typevideo):
  try:
    if (typevideo == "youtube"): #Start youtube
      result = youtube(video, valid)
    elif (typevideo == "nico"): #Start nicovideo
      global cookie, download, usingcookie
      result,cookie = niconico(video, valid, mail, passw, cookie)
      usingcookie = True
    elif (typevideo == "godtube"):
      result = godtube(video, valid)
    elif (typevideo == "redtube"):
      result = redtube(video, valid)
    elif (typevideo == "dailymotion"):
      result = dailymotion(video, valid)
    elif (typevideo == "facebook"):
      result = facebook(video, valid)
    else:
      result = "Nothing"
      print "Is not working..."
  except urllib2.URLError:
    messages("You are not connected to internet", "Error")
    return False
  except:
    messages("Report this error please", "Error")
    raise
  watchVideo(result)
  
def login():
  if gui is True: #A login with GUI
    global mail
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
      global mail,passw
      mail = login_mail.text()
      passw = login_passw.text()
      login.done(1)
      
    #Signals
    login.connect(login_Ok, SIGNAL("clicked()"), accept)
    login.connect(login_cancel, SIGNAL("clicked()"), SLOT("close()") )
    
    #Options and execution
    login_passw.setEchoMode(2)
    login.setWindowTitle("NicoLogin")
    login.show()
    login.exec_()
    
  else: #A login without GUI
    mail = raw_input("Email: ")
    passw = getpass.getpass(prompt="Password: ")
    
def work(): #Im checking if all is right, and preparation for kamlib functions
  global video, download
  #Check if .kamiltube exists, if not, create it
  try:
    import os.path
    if os.path.lexists(os.environ['HOME'] + "/.kamiltube") is False:
      os.mkdir(os.environ['HOME'] + "/.kamiltube")
  except:
    messages("Kamiltube need write on your $HOME. Check your permissions", "Error")
    return False
  #End of kamiltube exists
  
  if gui is True:
    video = str(box.text())
  if (video[0] == "d"): #If you want download a video
    download = True
  adcommands = additional(video) #Work with extra info.
  if adcommands is True:
    return True
  global cookie, mail, passw
  flvlink = ""
  validyt = video.find("ube.com/watch?v=")
  validnico = video.find("o.jp/watch/")
  validredtube = video.find("edtube.com/")
  validgodtube = video.find("odtube.com/view_video.php?")
  validailymotion = video.find("tion.com")
  validyoutube = video.find("video/video.php?")
  #Start validating...
  if validyt != -1: #If is youtube...
    results = response(video, validyt, "youtube" ) #youtube(video, validyt, qual)
  elif validnico != -1: #If is niconico
    if cookie is None:
      login()
    if (mail is not None) and (passw is not None):
      results = response(video, validnico, "nico")
    else: #If mail and passw are None
      	messages("Invalid Username or Password", "Error")
	cookie = None
	return False
  elif validgodtube != -1: #If is godtube
    results = response(video, validgodtube, "godtube")
  elif validredtube != -1: #If is redtube
    results = response(video, validredtube, "redtube")
  elif validailymotion != -1: #If is dailymotion
    results = response(video, validailymotion, "dailymotion")
  elif validyoutube != -1: #If is Youtube
    results = response(video, validyoutube, "facebook")
  else:
    messages("Bad video url", "Error")
    return False
  #End Validating
  return results
  
try: #GUI
  from PyQt4.QtCore import *
  from PyQt4.QtGui import *
  app = QApplication(sys.argv)
  print "Nice, i can use PyQt4 =D"
  
  mainapp = QWidget()
  #Objets
  gui = True
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
except ImportError: #Console only.
  print "Kamiltube Version " + version
  print ""
  print "Write exit for quit of the application"
  print ""
  while True:
    video = raw_input("Video Address: ")
    print "" #Is nicer...
    if (video == "exit" or video == "quit" or video == "q"):
      break
    else:
      k = work()
print "Thanks for use Kamiltube"
