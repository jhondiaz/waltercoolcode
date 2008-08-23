#!/usr/bin/python
import web
from web.contrib.template import render_cheetah

valido = 0
urls = ('/', 'index', '/main', 'main', '/insert', 'insert')
db = web.database(dbn='sqlite', db='test.db')
render = render_cheetah('templates/')

class index:
  def GET(self):
    return render.login(error = '')
    
  def POST(self):
    params = web.input()
    login = db.select('users')
    for x in login:
      if params.loguser == x.user:
	if params.logpasswd == x.passwd:
	  globals() ['valido'] = 1
	  
    if globals() ['valido'] == 1:
      return web.seeother('/main')
    else:
      error = 'Usuario o clave invalida'
      return render.login(error = error)
 
class main:
  def GET(self):
    if globals() ['valido'] == 0:
      return web.seeother('/')
    pepejuanydiego = db.select("test")
    return render.test(pepejuanydiego = pepejuanydiego)
  
  def POST(self):
    print "hola"
    
class insert:
  def GET(self):
    if globals() ['valido'] == 0:
      return web.seeother('/')
    return render.first()
    
  def POST(self):
    params = web.input()
    error = ""
    try:
      value = db.insert('test', name = params.nombres)
    except OperationalError:
      error = "Error insertando datos"
      return render.test(error = error)
    web.seeother('/main')

if __name__ == "__main__":
  app = web.application(urls,globals())
  app.run()
