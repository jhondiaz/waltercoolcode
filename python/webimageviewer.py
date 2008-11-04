#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import os
import web
from web.contrib.template import render_cheetah

version = "Version 0.001 Alpha"
urls= ('/','index','/viewdir','viewdir','/photoview','photoview')
render = render_cheetah('templates/')

class index:
  def GET(self):
    global version
    return render.imageviewer_index(version = version)

class viewdir:
  def GET(self):
    return render.imageviewer_index()
  def POST(self):
    return render.imageviewer_viewdir()
    
class photoview:
  def GET(self):
    return render.imageviewer_photoview()
    
if __name__ == "__main__":
  app = web.application(urls,globals())
  app.run()
