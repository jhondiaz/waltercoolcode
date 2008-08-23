#/usr/bin/python
import web 

urls = ('/(.*)', 'hello') 

class hello: 
	def GET(self, name): 
		i = web.input(times=1) 
		if not name: name = 'world' 
		web.render('hello.html') 


if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()
