#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import threading
from math import *
import time

b = 0
x = []
aver = 0
threads = 11
print("PyWalterCool Benchmark")
class task(threading.Thread):
  def run(self):
    self.data = 0
    global a,b
    while(b == 0):
      sin(2*pi*e*self.data)
      self.data += 1.0

  def finish(self):
    return self.data/1000

print("Eins Zwei Drei Vier!")
for a in range(threads):
  x.append( task() )
  x[a].start() 
time.sleep(3)
b = 1
for a in range(threads):
  x[a] = x[a].finish()
  aver += x[a]
print ("Finished!")
x.sort()
print("Your PyWaltercool MAX:", max(x), 'MIN:', min(x), 'AVERAGE:',aver/threads)
