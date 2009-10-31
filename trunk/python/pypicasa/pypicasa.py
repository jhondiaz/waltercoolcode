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
import sys, getpass, mimetypes, os, dircache

class pypicasa():
  suppfiles = ["image/jpeg","image/png"]
  def __init__(self):
    self.gclient = gdata.photos.service.PhotosService()
    
  def is_supported(self, photo):
    if os.path.isdir(photo) == True: #Avoid directories
      return False
    imptype = mimetypes.guess_type(photo)[0]
    if self.suppfiles.count(imptype) == 0:
      return False
    return imptype
    
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
    return True
      
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
      desc = raw_input("Add album description. Press q for exit: ")
      if desc.capitalize() == "Q":
        return False
      else:
        self.gclient.InsertAlbum(album, desc)
        self.req_data()
      return True
        
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
    mime = self.is_supported(photo)
    if mime == False:
      print("Non photo or not supported")
      return False
    print("*Uploading " + photo)
    try:
      photo = self.gclient.InsertPhotoSimple(album_url, self.photoToName(photo), desc, photo, mime)
    except socket.gaierror:
      print("Error... retry...")
      self.uploadPicture(album, photo, desc)
    
def help():
  print("\nHelp")
  print("*-Album list: List all your albums")
  print("*-New Album: Add a new album")
  print("*-Upload photo: Add a new photo")
  print("*-Upload folder: Add all your photos on current folder")
      
             
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
        print("Photo not found.\n")
      
    if a == "Upload folder":
      album = raw_input("What album?: ")
      for a in dircache.listdir("."):
        googleobj.uploadPicture(album, a, "")
      print("Folder images uploaded.\n")
      
    if a == "New album":
      album = raw_input("Whats your album name?: ")
      b = googleobj.create_album(album)
      if b == False:
        print("Sorry, already exists")
        
    if a == "Album list":
      print(googleobj.albums.keys())
      
    if a == "Help":
      help()
      
    if a == "Q":
      sys.exit(0)
