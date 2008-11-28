#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import sys, os

try:
  imustdir = sys.argv[4]
except:
  pass
  
try:
  directory = sys.argv[1]
  extension = sys.argv[2]
  to = sys.argv[3]
except:
  directory = raw_input("Directory: ")
  extension = raw_input("Extension: ")
  to = raw_input("To: ")
  
try:
  dirlist = os.listdir(directory)
except:
  print directory, "is an invalid directory"
  sys.exit()
  
if directory.find("/") is not len(directory):
  directory = directory + "/"

for x in dirlist:
  ifile = directory + x
  if (os.path.islink(ifile) is False and os.path.isdir(ifile) is False):
    result = x.find(extension)
    expected = directory + x[:result] + to
    if result is not -1:
      os.rename(ifile, expected)
    
