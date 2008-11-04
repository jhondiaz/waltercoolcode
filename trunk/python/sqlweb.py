#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import web
urls = ('/', 'index')
db = database(dbn='sqlite', db='test.db')
web.webapi.internalerror = web.debugerror

def head():
  print "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">"
  print "<html xmlns=\"http://www.w3.org/1999/xhtml\">"
  print "<head>"
  print "<title>Título</title>"
  print "<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\" />"
  print "</head>"
  print "<body>"
  
def end():
  print "</body>"
  print "</html>"

class index:
  def GET(self):
    head()
    #row = cur.execute("select * from test")
    print "<dl>"
    print "<dd>All working sir</dd>"
    resultset = db.query('test')
    print resultset
    print "<input type='text' name='prueba' />"
    print "<form action=asdf.html><input type=submit value=\"Click Me\" /></form>"
    print "</dl>"
    end()
      
if __name__ == "__main__": web.run(urls, globals())
