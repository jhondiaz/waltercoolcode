#!/usr/bin/env python

import threading

class thread(threading.Thread):
  def __init__(self, event):
    threading.Thread.__init__(self)
    self.event = event
    
  def run(self):
    print self.getName(), "waiting"
    self.event.wait()
    print self.getName(), "ending"
    
event = threading.Event()
t1 = thread(event)
t2 = thread(event)
t1.start()
t2.start()

event.set()