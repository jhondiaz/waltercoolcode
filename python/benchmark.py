#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import threading
import math
import time

b = 0
threads = 4

print("PyWalterCool Benchmark")
class task(threading.Thread):
  def run(self):
    sin = math.sin
    pi = math.pi
    e = math.e
    self.data = 0
    while(True):
      sin(2*pi*e*self.data)
      self.data += 1.0

  def finish(self):
    return self.data/1000

class bench():
  x = []
  running = 0
  def start(self):
    self.x = []
    self.running = 0
    for a in range(threads):
      self.x.append( task() )
      self.running+=1
      self.x[a].start()
    
  def stop(self):
    aver = 0
    for a in range(self.running):
      self.x[a] = self.x[a].finish()
      aver += self.x[a]
    return aver
      
if __name__ == '__main__':
  ben = bench()
  try:
    while True:
      ben.start()
      time.sleep(3)
      aver = ben.stop()
      ben.x.sort()
      print(("Your PyWaltercool MAX:", max(ben.x), 'MIN:', min(ben.x), 'AVERAGE:',aver/threads))
  except KeyboardInterrupt:
    ben.stop()
  except:
    ben.stop()
    raise
