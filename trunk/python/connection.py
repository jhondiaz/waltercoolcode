#!/usr/bin/python
# -*- coding: utf-8 -*-
#from pysqlite2 import dbapi2 as sqlite
import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()
try:
  cur.execute ("create table test( id int, name varchar[256])")
  con.commit()
  print "Creando nueva BDD"
except:
  print "Base de datos ya creada"
cur.execute ("insert into test values(1,\"pepe\")")
con.commit()
for row in cur.execute ("select * from test"):
  print '|'.join(str(data).ljust(15) for data in row)
cur.close()
con.close()