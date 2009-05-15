#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# Library to get the flv URL from various online videos webpages
# like youtube, nico douga and others. Mainly developed for
# kamiltube application, but you are free for use it for any
# application.
#

def urltranslator(url):
  "Translation from web symbols urls to strings"
  url = url.replace("%2F","/")
  url = url.replace("%3F","?")
  url = url.replace("%3D","=")
  url = url.replace("%3A",":")
  return url
  
class methods:
  import urllib, urllib2, os
  from cookielib import MozillaCookieJar
  mail = None
  passw = None
  cj = MozillaCookieJar()
  
  def saveCookie(self, path):
    
    "Here you can save your created cookie on ~/path/"
    self.cj.save(path)

  def youtube(self, video):
    """Here you must insert a youtube link called video. Should be partially uncomplete the link.
    Doing that you will get the location of flv video or some error <non link>."""
    video = "http://www.youtube.com/watch" + video[video.find("?v="):]
    resp = self.urllib2.urlopen(video).read()
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
      self.urllib2.urlopen(link)
    except urllib2.HTTPError:
      return "You cant watch this video using this quality, change it"
    return link
  
  def niconico(self, video, mail, passw):

    """Here you must insert a nico nico douga link on video with mail and
    passw are email and password of your nico nico douga user account,
    cj is a cookie jar, if you havent a cookie jar, only say None, i can
    create the cookie jar for you. With that, you will get the location of
    flv video and the cookie jar need it."""
    video = "http://www.nicovideo.jp/" + video[video.find("watch/"):]
    if video.find("?") is not -1:
      video = video[:video.find("?")]    
    nicode = video[video.find("watch/")+6:]
    self.cj.clear_expired_cookies()
    if len(self.cj) is 0:
      #print "Trying to login"
      opener = self.urllib2.build_opener(self.urllib2.HTTPCookieProcessor(self.cj))
      self.urllib2.install_opener(opener)
      url = "https://secure.nicovideo.jp/secure/login?site=niconico"
      values = {"mail": mail, "password": passw, "next_url": "/watch/" + nicode }
      params = self.urllib.urlencode(values)
      req = self.urllib2.Request(url, params)
      self.urllib2.urlopen(req)
      
    #req = self.urllib2.Request("http://www.nicovideo.jp/watch/" + nicode)
    #self.urllib2.urlopen(req)  
    
    url = "http://www.nicovideo.jp/api/getflv?v=" + nicode
    req = self.urllib2.Request(url)
    fvideo = self.urllib2.urlopen(req).read()
        
    if fvideo == "closed=1&done=true":
      return "Invalid Username or Password", None
    #print "Logged in"
    smile = fvideo[fvideo.find("&url=")+5:fvideo.find("&link=")]
    video = urltranslator(smile)
    #video = "http://smile" + smile + ".nicovideo.jp/smile?v=" + code
    return video
  
  def redtube(video):
    
    """That functon is not implemented, if you can help, i will thank you"""
  
    return "Not implemented"
    
  def godtube(video):
  
    """Here you must insert a godtube link called.
    Doing that you will get the location of flv video or some error <non link>.
    I know a bug with godtube and i dont know fix that, but at least works with some
    links. If you want help, welcome!"""
  
    video = "http://www.godtube.com/" + video[video.find("view_video.php?"):]
    #print video
    resp = urllib2.urlopen(video).read()
    link = "http://video.godtube.com/" + resp[resp.find("video=flvideo")+6:resp.find("flv&viewkey")+3]
    try:
      urllib2.urlopen("http://video.godtube.com/flvideo2/c7e177079d3786edb467/194613.flv")
    except urllib2.HTTPError:
      return "Unknown Error"
    return link
  
  def breakdotcom(video):
  
    """Here you must insert a break.com link.
    Doing that you will get the location of flv video."""
  
    if video.find("/my.break") != -1:
      video = "http://my.bre" + video[video.find("ak.com/"):]
    else:
      video = "http://www.bre" + video[video.find("ak.com/"):]
      resp = urllib2.urlopen(video).read()
      a = resp[resp.find("videoPath', '")+13:resp.find("'+sGlobalContentFilePath+'/'+sGlobalFileName+'.flv'")] #Start
      b = resp[resp.find("sGlobalContentFilePath=")+24:resp.find("';sGlobalContentUrl=")] #Global Content FilePath
      c = resp[resp.find("sGlobalFileName=")+17:resp.find("';sGlobalContentID='")] #Global Content FileName
    return a+b+"/"+c+".flv"
    
  def dailymotion(video):
  
    """Here you must insert a dailymotion link.
    Doing that you will get the location of flv video.
    I have a small error."""
  
    video = "http://www.dailymo" + video[video.find("tion.com"):]
    resp = urllib2.urlopen(video).read()
    resp1 = resp[resp.find("&videoUrl=")+10:]
    link = resp1[:resp1.find("&embedUrl=")]
    link = urltranslator(link)
    #link = "http://www.dailymotion.com/" + link
    return link
    
  def youporn(video):
  
    """Here you must insert a youporn link.
    Doing that you will get the location of flv video.
    Not complete"""
    video = "http://youporn.com/" + video[video.find("watch/"):]
    #Adult check
    values = {"id": "enterbutton","type":"submit","name": "user_choice", "value": "enter" }
    params = urllib.urlencode(values)
    req = urllib2.Request(video, params)
    resp = urllib2.urlopen(req).read()
    #End adult check
    link = resp[resp.find("<h2>Download:</h2>"):resp.find("FLV - Flash Video format</a>")-2]
    vid = link[link.find("<a href=\"")+9:]
    return vid