#!/usr/bin/python
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

a = 0.0
b = 0
print "PyWalterCool Benchmark"
def task():
	global a,b
	while(b==0):
		sin(2*pi*e*a)
		a += 1




t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t3 = threading.Thread(target=task)
t4 = threading.Thread(target=task)

print "Eins Zwei Drei Vier!"
t1.start()
t2.start()
t3.start()
t4.start()
time.sleep(3)
b = 1

t1.join()
t2.join()
t3.join()
t4.join()

print "Finished!"
print "Tu PyWalterCool Benchmark es de: ", round(a*2/1000000,3)
