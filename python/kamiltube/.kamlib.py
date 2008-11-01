#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import urllib, urllib2
from cookielib import MozillaCookieJar
cj =  None
mail = None
passw = None

def youtube(video, valid):
  video = "http://www.yout" + video[valid:]
  resp = urllib2.urlopen(video).read()
  cut1 = resp[resp.find("video_id="):]
  video_id = cut1[:cut1.find("&")]
  #print "Video ID= " + video_id
  cut2 = cut1[cut1.find("&t=")+1:]
  video_t = cut2[:cut2.find("&")]
  #print "Video T= " + video_t
  link = "\"http://www.youtube.com/get_video?" + video_id + "&" + video_t + "\""
  print "link: " + link
  return link
  
def niconico(video, valid, mail, passw, cj):
  nicode = video[video.find("watch/")+6:]
  video = "http://www.nicovide" + video[valid:]
  if cj is None:
    cj = MozillaCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    url = "https://secure.nicovideo.jp/secure/login?site=niconico"
    values = {"mail": mail, "password": passw, "next_url": "/" }
    params = urllib.urlencode(values)
    req = urllib2.Request(url, params)
    urllib2.urlopen(req)
    print "Trying to login"
  
  req = urllib2.Request("http://www.nicovideo.jp/watch/" + nicode)
  urllib2.urlopen(req)
    
  url = "http://www.nicovideo.jp/api/getflv?v=" + nicode
  print "URL=" + url
  req = urllib2.Request(url)
  fvideo = urllib2.urlopen(req).read()
  print "Getting data"
  
  if fvideo == "closed=1&done=true":
    return "badlogin", None
  smile = fvideo[fvideo.find("%2Fsmile")+8:fvideo.find(".nicovideo.jp")]
  code = fvideo[fvideo.find("%3D")+3:fvideo.find("&link=")]
  cj.save("./cookies")
  video = "http://smile" + smile + ".nicovideo.jp/smile?v=" + code
  print fvideo
  print smile
  print video

  print "Watching Video..."
  link = "-cookies -cookies-file cookies \"" + video + "\""
  return link, cj

def redtube(video, valid):
  #Example1: http://www.redtube.com/14924
  #Response1:http://dl.redtube.com/_videos_t4vn23s9jc5498tgj49icfj4678/0000014/C577DH0LD.flv
  #Example2: http://www.redtube.com/3171
  #Response2: dl.redtube.com/_videos_t4vn23s9jc5498tgj49icfj4678/0000003/I2XDPA18A.flv
  return "disabled"
