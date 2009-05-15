#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import urllib, urllib2, os
from cookielib import MozillaCookieJar
cj =  None
mail = None
passw = None

def urltranslator(url):
  url = url.replace("%2F","/")
  url = url.replace("%3F","?")
  url = url.replace("%3D","=")
  return url



def youtube(video, valid):

  """Here you must insert a youtube link with valid = 0, im using valid for checking.
  Doing that you will get the location of flv video or some error <non link>."""

  video = "http://www.yout" + video[valid:]
  resp = urllib2.urlopen(video).read()
  #Protection
  if resp.find("This video is no longer available due to a copyright") is not -1:
    return "This video is not available due copyright"
  if resp.find("This video has been removed by the user.") is not -1:
    return "This video has been removed by the user."
  elif resp.find("The URL contained a malformed video ID.") is not -1:
    return "Bad video url"
  elif resp.find("This video or group may contain content that is inappropriate") is not -1:
    return "Is a video for 18+, you must be logged in, but you cant now."
  elif resp.find("This is a private video.") is not -1:
    return "Private Video"
  elif resp.find("This video is not available in your country.") is not -1:
    return "This video is not available in your country."
  #End Protection
  cut1 = resp[resp.find("video_id="):]
  video_id = cut1[:cut1.find("&")]
  
  cut2 = resp[resp.find("&t=")+1:]
  video_t = cut2[:cut2.find("&")]
  
  if video.find("&fmt=") is not -1:
    qual = "&fmt=" + video[video.find("fmt=")+4:video.find("fmt=")+6]
  else:
    qual = ""
  link = "http://www.youtube.com/get_video?" + video_id + "&" + video_t + qual
  try:
    urllib2.urlopen(link)
  except urllib2.HTTPError:
    return "You cant watch this video using this quality, change it"
  return link
  
def niconico(video, valid, mail, passw, cj):

  """Here you must insert a nico nico douga link on videowith valid = 0, 
  im using valid for checking, mail and passw are email and password
  of your nico nico douga user account, cj is a cookie jar, can be None
  because if is None, i can create a new CookieJar, else, i will use your
  CookieJar, doing that you will get the location of flv video."""

  nicode = video[video.find("watch/")+6:]
  video = "http://www.nicovide" + video[valid:]
  if cj is None:
    print "Trying to login"
    cj = MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    url = "https://secure.nicovideo.jp/secure/login?site=niconico"
    values = {"mail": mail, "password": passw, "next_url": "/watch/" + nicode }
    params = urllib.urlencode(values)
    req = urllib2.Request(url, params)
    urllib2.urlopen(req)
  else:
    req = urllib2.Request("http://www.nicovideo.jp/watch/" + nicode)
    urllib2.urlopen(req)
    
  url = "http://www.nicovideo.jp/api/getflv?v=" + nicode
  print "URL=" + url
  req = urllib2.Request(url)
  fvideo = urllib2.urlopen(req).read()
  
  if fvideo == "closed=1&done=true":
    return "Invalid Username or Password", None
  print "Logged in"
  smile = fvideo[fvideo.find("%2Fsmile")+8:fvideo.find(".nicovideo.jp")]
  code = fvideo[fvideo.find("%3D")+3:fvideo.find("&link=")]
  cj.save(os.environ['HOME'] + "/.kamiltube/cookies")
    
  video = "http://smile" + smile + ".nicovideo.jp/smile?v=" + code
  print video
  return video,cj

def redtube(video, valid):
  
  """That functon is not implemented, if you can help, i will thank you"""

  return "Not implemented"
  
def godtube(video, valid):


  """Here you must insert a godtube link with valid = 0, im using valid for checking.
  Doing that you will get the location of flv video or some error <non link>.
  I know a bug with godtube and i dont know fix that, but at least works with some
  links."""

  video = "http://www.g" + video[valid:]
  print video
  resp = urllib2.urlopen(video).read()
  link = "http://video.godtube.com/" + resp[resp.find("video=flvideo")+6:resp.find("flv&viewkey")+3]
  try:
    urllib2.urlopen("http://video.godtube.com/flvideo2/c7e177079d3786edb467/194613.flv")
  except urllib2.HTTPError:
    return "Unknown Error"
  return link

def breakdotcom(video, valid):

  """Here you must insert a break.com link with valid = 0, im using valid for checking.
  Doing that you will get the location of flv video or some error <non link>."""

  if video.find("/my.break") != -1:
    video = "http://my.bre" + video[valid:]
  else:
    video = "http://www.bre" + video[valid:]
  resp = urllib2.urlopen(video).read()
  a = resp[resp.find("videoPath', '")+13:resp.find("'+sGlobalContentFilePath+'/'+sGlobalFileName+'.flv'")] #Start
  b = resp[resp.find("sGlobalContentFilePath=")+24:resp.find("';sGlobalContentUrl=")] #Global Content FilePath
  c = resp[resp.find("sGlobalFileName=")+17:resp.find("';sGlobalContentID='")] #Global Content FileName
  return a+b+"/"+c+".flv"
  
def dailymotion(video, valid):

  """Here you must insert a dailymotion link with valid = 0, im using valid for checking.
  Doing that you will get the location of flv video or some error <non link>."""

  video = "http://www.dailymo" + video[valid:]
  resp = urllib2.urlopen(video).read()
  resp1 = resp[resp.find("&videoUrl=")+10:]
  link = resp1[:resp1.find("&embedUrl=")]
  link = urltranslator(link)
  #link = "http://www.dailymotion.com/" + link
  return link
  
def youporn(video, valid):

  """Here you must insert a youporn link with valid = 0, im using valid for checking.
  Doing that you will get the location of flv video or some error <non link>."""
  video = "http://youp" + video[valid:]
  #Adult check
  values = {"id": "enterbutton","type":"submit","name": "user_choice", "value": "enter" }
  params = urllib.urlencode(values)
  req = urllib2.Request(video, params)
  resp = urllib2.urlopen(req).read()
  #End adult check
  link = resp[resp.find("<h2>Download:</h2>"):resp.find("FLV - Flash Video format</a>")-2]
  vid = link[link.find("<a href=\"")+9:]
  return vid
