#!/usr/bin/env python

import threading, time, random

t = list()
def event(asdf):
    print "waiting, ", asdf
    time.sleep(random.random()*100+1)
    print "ending, ", asdf

for i in range(99):
	t.append (threading.Thread(target=event, args=(i,)))

for i in range(99):
	t[i].start()

