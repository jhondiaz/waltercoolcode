#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

from sqlite3 import *

con = connect("test.db")
cur = con.cursor()
try:
  cur.execute ("create table test( id int, name varchar[256])")
  con.commit()
  print "Creando nueva BDD"
except:
  print "Base de datos ya creada"
cur.execute ("insert into test values(\"pepe\")")
con.commit()
for row in cur.execute ("select * from test"):
  print '|'.join(str(data).ljust(15) for data in row)
cur.close()
con.close()
