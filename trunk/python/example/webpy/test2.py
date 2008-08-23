#!/usr/bin/env python
import web, os

#for the templates
os.chdir('.') 

urls = (
  '/all', 'all',
  '/(\d+)', 'show',
  '/', 'view',
  '/(\d\d\d\d\-\d\d)', 'month'
)

web.db_parameters = dict(dbn='sqlite', db='/mnt/cvs/SABS.db')
web.internalerror = web.debugerror

class view:
    def GET(self):
        tickets = web.query("SELECT * FROM ticket WHERE (owner='kg') OR (extra1='KG')")
        name = "All %d tickets" % len(tickets)
        #print tickets
        web.render('view.html')

class all:
    def GET(self):
        tickets = web.query("""SELECT
                            t.tn AS '#',
                            e.value AS 'Type'
                            FROM enums e, ticket t
                            WHERE e.type='type'
                            AND e.name=t.type
                            AND (owner='kg')
                            """)
        name = "All %d tickets" % len(tickets)
        #print tickets
        web.render('squeel.html')

class show:
    def GET(self, name):
        # Could do some checking
        # tns = web.query("SELECT tn FROM ticket")
        tickets = web.query("SELECT * FROM ticket WHERE tn = %d" % int(name))
        name = "Ticket detail : %d" % int(name)
        web.render('view.html')

class month:
    def GET(self, name):
        year, month = name.split('-')
        name = "Tickets upto month: %s" % name
        #if not month in range(1,13) or year not in range(2004,2010):
        #    raise view
        tickets = web.query("""SELECT * FROM ticket
                               WHERE status IN ('new','active') 
                               AND origtime<= %d 
                               AND (owner='kg')""" % self.parsedate(year, month))
        #print tickets
        web.render('view.html')

    def parsedate(self, year, month):
        # Beginning of the month is easy, end of the month not so
        import time
        return time.mktime(time.strptime('%d-%d-01 00:00' % (int(year), int(month)), "%Y-%m-%d %H:%M"))

if __name__ == '__main__': web.run(urls, web.reloader)