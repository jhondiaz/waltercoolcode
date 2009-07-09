# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# Methods used for kamlib. I dont want mix the web database
# with external methods. This is mainly developed for
# kamiltube application, but you are free for use it for any
# GPL-2 compatible application.
#

def urltranslator(url):
  "Translation from web symbols urls to strings"
  url = url.replace("%2F","/")
  url = url.replace("%3F","?")
  url = url.replace("%3D","=")
  url = url.replace("%3A",":")
  return url
  
