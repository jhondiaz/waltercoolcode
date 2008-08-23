# encoding: utf-8
# File: code.py

import web
import render_cheetah
render = render_cheetah('templates/')
urls = (
    '/(first)', 'first',
    '/(second)', 'second'
    )

app = web.application(urls, globals(), web.reloader)

class first:
    def GET(self, name):
        # cheetah template takes only keyword arguments,
        # you should call it as:
        #   return render.hello(name=name)
        # Below is incorrect:
        #   return render.hello(name)
        return render.first(name=name)

class second:
    def GET(self, name):
        return render.first(**locals())

if __name__ == "__main__":
    app.run()