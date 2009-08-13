#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
version = "0.7.4_alpha1"

import sys, getpass, os, urllib.request, urllib.error, urllib.parse

try: #Finding kamlib
  import kamlib.weblib
except ImportError:
  print("I cant find kamlib. Kamiltube needs kamlib installed. Exiting.")
  sys.exit(1)  

data = kamlib.weblib #Loading a kamlib object

#Variables
mail = ""
passw = ""
cookie = None
usingcookie = False
download = False
savepath = os.environ['HOME'] + "/.kamiltube/"
debugMode = False
gui = None
guisupport = list()
#End Variables

#Importing GUI
try:
  from PyQt4.QtCore import SIGNAL, SLOT
  from PyQt4.QtGui import QDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
  guisupport.append("PyQt4")
except ImportError:
  pass
try:
  import tkinter as Tk
  import tkinter.messagebox as tkMB
  guisupport.append("Tk")
except ImportError:
  pass
  
#End Importing GUI

def checkparameters(x): #For something
  global gui, debugMode
  #Only for debug
  if x.find("gui") > 0:
    print("Supported GUIs:")
    for x in guisupport:
      print("* " , x)
    sys.exit(True)
  if x.find("d") > 0 and debugMode is not True:
    debugMode = True
    print("Using debug mode")
  if x.find("-help") > 0 or x.find("h") > 0: #Parameters
    sys.argv = ["", x, "help"]
  if x.find("qt4") > 0 and gui != "PyQt4" and guisupport.count("PyQt4") == 1:
    if debugMode == True: #Only for debug
      print("Using PyQt4 version")
    gui = "PyQt4"
  if x.find("tk") > 0 and gui != "Tk" and guisupport.count("Tk") == 1:
    if debugMode == True: #Only for debug
      print("Using Tk version")
    gui = "Tk"
  return True
    
def messages(message,title): #Messages
  if debugMode == True:
    print("Im on messages method")
  global gui
  if gui is "PyQt4":
    QMessageBox.information(None ,title,message)
  elif gui is "Tk":
    tkMB.showinfo(title, message)
  else:
    print("* " , message)
  return True

def additional(link): #Not video links.
  if debugMode == True:
    print("Im on additional method")
  val = link.capitalize()
  if val == "Help" or val == "Info":
    messages("Kamiltube Help\n\n- kamiltube --help, -h or help: This help\n- kamiltube <video1> <video2> <videoN>: Watch video 1, then video 2... n videos\n- kamiltube -qt4/-tk: Use PyQt4 or Tk mode.\n- kamiltube -gui: Supported GUI.\n\n On video parameters:\n- d<video>: Download the video.\n- update: for check some updates.\n","Information\n")
  elif val == "Website":
    messages("The website of this application is www.slash.cl, visit it for check updates or others","Information")
  elif val == "Update":
    webversion = bytes.decode(urllib.request.urlopen("http://www.slash.cl/kamiltube/version").read()).split("\n")
    if webversion[1] > version:
      conclusion = "Exist a update for you, please check www.slash.cl for more info"
    elif webversion[1] == version:
      conclusion = "You are using a stable updated version"
    elif webversion[0] > version:
      conclusion = "You are using a not updated unstable version, please check www.slash.cl for more info"
    elif webversion[0] == version:
      conclusion = "You have the last unstable version."
    else:
      conclusion = "You have an edited version, check www.slash.cl, maybe your version is fake."
    messages("Update\nLast version: " + webversion[0] + "\nLast stable version: " + webversion[1] + "\nYour version: " + version + "\n" + conclusion, "Information")
  else:
    return False
  return True

def watchVideo(flvlink): #Display it
  if debugMode == True:
    print("Im on watchVideo method")
  global download, usingcookie
  #ErrorCheck
  if flvlink.find("http://") == -1:
    messages(flvlink, "Error")
    return False
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
    return False
    
  flvlink = "\"" + flvlink +"\""
  if os.path.exists(mplayeroute) is True:
    if (usingcookie is True):
      if (download is False):
        flvlink = flvlink + " -cookies -cookies-file " + savepath + "cookie"
      else:
        flvlink = flvlink + " --load-cookies=" + savepath + "cookie"
      data.cj.save(savepath + "cookie")
    watchit = mplayeroute + " " + flvlink
    usingcookie = False
  elif os.path.exists(vlcroute) is True:
    watchit = vlcroute + " " + flvlink
  else:
    messages("No mplayer or VLC detected", "Error")
    return False
  if download == True:
    result = os.popen("wget -O " + savepath + "video " + flvlink).read() #Downloading
    print(result)
    download = False
    if result == 1:
      messages("Download Complete", "Information")
    else:
      messages("Download Incomplete, Canceled? No internet?", "Information")
      return False
  else:
    result = os.popen(watchit).read()
    print(result)
  if result.find("Starting playback...") == -1:
    messages("Unknown error with your player", "Error")
    return False
  return True
  
def response(video, typevideo): #Uses a dirty method!!
  if debugMode == True:
    print("Im on response method")
  try: #For URL Errors
    if (typevideo == "youtube"): #Start youtube
      result = data.youtube(video)
    elif (typevideo == "nico"): #Start nicovideo
      global download, usingcookie
      result = data.niconico(video, mail, passw)
      usingcookie = True #That avoids create a new cookie
    elif (typevideo == "godtube"):
      result = data.godtube(video)
    elif (typevideo == "redtube"):
      result = data.redtube(video)
    elif (typevideo == "dailymotion"):
      result = data.dailymotion(video)
    elif (typevideo == "breakdotcom"):
      result = data.breakdotcom(video)
    elif (typevideo == "youporn"):
      result = data.youporn(video)
    elif (typevideo == "blip"):
      result = data.blip(video)
    return watchVideo(result)
  except urllib.error.HTTPError as e: 
    if str(e.errno()) == "404":
      messages("That's a bad URL. I got a 404 Error", "Error")
  except:
    raise

def login(video):
  if debugMode == True:
    print("Im on login method")
  if gui is "PyQt4": #A login with Qt4 GUI
    global mail, passw
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
    
    #Method
    def accept():
      global mail, passw
      mail = login_mail.text()
      passw = login_passw.text()
      if mail != "" and passw != "":
        login.close()
        return work(video)
      
    #Signals
    login.connect(login_Ok, SIGNAL("clicked()"), accept)
    login.connect(login_cancel, SIGNAL("clicked()"), SLOT("close()") )
    
    #Options and execution
    login_passw.setEchoMode(2)
    login.setWindowTitle("NicoLogin")
    login.show()
    login.exec_()
  elif gui is "Tk": #A login with Tk GUI
    #Method
    def accept(*args):
      global mail, passw
      mail = login_mail.get()
      passw = login_passw.get()
      if mail != "" and passw != "":
        login.destroy()
        return work(video)
	
    #Objects
    login = Tk.Toplevel()
    login_mailtext = Tk.Label(login, text="Email:")
    login_passtext = Tk.Label(login, text="Password:")
    login_mail = Tk.Entry(login)
    login_passw = Tk.Entry(login, show="*")
    login_Ok = Tk.Button(login, text="Ok", command=accept)
    login_cancel = Tk.Button(login, text="Cancel", command=login.destroy)
    
    #Connection to grid    
    login_mailtext.grid(row=0)
    login_passtext.grid(row=1)
    login_mail.grid(row=0, column=1)
    login_passw.grid(row=1, column=1)
    login_Ok.grid(row=2)
    login_cancel.grid(row=2, column=1)
    
    #Options and execution
    login_mail.focus()
    login.bind("<Return>", accept)
    login.mainloop()
  else: #A login without GUI
    while mail == "" or passw == "":
      mail = input("\nEmail: ")
      passw = getpass.getpass(prompt="Password: ")
      return work(video)
  return False
    
def work(video): #Im checking if all is right, and preparation for kamlib functions
  global download
  if debugMode == True:
    print("Im on work method")
  #Check if .kamiltube exists, if not, create it
  try:
    import os.path
    if os.path.lexists(savepath) is False:
      os.mkdir(savepath)
  except:
    messages("Kamiltube need write on your $HOME. Check your permissions", "Error")
    return False
  #End of kamiltube exists
  if (video[0] == "d"): #If you want download a video
    download = True
  adcommands = additional(video) #Work with extra info.
  if adcommands is True:
    return True
  global mail, passw
  flvlink = ""
  validyt = video.find("ube.com/watch?v=")
  validyt2 = video.find("ube.com/v/")
  validnico = video.find("o.jp/watch/")
  validredtube = video.find("edtube.com/")
  validgodtube = video.find("odtube.com/view_video.php?")
  validailymotion = video.find("tion.com")
  validyoutube = video.find("video/video.php?")
  validbreakdotcom = video.find("ak.com/")
  validyouporn = video.find("orn.com/watch/")
  validblip = video.find("ip.tv/file/")
  #Start validating...
  if validyt != validyt2: #If is youtube...
    results = response(video, "youtube" ) #youtube(video)
  elif validnico != -1: #If is niconico
    if mail != ""  and passw != "": pass
    else:
      login(video) #Try logging in, can call me again, i need return false for that
      return False
    if (mail is not None) and (passw is not None):
      results = response(video, "nico")
    if results == False: #If nico fails
      data.cj.clear()
      mail = ""
      passw = ""
      return False
  elif validgodtube != -1: #If is godtube
    results = response(video, "godtube")
  elif validredtube != -1: #If is redtube
    results = response(video, "redtube")
  elif validailymotion != -1: #If is dailymotion
    results = response(video, "dailymotion")
  elif validbreakdotcom != -1: #If is breakdotcom
    results = response(video, "breakdotcom")
  elif validyouporn != -1: #If is youporn
    results = response(video, "youporn")
  elif validblip != -1: #If is blip
    results = response(video, "blip")
  else:
    messages("Bad video url", "Error")
    return False
  #End Validating
  return False
  
def guiPyQt4(): 
  app = QApplication(sys.argv)
  widget = QWidget()
  if debugMode == True:
    print("Im using PyQt4 mode")
  
  #Objets
  label = QLabel("Video Address:")
  box = QLineEdit("http://www.youtube.com/watch?v=iW87vxM11tw")
  button = QPushButton("&Watch it!")

  #Layouts
  grid = QGridLayout()
  grid.addWidget(label,0,0)
  grid.addWidget(box,1,0)
  grid.addWidget(button,1,1)
  widget.setLayout(grid)
  
  #Methods
  def gotowork():
    if box.text() != "": work(str(box.text()))
    
  #Signals and others!
  widget.connect(button, SIGNAL("clicked()"), gotowork)
  box.selectAll()
  widget.setWindowTitle("Kamiltube " + version)
  widget.show()
  app.exec_()

def guiTk():
  if debugMode == True:
    print("Im using Tk mode")
    
  #Methods
  def gotowork(*args):
    if box.get() != "":
      video = box.get()
      work(video)
      
  #Objets
  root = Tk.Tk()
  frame = Tk.Frame(root)
  label = Tk.Label(frame, text="Video Address:")
  box = Tk.Entry(frame)
  button = Tk.Button(frame, text="Watch It!", command=gotowork)
  #Layouts
  label.grid(row=0)
  box.grid(row=1)
  button.grid(row=1, column=1)
  #Signals and others!
  root.title("Kamiltube " + version)
  root.minsize(350,50)
  box.insert(0,"http://www.youtube.com/watch?v=iW87vxM11tw")
  box.select_range(0, Tk.END)
  box.focus()
  box.bind("<Return>", gotowork)
  frame.pack()
  root.mainloop()
  
def console(): #Console only.
  if debugMode == True:
    print("Im using console mode")
  while True:
    print("\nWrite exit for quit of the application\n")
    video = input("Video Address: ")
    if video == "exit" or video == "quit" or video == "q":
      break
    elif (len(video) == 0):
      pass
    else:
      try:
        work(video)
      except:
        raise

def bashmode():
  sys.argv.reverse()
  sys.argv.pop()
  sys.argv.reverse()
  if debugMode == True:
    print("Using bashmode")
  for video in sys.argv:
    try:
      work(video)
    except:
      raise

def main(): #Main App
  print("Kamiltube Version: " , version)
  print("Kamlib Version: ", kamlib.__version__, "\n")

  tempArgv = list(sys.argv)  #Check the parameters
  for x in tempArgv:
    if x.find("-") == 0:
      checkparameters(x.capitalize())
      sys.argv.remove(x)

  if len(sys.argv) > 1:
    bashmode()
  elif gui is "PyQt4": #Run PyQt4
    guiPyQt4()
  elif gui is "Tk":
    guiTk()
  else:
    console()

try:
  main()
except KeyboardInterrupt:
  pass
except EOFError:
  pass
  
print("\nThanks for use Kamiltube")
