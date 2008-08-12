#!/usr/bin/python
import web
urls = ('/(.*)', 'index')
dd = ""
  
class index:
  def GET(self,dd):
    print "<dd>Hello, world!</dd>"
    print "<dd>TT</dd>"
    if dd != "":
      for i in range(1,100):
	print "<dd>",dd, "es gay</dd>"
	
web.webapi.internalerror = web.debugerror
if __name__ == "__main__": web.run(urls, globals())
