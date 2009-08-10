#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("",9999))

while True:
  message = input("Message: ")
  mail = str.encode(message)
  s.send(mail)
  confirmation = bytes.decode(s.recv(10))
  if confirmation == "Ok": print("Sent")
  else:
    print("Server down. Disconnected")
    break
  if message == "quit": break
s.close()
