#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

from pylab import *

theta = arange(0,2*pi,0.1)
polar(theta, 2*pi*theta)
savefig("asd")
