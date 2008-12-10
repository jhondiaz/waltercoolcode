#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import urllib, urllib2, sys, os, math
from cookielib import MozillaCookieJar

autoskip = False
autoskipAsk = False

def quit():
  print "Thanks for use this program!"
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
  if tsize > 1024:
    tsize = tsize/1024
    tsizes = "Kb"
    if tsize > 1024:
      tsize = tsize/1024
      tsizes = "Mb"
      if tsize > 1024:
	tsize = tsize/1024
	tsizes = "Gb"
  print "\rDownloading %s %s of %s %s" % (downloaded, size, tsize, tsizes) ,

def loginmegaupload():
  cj = MozillaCookieJar()
  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
  urllib2.install_opener(opener)
  url = "http://www.megaupload.com/"
  username = raw_input("Username: ")
  password = raw_input("Password: ")
  print "Logging in"
  params = urllib.urlencode({"login":username, "password":password})
  req = urllib2.Request(url, params)
  checklogin = urllib2.urlopen(req).read()
  if checklogin.find("name=\"logout\"") == -1:
    print "Username or password invalid"
    sys.exit(0)
  print "Logged"
  return cj
  
def checkmegaupload(links):
  try:
    url = urllib2.urlopen(links).read()
  except urllib.URLError:
    print "Not connected to internet!"
    sys.exit(0)
    
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
  down1 = url[url.find("innerHTML = '<a href=\"http://www")+5:]
  down1 = down1[down1.find("innerHTML = '<a href=\"http://www")+5:]
  valid1 = down1[down1.find("innerHTML = '<a href=\"http://www")+22:]
  valido = valid1[:down1.find("\" ")-7]
  
  abs1 = url[url.find("Math.abs(")+9:]
  try:
    absol = abs(int(abs1[:abs1.find("));")]))
  except ValueError:
    print "This URL have problems, check your links again with this app"
  
  sqr1 = url[url.find("Math.sqrt(")+10:]
  sqr = int(math.sqrt(int(sqr1[:sqr1.find("));")])))
  
  valor = str(url[url.find("Math.sqrt(")-25:url.find("Math.sqrt(")-24])
  
  validop1 = valido[:valido.find("' + ")]
  validop2 = valido[valido.find(" + '")+4:]
  valido = validop1 + valor + unichr(sqr) + unichr(absol) + validop2

  #webFile = urllib.urlopen(valido)
  filename = valido.split('/')[-1]
  
  #Start "When exist a file..."
  if autoskip != True and (os.path.exists(filename) is True): # If is not autoskipped.
      filexist = raw_input("A file with the same name " + filename + " exists, overwrite? y/N: ").capitalize()
      if filexist != "Y": # You want skip that file
	if autoskipAsk is False: # I havent asked you for autoskip
	  autoskipAsk = True
	  askipall = raw_input("Autoskip All? Y/n: ").capitalize()
		
	  if (askipall == "Y") or (askipall == ""): # If you want autoskip all
	    autoskip = True
  if (autoskip == True) and (os.path.exists(filename) is True): # When autoskip is on.
    print "Skipped " + filename + ", url = " + link
    return True
  #End "When exist a file..."
    
  #localFile = open(filename, 'w')
  print "Downloading " + valido.split('/')[-1] + " as " + link
  
  try:
    #localFile.write(webFile.read())
    #localFile.close()
    urllib.urlretrieve(valido,filename, hook)
    print "\rDownloaded."
  except:
    print "  Error."
    discon = raw_input("I lose the connection downloading " + link + ", try again? Y/n/q: ").capitalize()
    if (discon == "") or (discon == "Y"):
      os.remove(filename)
      megaupload(link)
      return True
    elif discon == "Q":
      os.remove(filename)
      exit()
    else:
      print "Skipping"
      os.remove(filename)
  
def megalink(link): #Is a valid link or strange text?
  start = link.find("http://")
  if start == -1:
    return "nolink"
  return link[start:]
try:
  f = open("links", "rw")
except:
  print("You need a \"links\" file with the urls.")
  sys.exit(0)
deadlink = []
downlink = []
livelink = []
checklinks = raw_input("You want check the links? Y/n/q: ").capitalize()
if checklinks == "Q":
  exit()
elif checklinks != "N":
  print "Checking for dead links..."
  for lineas in f:
    lines = megalink(lineas)
    if lines != "nolink":
      stats = checkmegaupload(lineas)
      if stats == "live link":
	livelink += [lineas]
      elif stats == "down link":
	downlink += [lineas]
      else:
	deadlink += [lineas]
  
  print str(len(livelink)) + " links ready for download"
  print str(len(downlink)) + " links are temporarily down"
  for lineas in downlink:
    print "- Link down: " + lineas
  print str(len(deadlink)) + " links are dead"
  for lineas in deadlink:
    print "- Link dead: " + lineas
  if len(livelink) == 0:
    print "Sorry, you cant download files on your list."
    sys.exit(0)
    if len(downlink) != 0:
      print "Try again when this " + str(len(downlink)) + " become available"
      sys.exit(0)
  cont = raw_input("Continue? Y/n: ").capitalize()
else:
  for lineas in f:
    lines = megalink(lineas)
    if lines != "nolink":
      livelink += [lineas]
  cont = ""

if cont == "" or cont == "Y":
  loginmegaupload()
  for lineas in livelink:
    megaupload(lineas)
