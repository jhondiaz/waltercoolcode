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
import sys, getpass, mimetypes, os

class pypicasa():
  def __init__(self):
    self.gclient = gdata.photos.service.PhotosService()
  def login(self, email=None, passw=None):
    if email == None and passw == None:
      email = raw_input("Username: ")
      passw = getpass.getpass(prompt="Password: ")
    self.gclient.email = email
    self.gclient.password = passw
    try:
      self.gclient.ProgrammaticLogin()
    except gdata.service.BadAuthentication:
      print("Bad login. Try again")
      self.login()
      return True
    print("Now logged as " + self.gclient.email)
    return True
  
  def req_data(self): #Add a list of albums
    self.albums = {}
    info = self.gclient.GetUserFeed()
    for x in info.entry:
      self.albums[x.title.text] = x.gphoto_id.text
      
  def check_album(self,album): #Check for album
    if self.albums.has_key(album):
      return True
    else:
      return False
      
  def create_album(self,album): #New album
    if self.check_album(album):
      return False
    else:
      print("* New album " + album)
      desc = raw_input("Add a description. Press q for exit: ")
      if desc.capitalize() == "Q":
        return False
      else:
        self.gclient.InsertAlbum(album, desc)
        
  def photoToName(self,photo):
    pic = photo.split(".")
    pic.pop()
    newPic = ""
    for a in pic:
      newPic = newPic + "." + a
    return newPic[1:]

  def uploadPicture(self, album, photo, desc):
    if self.check_album(album) == False:
      if self.create_album(album) == False:
        return False
    album_url = '/data/feed/api/user/%s/albumid/%s' % (self.gclient.email, self.albums[album])
    mime = mimetypes.guess_type(photo)[0]
    photo = self.gclient.InsertPhotoSimple(album_url, self.photoToName(photo), desc, photo, mime)
    
def help:
  print("Help\n")
  print("Album list: List all your albums")
  print("New Album: Add a new album")
  print("Upload photo: Add a new photo")
      
             
if __name__ == "__main__":
  googleobj = pypicasa()
  googleobj.login()
  googleobj.req_data()
  while True:
    a = raw_input("What are you doing?: ").capitalize()
    if a == "Upload photo":
      photo = raw_input("What filename?: ")
      desc = raw_input("Photo description?: ")
      album = raw_input("What album?: ")
      if os.path.exists(photo):
        googleobj.uploadPicture(album, photo, desc)
      else:
        print("Photo not found")
      
    if a == "Upload folder":
      print("Not implemented")
    if a == "New album":
      album = raw_input("Whats your album name?: ")
      b = googleobj.create_album(album)
      if b == False:
        print("Sorry, already exists")
        
    if a == "Album list":
      print(googleobj.albums.keys())
      
    if a == "Q":
      sys.exit(0)
