#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import socket

class client():
  def __init__(self):
    try: 
      while True:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("",9999))
        a = self.send("Nick: ")
        if a:
          print("Logged as",message)
        else:
          self.s.close()
    except:
      raise
    print("Connected")

  def send(self,question): 
    message = input(question)
    mail = str.encode(message)
    self.s.send(mail)
    message = self.s.recv(2)
    if message == "Ok":
      return True
    return False

  def recive(self):
    message = self.s.recv(100)
    return bytes.decode(message)

  def main(self):
    while True:
      a = send("Message")
      if a: print("Sent")
      else:
        print("Server down. Disconnected")
        break
      if message == "quit": break
    s.close()

a = client()
a.main()
