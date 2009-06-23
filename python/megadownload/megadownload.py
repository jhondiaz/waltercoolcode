#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# Version 1.0 Stable

import urllib, urllib2, sys, os, math, getpass
from cookielib import MozillaCookieJar

autoskip = False
autoskipAsk = False
if (len(sys.argv) > 1):
  if (sys.argv.count("help") > 0): #If someone ask for help
    print("Megadownload.\nYou must create a links named file with your megadownload links, bad typed urls will not downloaded\n")
    print("Usage: megadownload.py, If finds a links named file, i should download your megaupload files")
    print("       megadownload.py <route>, If finds a links named file on <route>, i should download your megaupload files on that route")
    sys.exit(0)
  else:
    path = sys.argv[1]
else:
  path = os.path.realpath("") + "/"

def exit(): #Bye!
  print "Thanks for use this program!"
  print "Visit www.slash.cl for more info"
  sys.exit(0)

def hook(blockNumber, blockSize, totalSize): #Is dirty!
  downloaded = blockNumber * blockSize / 1.0
  tsize = totalSize / 1.0
  size = "b"
  tsizes = "b"
  if downloaded > 1024:
    downloaded = downloaded/1024
    size = "Kb"
    if downloaded > 1024:
      downloaded = downloaded/1024
      size = "Mb"
  if tsize > 1024: #Bad bad bad, really bad implemented!.
    tsize = tsize/1024
    tsizes = "Kb"
    if tsize > 1024:
      tsize = tsize/1024
      tsizes = "Mb"
      if tsize > 1024: #Ugly!
	tsize = tsize/1024
	tsizes = "Gb"
  print "\rDownloading %.3f %s of %.3f %s   " % (downloaded, size, tsize, tsizes) ,

def loginmegaupload():
  cj = MozillaCookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  urllib2.install_opener(opener)
  url = "http://www.megaupload.com/?c=login"
  username = raw_input("Username: ")
  password = getpass.getpass(prompt="Password: ")
  print "Logging in"
  params = urllib.urlencode({"login":1, "redir":1, "username":username, "password":password})
  req = urllib2.Request(url, params)
  try:
    checklogin = urllib2.urlopen(req).read()
  except urllib2.URLError: #If you arent on internet.
    print "Not connected to internet!"
    exit()
  if checklogin.find("\">Sign out</a>") == -1:
    print "Username or password invalid"
    question = raw_input("Try again? Y/n: ").capitalize() #You are failed on a word?
    if question == "N":
      quit()
    else:
      cj = loginmegaupload()
      return cj
  print "Logged"
  return cj #Maybe i can use it on future.
  
def checkmegaupload(links):
  try:
    url = urllib2.urlopen(links).read()
  except urllib2.URLError:
    print "Not connected to internet!"
    exit()
    
  notavailable = "Unfortunately, the link you have clicked is not available."
  unavailable = "The file you are trying to access is temporarily unavailable"
  if url.find(notavailable) != -1: 
    return "dead link"
  if url.find(unavailable) != -1:
    return "down link"
  return "live link"
  
def megaupload(link):
  global autoskip, autoskipAsk
  url = urllib2.urlopen(link).read()
  down1 = url[url.find("id=\"downloadlink\">"):]
  down2 = down1[down1.find("<a href=\"")+9:]
  valid = down2[:down2.find("\"")]
  filename = valid.split('/')[-1] #Name, i like for print use only
  destinypath = path + filename #Path + Filename
  
  #Start "When exist a file..."
  if autoskip != True and (os.path.exists(destinypath) is True): # If is not autoskipped.
      filexist = raw_input("A file with the same name " + filename + " exists, overwrite? y/N/q: ").capitalize()

      if filexist == "Q":
        quit() #You want quit.
      if (filexist != "Y") and (autoskipAsk == False): # Skip that file for first time?
	autoskipAsk = True
	askipall = raw_input("Autoskip All? Y/n: ").capitalize()
	if askipall != "N": # If you want autoskip all.
	  autoskip = True

  if (autoskip == True) and (os.path.exists(destinypath) is True): # When autoskip is on.
    print "Skipped " + filename + ", url = " + link
    return True
  #End "When exist a file..."
    
  print "Downloading " + valid.split('/')[-1] + " as " + link
  
  try: #Download it.!
    urllib.urlretrieve(valid,destinypath, hook)
    print "\nDownloaded."
  except IOError: #If IO Error
    print "No space on disk or data write error"
    IOresp = raw_input("Retry? Y/n/q: ").capitalize()
    try:
      os.remove(destinypath)
    except:
      pass
    if (IOresp == "Q"):
     sys.exit(0)
    elif (IOresp == "Y") or (IOresp == ""):
      megaupload(link)
      return 1
  except KeyboardInterrupt:
    try:
      os.remove(destinypath)
    except:
      pass
    print "Stopped, i have deleted the file..."
    sys.exit(1)
  except: #If something is wrong...
    print "\nError."
    raise
    discon = raw_input("I lose the connection downloading " + link + ", try again? Y/n/q: ").capitalize()
    try: #Try to remove the file.
      os.remove(destinypath)
    except: #Well, if i havent start to download, continue.
      pass

    if (discon == "") or (discon == "Y"): #You want continue?
      megaupload(link)
      return True
    elif discon == "Q": #You want exit.
      quit()
    else: #You want skip that file...
      print "Skipping"
      os.remove(destinypath)
  return True
  
def megalink(link): #Is a valid link or strange text?
  fixlink = link.replace(" ","")
  start = fixlink.find("http://www.megaupload.com")
  if start == -1:
    return "nolink"
  return fixlink[start:]

try: #Open the file.
  f = open(path + "links", "rw")
except:
  print("You need a \"links\" file with the urls.")
  quit()
totallines = 0
validlinks = []
deadlink = []
downlink = []
livelink = []
for lineas in f:
  lines = megalink(lineas)
  if lines != "nolink":
    validlinks += [lines]

checklinks = raw_input("You want check the links? Y/n/q: ").capitalize()
if checklinks == "Q": #You want quit.
  exit()
elif checklinks != "N": #You want check it.
  print "Checking for dead links..."
  x = 0
  for lineas in validlinks:
    stats = checkmegaupload(lineas)
    if stats == "live link":
      livelink += [lineas]
    elif stats == "down link":
      downlink += [lineas]
    else:
      deadlink += [lineas]
    x += 1
    sys.stdout.write( str(x) + " ")
    sys.stdout.flush() 

  print "\n" + str(len(livelink)) + " links ready for download"
  print str(len(downlink)) + " links are temporarily down"
  for lineas in downlink:
    print "- Link down: " + lineas
  print str(len(deadlink)) + " links are dead"
  for lineas in deadlink:
    print "- Link dead: " + lineas
  if len(livelink) == 0:
    print "Sorry, you cant download files on your list."
    quit()
    if len(downlink) != 0: #You cant download a file
      print "Try again when this " + str(len(downlink)) + " become available"
      quit()
  cont = raw_input("Continue? Y/n: ").capitalize() #Are you happy with resuts?
else:
  for lineas in validlinks:
    lines = megalink(lineas)
    if lines != "nolink":
      livelink += [lineas]
  cont = ""

if cont != "N":
  loginmegaupload() #Log it.
  for lineas in livelink:
    megaupload(lineas) #Download the N files.
