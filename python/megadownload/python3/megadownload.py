#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# Version 1.0 Stable

import urllib, urllib.request, urllib.error, urllib.parse, math, getpass,os
sys = os.sys
from http.cookiejar import MozillaCookieJar

autoskip = False
autoskipAsk = False
wrongSize = 0

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
  print('Thanks for use this program!')
  print('Visit www.slash.cl for more info')
  sys.exit(0)

def download(valid, destinypath, link): #Download algorithm.
  try: #Download it.!
    urllib.request.urlretrieve(valid,destinypath, hook)
    print('\nDownloaded.')
  except IOError: #If IO Error
    print('No space on disk or data write error')
    IOresp = input("Retry? Y/n/q: ").capitalize()
    try:
      os.remove(destinypath)
    except:
      pass
    if (IOresp == "Q"):
     sys.exit(0)
    elif (IOresp == "Y") or (IOresp == ""): #You want try again? Resume!!!
      return False
  except KeyboardInterrupt:
    try:
      os.remove(destinypath)
    except:
      pass
    print("Stopped, i have deleted the file...")
    sys.exit(1)
  except: #If something is wrong...
    print("\nError.")
    raise
  return True

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
  downloaded = format(downloaded,'.5g')
  tsize = format(tsize,'.5g')
  print("\rDownloading {} {} of {} {}   ".format(downloaded, size, tsize, tsizes), end=' ')

def loginmegaupload(): #Try validating on megaupload server.
  cj = MozillaCookieJar()
  opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
  urllib.request.install_opener(opener)
  url = "http://www.megaupload.com/?c=login"
  username = input("\nUsername: ")
  password = getpass.getpass(prompt="Password: ")
  if not (username != '' and password != ''):
    return False
  print("Logging in")
  params = urllib.parse.urlencode({"login":1, "redir":1, "username":username, "password":password})
  req = urllib.request.Request(url, params)
  try:
    checklogin = bytes.decode(urllib.request.urlopen(req).read())
  except urllib.error.URLError: #If you arent on internet.
    print("Not connected to internet!")
    exit()
  if checklogin.find("Username and password do not match. Please try again!") > 1:
    print("Username or password invalid")
    question = input("Try again? Y/n: ").capitalize() #You are failed on a word?
    if question == "N" or question == 'Q':
      quit()
    else:
      cj = loginmegaupload()
      return cj
  elif checklogin.find('\">Sign out</a>') > 0:
    print("Logged")
    return cj #Maybe i can use it on future.
  else:
    print('Error')  
  return False
  
def checkmegaupload(links):
  try:
    url = bytes.decode(urllib.request.urlopen(links).read())
  except urllib.error.URLError:
    print("Not connected to internet!")
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
  url = bytes.decode(urllib.request.urlopen(link).read())
  down1 = url[url.find("id=\"downloadlink\">"):]
  down2 = down1[down1.find("<a href=\"")+9:]
  valid = down2[:down2.find("\"")] #Download Link
  filename = valid.split('/')[-1] #Name, i like for print use only
  destinypath = path + filename #Path + Filename
  
  #Start "When exist a file..."
  if autoskip != True and (os.path.exists(destinypath) is True): # If is not autoskipped.
      filexist = input("A file with the same name " + filename + " exists, overwrite? y/N/q: ").capitalize()

      if filexist == "Q":
        quit() #You want quit.
      if (filexist != "Y") and (autoskipAsk == False): # Skip that file for first time?
        autoskipAsk = True
        askipall = input("Autoskip All? Y/n: ").capitalize()
        if askipall != "N": # If you want autoskip all.
          autoskip = True

  if (autoskip == True) and (os.path.exists(destinypath) is True): # When autoskip is on.
    print("Skipped " + filename + ", url = " + link)
    return True
  #End "When exist a file..."

  print("Downloading " + valid.split('/')[-1] + " as " + link)
  dow = download(valid, destinypath, link) #Start to download.
  if dow is False: #If fail
    megaupload(link)
  
  return True
  
def megalink(link): #Is a valid link or strange text?
  fixlink = link.replace(" ","")
  start = fixlink.find("http://www.megaupload.com")
  if start == -1:
    return "nolink"
  return fixlink[start:]

def main():
  try: #Open the file.
    f = open(path + "links")
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

  checklinks = input("You want check the links? Y/n/q: ").capitalize()
  if checklinks == "Q": #You want quit.
    exit()
  elif checklinks != "N": #You want check it.
    print("Checking for dead links...")
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
    print('')
    print(len(livelink), "links ready for download")
    print(len(downlink), 'links are temporarily down')
    for lineas in downlink:
      print('- Link down:', lineas)
    print(len(deadlink), " links are dead")
    for lineas in deadlink:
      print("- Link dead:", lineas)
    if len(livelink) == 0:
      print("Sorry, you cant download files on your list.")
      quit()
      if len(downlink) != 0: #You cant download a file
        print("Try again when this", downlink, "become available")
        quit()
    cont = input("Continue? Y/n: ").capitalize() #Are you happy with resuts?
  else:
    for lineas in validlinks:
      lines = megalink(lineas)
      if lines != "nolink":
        livelink += [lineas]
    cont = ""

  if cont != "N":
    while not loginmegaupload(): #Log it
      pass
    for lineas in livelink:
      megaupload(lineas) #Download the N files.

if __name__ == '__main__':
  main()
