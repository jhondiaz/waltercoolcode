#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
version = "0.7.4_beta"

import sys, getpass, os, urllib2

try: #Finding kamlib
  import kamlib.weblib
  import core
except ImportError:
  print("Data missing!")
  sys.exit(1)

videolib = kamlib.weblib.video() #Loading a kamlib object
core = core.detect()

#Variables
mail = ""
passw = ""
cookie = None
usingcookie = False
download = False
savepath = os.environ['HOME'] + "/.kamiltube/"
debugMode = False
guiparent = None
playersupport = list()
defgui = ""
#End Variables

deftit = "Kamiltube " + version
defvid = "http://www.youtube.com/watch?v=iW87vxM11tw"
deflabel = "Video Address:"

def checkparameters(x): #For something
    global debugMode, defgui
    #Only for debug
    if x.find("-gui") >= 0:
      print("Supported GUIs:")
      for x in core.gui:
        print("* " + x)
      sys.exit(True)
    if x.find("D") >= 0 and debugMode is not True:
      debugMode = True
      print("Using debug mode")
    #if x.find("-help") == 0 or x.find("h") >= 0: #Parameters
      #sys.argv["help"]
    if x.find("-qt4") == 0 and defgui != "PyQt4" and core.gui.count("Qt4") == 1:
      if debugMode == True: #Only for debug
        print("Using PyQt4 version")
      defgui = "PyQt4"
    elif x.find("-tk") == 0 and defgui != "Tk" and core.gui.count("Tk") == 1:
      if debugMode == True: #Only for debug
        print("Using Tk version")
      defgui = "Tk"
    elif x.find("-gtk") == 0 and defgui != "Gtk" and core.gui.count("Gtk") == 1:
      if debugMode == True: #Only for debug
        print("Using Gtk version")
      defgui = "Gtk"
    return True

    
def messages(message,title): #Messages
  if defgui is "PyQt4":
    QMessageBox.information(None ,title,message)
  elif defgui is "Tk":
    tkMB.showinfo(title, message)
  elif defgui is "Gtk":
    d = gtk.MessageDialog(parent=guiparent,buttons=gtk.BUTTONS_CLOSE, message_format=message)
    d.run()
    d.destroy()
  else:
    print("* " + message)
  return True
  
def additional(link): #Not video links.
  if debugMode == True:
    print("Im on additional method")
  val = link.capitalize()
  if val == "Help" or val == "Info":
    messages("Kamiltube Help\n\n- kamiltube --help, -h or help: This help\n- kamiltube <video1> <video2> <videoN>: Watch video 1, then video 2... n videos\n- kamiltube --qt4/--gtk/--tk: Use PyQt4, PyGTK or Tk mode.\n- kamiltube --gui: Supported GUI.\n\n On video parameters:\n- d<video>: Download the video.\n- update: for check some updates.\n","Information\n")
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
  if core.player.count('mplayer') == 1:
    if (usingcookie is True):
      if (download is False):
        flvlink = flvlink + " -cookies -cookies-file " + savepath + "cookie"
      else:
        flvlink = flvlink + " --load-cookies=" + savepath + "cookie"
      videolib.cj.save(savepath + "cookie")
    watchit = mplayeroute + " " + flvlink
    usingcookie = False
  elif core.player.count('totem') == 1:
    watchit = core.totemroute + " " + flvlink
    
  else:
    messages("No mplayer or Totem detected", "Error")
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
      result = videolib.youtube(video)
    elif (typevideo == "nico"): #Start nicovideo
      global download, usingcookie
      result = videolib.niconico(video, mail, passw)
      usingcookie = True #That avoids create a new cookie
    elif (typevideo == "godtube"):
      result = videolib.godtube(video)
    elif (typevideo == "redtube"):
      result = videolib.redtube(video)
    elif (typevideo == "dailymotion"):
      result = videolib.dailymotion(video)
    elif (typevideo == "breakdotcom"):
      result = videolib.breakdotcom(video)
    elif (typevideo == "youporn"):
      result = videolib.youporn(video)
    elif (typevideo == "blip"):
      result = videolib.blip(video)
    return watchVideo(result)
  except urllib2.HTTPError,e: 
    if str(e.errno()) == "404":
      messages("That's a bad URL. I got a 404 Error", "Error")
  except urllib2.URLError:
    messages("You are not connected to internet, ISP problems or server down", "Error")
  except:
    raise


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
  validblip = video.find("lip.tv/file")
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
      videolib.cj.clear()
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
  elif validblip != -1: #IF is blip
    results = response(video, "blip")
  else:
    messages("Bad video url", "Error")
    return False
  #End Validating
  return False

def login(video):
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

  elif gui is "Gtk": #A login with GTK GUI
    #Method
    def accept(widget):
      global mail, passw
      mail = login_mail.get_text()
      passw = login_passw.get_text()
      if mail != "" and passw != "":
	      login.destroy()
	      return work(video)
    def close(widget):
      login.destroy()

    #Objects
    login = gtk.Window()
    layout = gtk.Table(2,3,True)
    login_mailtext = gtk.Label()
    login_mail = gtk.Entry()
    login_passtext = gtk.Label()
    login_passw = gtk.Entry()
    login_Ok = gtk.Button("Ok")
    login_cancel = gtk.Button("Cancel")
    
    #Grid
    layout.attach(login_mailtext,0,1,0,1)
    layout.attach(login_mail,1,2,0,1)
    layout.attach(login_passtext,0,1,1,2)
    layout.attach(login_passw,1,2,1,2)
    layout.attach(login_Ok,0,1,2,3)
    layout.attach(login_cancel,1,2,2,3)

    #Options and Run
    login_Ok.connect("clicked",accept)
    login_cancel.connect("clicked",close)
    login.connect("destroy", gtk.main_quit)
    login_mailtext.set_text("Email:")
    login_mail.set_text(mail)
    login_passtext.set_text("Password:")
    login_passw.set_visibility(False)
    login.add(layout)
    login.show_all()
    gtk.main()

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
      mail = raw_input("\nEmail: ")
      passw = getpass.getpass(prompt="Password: ")
      return work(video)
  return False
    
def PyQt4(): 
  from PyQt4.QtCore import SIGNAL, SLOT
  from PyQt4.QtGui import QDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
  app = QApplication(sys.argv)
  widget = QWidget()
  global guiparent
  
  #Objets
  label = QLabel(deflabel)
  box = QLineEdit(defvid)
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
  widget.setWindowTitle(deftit)
  widget.show()
  guiparent = app
  app.exec_()

def Gtk():
  global guiparent
  import gtk

  #Methods
  def gotowork(widget):
    if box.get_text() != "":
      video = box.get_text()
      work(video)
  #Objects
  app = gtk.Window()
  label = gtk.Label()
  box = gtk.Entry()
  button = gtk.Button("Watch It")

  #Layouts
  layout = gtk.Table(2,2,True)
  layout.attach(label, 0,1,0,1)
  layout.attach(box,1,2,0,1)
  layout.attach(button,1,2,1,2)

  #Signals and others!
  button.connect("clicked",gotowork)
  label.set_text(deflabel)
  box.set_text(defvid)

  app.connect("destroy", gtk.main_quit)
  app.add(layout)
  app.set_title(deftit)
  app.set_size_request(350, 50)
  app.show_all()
  guiparent = app
  gtk.main()

def Tk():
  import Tkinter as Tk
  import tkMessageBox as tkMB
  
  global guiparent
  #Methods
  def gotowork(*args):
    if box.get() != "":
      video = box.get()
      work(video)
      
  #Objets
  root = Tk.Tk()
  frame = Tk.Frame(root)
  label = Tk.Label(frame, text=deflabel)
  box = Tk.Entry(frame)
  button = Tk.Button(frame, text="Watch It!", command=gotowork)
  #Layouts
  label.grid(row=0)
  box.grid(row=1)
  button.grid(row=1, column=1)
  #Signals and others!
  root.title(deftit)
  root.minsize(350,50)
  box.insert(0, defvid)
  box.select_range(0, Tk.END)
  box.focus()
  box.bind("<Return>", gotowork)
  frame.pack()
  guiparent = root
  root.mainloop()
  
def console(): #Console only.
  while True:
    print("\nWrite exit for quit of the application\n")
    video = raw_input("Video Address: ")
    if (video == "exit" or video == "quit" or video == "q"):
      break
    elif (len(video) == 0):
      pass
    else:
      try:
        work(video)
      except:
	raise

def bashmode(): #Method for std input
  sys.argv.reverse()
  sys.argv.pop()
  sys.argv.reverse()
  for video in sys.argv:
    try:
      work(video)
    except:
      raise
      
def main(): #Main App
  print("Kamiltube Version: " + version)
  print("Kamlib Version: " + kamlib.__version__ + "\n")

  tempArgv = list(sys.argv)  #Check the parameters
  for x in tempArgv:
    if x.find("-") == 0:
      checkparameters(x[1:].capitalize())
      sys.argv.remove(x)

  if len(sys.argv) > 1:
    bashmode()
  elif defgui is "PyQt4": #Run PyQt4
    PyQt4()
  elif defgui is "Tk":
    Tk()
  elif defgui is "Gtk":
    Gtk()
  else:
    console()
  print("\nThanks for use Kamiltube")
      
try:
  if __name__ == '__main__':
    main()
except (KeyboardInterrupt, EOFError):
  pass
except:
  raise
