#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import dircache,sys,os

dir = dircache.listdir(".")

if len(sys.argv) < 2:
  print('Usage: rename.py "what you want change" "the real change')
  print('Using rename.py "" "change" you will add changeFILE1, changeFILE2...')
  sys.exit(0)
if sys.argv[1] == "":
  y = raw_input('Are you sure... you will append ' + sys.argv[2] + ' on all files. Y/n:').capitalize()
  if y == "N":
    sys.exit(0)
  else:
    for x in dir:
      os.rename(x,sys.argv[2] + x)
else:
  for x in dir:
    loc = x.find(sys.argv[1])
    if loc != -1:
      os.rename(x,x.replace(sys.argv[1],sys.argv[2]))
    
