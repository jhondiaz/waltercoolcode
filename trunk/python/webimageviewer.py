#!/usr/bin/python
#
# Developed by Pablo Cholaky.
#   Under GPL-2 License
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