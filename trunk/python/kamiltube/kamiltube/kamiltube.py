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
  import kamiltube_core
  import kamiltube_gui
except ImportError:
  print("Data missing!")
  sys.exit(1)

videolib = kamlib.weblib.video() #Loading a kamlib object
core = kamlib.core.work()

#Variables
mail = ""
passw = ""
cookie = None
usingcookie = False
download = False
savepath = os.environ['HOME'] + "/.kamiltube/"
debugMode = False
gui = None
playersupport = list()
#End Variables
#GUI Global Variables
deftit = "Kamiltube " + version
defvid = "http://www.youtube.com/watch?v=iW87vxM11tw"
deflabel = "Video Address:"
defgui=""
#End GUI Global Variables

def checkparameters(x): #For something
  global gui, debugMode
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
  if x.find("-qt4") == 0 and gui != "PyQt4" and core.gui.count("Qt4") == 1:
    if debugMode == True: #Only for debug
      print("Using PyQt4 version")
    gui = "PyQt4"
  elif x.find("-tk") == 0 and gui != "Tk" and core.gui.count("Tk") == 1:
    if debugMode == True: #Only for debug
      print("Using Tk version")
    gui = "Tk"
  elif x.find("-gtk") == 0 and gui != "Gtk" and core.gui.count("Gtk") == 1:
    if debugMode == True: #Only for debug
      print("Using Gtk version")
    gui = "Gtk"
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
  if os.path.exists(mplayeroute) is True:
    if (usingcookie is True):
      if (download is False):
        flvlink = flvlink + " -cookies -cookies-file " + savepath + "cookie"
      else:
        flvlink = flvlink + " --load-cookies=" + savepath + "cookie"
      videolib.cj.save(savepath + "cookie")
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
  elif gui is "PyQt4": #Run PyQt4
    guiPyQt4()
  elif gui is "Tk":
    guiTk()
  elif gui is "Gtk":
    guiGtk()
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
