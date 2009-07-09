#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, shutil, os
if os.popen("groups").read().find("root") is -1:
  print "You need root permissions if you want run this application"
  sys.exit(1)
kamversion = "2.7.3"
if sys.platform == "darwin" or sys.platform == "win32" or sys.platform == "freebsd6":
  print("Instalation not known for OSX, Windows or FreeBSD")
  sys.exit(1)
if sys.version.find("2.6") is 0:
  version = "python2.6"
elif sys.version.find("2.5") is 0:
  version = "python2.5"

dirpy = "/usr/lib/" + version + "/site-packages/kamlib" 

if sys.argv.count("install") > 0:
  try:
    os.mkdir(dirpy)
  except:
    pass
  try:
    shutil.copy("__init__.py", dirpy)
    shutil.copy("methods.py", dirpy)
    shutil.copy("weblib.py", dirpy)
    shutil.copy("kamiltube.py","/usr/bin/kamiltube.py")
    print("Kamiltube " + kamversion + " installed")
  except:
    print("Error installing kamiltube, please check again your disk space or copy problem")
  sys.exit(1)
elif sys.argv.count("uninstall") > 0:
  try:
    os.unlink("/usr/bin/kamiltube.py")
    shutil.rmtree(dirpy)
  except OSError:
    pass
  print("Kamiltube " + kamversion + " uninstalled, remember, you must be root for delete it")
else:
  print("Kamiltube Setup. For Linux only")
  print("Usage:\n  python setup.py install: Install Kamiltube on your system")
  print("  python setup.py uninstall: Uninstall Kamiltube on your system")
