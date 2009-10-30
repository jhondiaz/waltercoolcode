#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import gdata
import gdata.photos.service
import sys, getpass

class pypicasa():
  def __init__(self):
    self.gclient = gdata.photos.service.PhotosService()
  def login(self, email=None, passw=None):
    if email == None and passw == None:
      self.gclient.email = raw_input("Username: ")
      self.gclient.password = getpass.getpass(prompt="Password: ")
    try:
      self.gclient.ProgrammaticLogin()
    except gdata.service.BadAuthentication:
      print("Bad login. Try again")
      sys.exit(0)
    print("Now logged as " + self.gclient.email)
  
  def req_data(self):
    self.albums = []
    info = self.gclient.GetUserFeed()
    for x in info.entry:
      self.albums.append(x.title.text)
    if self.albums.count("Pypicasa Uploaded") == 0:
      print("Pypicasa album not detected...")
      self.gclient.InsertAlbum("Pypicasa Uploaded","Uploaded pictures from pypicasa")
      print("Pypicasa album created.")
   def upload(self):
     
if __name__ == "__main__":
  a = pypicasa()
  a.login()
  a.req_data()
