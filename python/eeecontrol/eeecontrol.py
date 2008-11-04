#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import web
from web.contrib.template import render_cheetah

urls = ('/', 'index', '/update', 'update')
render = render_cheetah('templates/')
Dir1 = "/proc/acpi/asus/"
Dir2 = "/sys/devices/platform/eeepc/"
webcam,card,wifi,clock = "<color=green>Online</color>"


def checkitout:
  
  return render.index(webcam = webcam, card = card, wifi = wifi, clock = clock)

class index:
  def GET(self):
    print "test"
    
class update:
  def GET(self):
    print "hola!"


if __name__ == "__main__":
  app = web.application(urls,globals())
  app.run()
