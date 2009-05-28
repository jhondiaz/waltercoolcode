#!/usr/bin/python

import sys, shutil, os
version = "2.7.3 Beta 2"

if sys.platform == "darwin" or sys.platform == "win32" or sys.platform == "freebsd6":
  print("Instalation not known for OSX, Windows or FreeBSD")
  sys.exit(1)
if sys.version.find("2.6") is 0:
  version = "python2.6"
elif sys.version.find("2.5") is 0:
  version = "python2.5"
if sys.argv.count("install") > 0:
  shutil.copy("kamlib.py", "/usr/lib/" + version + "/site-packages")
  shutil.copy("kamiltube.py","/usr/bin/kamiltube.py")
  print("Kamiltube " + version + " installed")
  sys.exit(1)
elif sys.argv.count("uninstall") > 0:
  try:
    os.unlink("/usr/lib/" + version + "/site-packages/kamlib.py")
    os.unlink("/usr/bin/kamiltube.py")
  except OSError:
    pass
  print("Kamiltube " + version + " uninstalled, remember, you must be root for delete it")
else:
  print("Kamiltube Setup. For Linux only")
  print("Usage:\n  python setup.py install: Install Kamiltube on your system")
  print("  python setup.py uninstall: Uninstall Kamiltube on your system")
