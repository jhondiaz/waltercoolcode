# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# If you run this file directly... your life will not change ;)
#
# Just another dammed dependence =)

import sys,os,time,urllib

class detect():
  def __init__(self):
    mp, totem = self.os_det()
    self.gui = self.gui_det()
    self.player = self.player_det(mp, totem)
  
  def os_det(self):
    os = sys.platform
    if os == 'darwin':
      mproute = '/Applications/mplayer/mplayer'
      totemroute = ''
    elif os == 'linux2':
      mproute = '/usr/bin/mplayer'
      totemroute = '/usr/bin/totem'
    else:
      mproute = ''
      totemroute = ''
    return mproute, totemroute
     
  def gui_det(self):
    data = list()
    try:
      import gtk
      data.append('Gtk')
    except ImportError:
      pass
    try:
      import PyQt4.QtCore, PyQt4.QtGui
      data.append('Qt4')
    except ImportError:
      pass
    try:
      import Tkinter, tkMessageBox
      data.append('Tk')
    except ImportError:
      pass
    return data
  
  def player_det(self,mproute, ttroute):
    data = list()
    if os.path.exists(mproute) is True:
      mpsup = list()
      d = 0
      a = os.popen(mproute + ' -vc help')
      for x in a:
        if x.rfind('ffflv') > -1: #FLV codec
          mpsup.append('flv')
        elif x.rfind('ffh264') > -1: #H264 codec
          mpsup.append('h264')
        elif x.rfind('ffvp6f') > -1: #VP6 Flash
          mpsup.append('vp6f')
      b = os.popen(mproute + " -ac help")
      for x in b:
        if x.rfind('mp3') > -1: #MP3 audio for FLV
          mpsup.append('mp3')
        elif x.rfind('faad') > -1: #FAAD audio for H264
          mpsup.append('faad')
                
      if mpsup.count('flv') > 0 and mpsup.count('mp3') > 0 and mpsup.count('vp6f'): 
        d+=1
      if mpsup.count('h264') > 0 and mpsup.count('faad') > 0:
        d+=1
      if d == 2:
        data.append('mplayer')
      elif d == 1:
        data.append('limplayer')
        
    if os.path.exists(ttroute) is True:
      data.append('totem')
    return data

class work():
  def __init__(self):
    start = detect()
    self.gui = start.gui
    self.player = start.player
    
  def play(self,video):
    if player == 'mplayer':
      print()
    return True
    
  def download(self, video, savepath):
    urllib.urlretrieve(video,savepath)
    return True
    

