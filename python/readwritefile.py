#!/usr/bin/python
try:
  filetest = file("asd",'rw+')
  filetest.write("hola")
  filetest = file("asd", "r")
  filetest.read()
  print "" 
except IOError:
  print("Bastardo! El archivo asd no existe!")

