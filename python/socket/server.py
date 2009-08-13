#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#

import socket,time, select, sys

class Multiple():
  def __init__(self):
    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.s.bind((socket.gethostbyname("localhost"), 9999))
    self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.s.listen(1)
    self.clients = [self.s]
    self.nicks = {}

  def recive_simple(self):
    message = self.s.recv(100)
    return bytes.decode(message)

  def conf_simple(self,cli, conf):
    if conf is True:
      cli.send(str.encode("Ok"))
    else:
      cli.send(str.encode("No"))
    return True

  def recive(self,cli):
    message = self.s.recv(100)
    conf = str.encode("Ok")
    cli.send(conf)
    return bytes.decode(message)

  def login(self):
    cli, addr = self.s.accept()
    username = self.recive_simple()
    if self.nicks.values().count(username) == 0: #If user is not on dict
      self.conf_simple(cli,True)
      self.nicks[addr[0]] = username #Add it
      self.clients.append(cli)
    else:
      conf_simple(cli,False) #Else, say no
  def message(self, cli, addr):
    message = recive(cli)
    if message == "q":
      self.clients = []
      return False
    print("Client", addr, "says:", message)
    return True

  def main(self):
    try:
      print("Server ready, waiting connections...")
      t = True
      while(t):
        rr,oo,ee = select.select(self.clients,[],[])
        for x in rr:
          if x == self.s:
            self.login()
          else:
            cli, addr = x.getpeername()
            t = self.message(x, cli + ":" + str(addr))
    except:
      self.s.close()
      raise
    self.s.close()
a = Multiple()
a.main()
print("Closed")
