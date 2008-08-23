#!/usr/bin/env python
 
import web
 
# For debugging use only
web.internalerror = web.debugerror
 
urls = (
    '/', 'index',
    '/login', 'login',
    '/logout', 'logout',
    '/add', 'add',
    '/view/(\d+)', 'view',
    '/edit/(\d+)', 'edit',
    '/edit', 'edit',
    '/comment', 'comment',
    '/styles.css', 'style',
    '/view/styles.css', 'style',
)
 
class index:
    def GET(self):
        post = web.query("select id, title, body, (select count(*) from comment where post_id = post.id) as total_comment from post;")
        web.render('index.html')
 
class add:
    def GET(self):
        session = web.cookies()
 
        web.render('add.html')
 
    def POST(self):
        input = web.input()
        n = web.insert('post', title=input.post_title, body=input.post_body)
        web.redirect('./view/'+str(n))
 
class view:
    def GET(self, post_id):
        post = web.query("select * from post where id = $post_id", vars=locals())
        comment = web.query("select * from comment where post_id = $post_id", vars=locals())
        web.render('view.html')
 
class edit:
    def GET(self, post_id):
        post = web.query("select * from post where id = $post_id", vars=locals())
        web.render('edit.html')
 
    def POST(self):
        input = web.input()
        n = web.update('post', int(input.post_id), title=input.post_title, body=input.post_body)
        web.redirect('./view/'+str(n))
 
class comment:
    def POST(self):
        input = web.input()
        n = web.insert('comment', username=input.post_username, body=input.post_body, post_id=input.post_id)
        web.redirect('./view/'+input.post_id)
 
class login:
    def POST(self):
        i = web.input()
        result = web.query(  \
            "select * \
                from members \
                where username = '$username' \
                and password = '$password'", vars=i) \
 
        if len(result) > 0:
            login = 'login success !'
            web.setcookie('id', result[0].id)
            web.setcookie('username', result[0].username)
        else:
            login = 'wrong user name or password'
        web.render('login.html')
 
class logout:
    def GET(self):
        web.setcookie('id', '', 'Mon, 01-Jan-2001 00:00:00 GMT')
        web.setcookie('username', '', 'Mon, 01-Jan-2001 00:00:00 GMT')
        web.render('logout.html')
 
class style:
    def GET(self):
        web.header("Content-Type","text/css; charset=utf-8")
        print open('templates/style.css').read()
 
if __name__ == "__main__":
    #web.db_parameters = dict(dbn='postgres', user='kamal', pw='any', db='webpy')
    web.db_parameters = dict(dbn='sqlite', db='test.db')
    web.run(urls, web.reloader)