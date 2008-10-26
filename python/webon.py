#!/usr/bin/env python

#
# Developed by Pablo Cholaky.
#   Under GPL-2 License
#

import urllib, urllib2, cookielib
from os import system

web = "http://www.nicovideo.jp/watch/sm1727663"
nicode = web[web.find("watch/")+6:]
print nicode
#url = "http://localhost:8080"
#values = {"loguser": "waltercool", "logpasswd": "1234"}
cj = cookielib.MozillaCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
url = "https://secure.nicovideo.jp/secure/login?site=niconico"
values = {"mail": "", "password": "", "next_url": "/watch/sm1727663"}
params = urllib.urlencode(values)
req = urllib2.Request(url, params)
urllib2.urlopen(req)
print "Entre"

#f = ClientCookie.urlopen(req)
url = "http://www.nicovideo.jp/watch/sm1727663"
req = urllib2.Request(url)
urllib2.urlopen(req)
print "Viendo video"

url = "http://www.nicovideo.jp/api/getflv?v=sm1727663"
req = urllib2.Request(url)
fvideo = urllib2.urlopen(req).read()
print "Obteniendo data"
print "Fvideo:" + fvideo

smile = fvideo[fvideo.find("%2Fsmile")+8:fvideo.find(".nicovideo.jp")]
code = fvideo[fvideo.find("%3Fv%3D")+7:fvideo.find("&link=")]
#print smile
#print code
cj.save("./cookies")
video = "http://smile" + smile + ".nicovideo.jp/smile?v=" + code

#req = urllib2.Request(video)

#f = open("video.flv", "wb+")
print "Descargando..."
#f.write(urllib2.urlopen(req).read())
vid = "mplayer -cookies -cookies-file cookies \"" + video + "\""
system(vid)
