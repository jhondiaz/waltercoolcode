#!/usr/bin/python

from pylab import *

a = arange(0,2*pi,0.1)
polar(a, cos(2*a))
savefig("asd")
