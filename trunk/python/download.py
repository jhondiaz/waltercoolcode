#!/usr/bin/python

import urllib, urllib2

def hook(bN, bS, tS):
  print "%s of %s" % (bN*bS, tS)

link = raw_input("Insert the url: ")
file = raw_input("With the name: ")
file = open(file,"w+")
urllib.urlretrieve(link, file, hook)
print "Complete!"
