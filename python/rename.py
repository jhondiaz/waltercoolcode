#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import dircache,sys,os

if len(sys.argv) < 2:
  print('Usage: rename.py "what you want change" "the real change')
  sys.exit(0)

dir = dircache.listdir(".")
for x in dir:
  loc = x.find(sys.argv[1])
  if loc != -1:
    os.rename(x,x.replace(sys.argv[1],sys.argv[2]))
    
