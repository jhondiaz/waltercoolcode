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
    #self.s.bind(("", 9999))
    self.s.bind((socket.gethostbyname("localhost"), 9999))
    self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.s.listen(1)
    self.clients = [self.s]
    
  def message(self, cli, addr):
    message = bytes.decode(cli.recv(100))
    cli.send(str.encode("Ok"))
    if message == "q":
      self.clients = []
      return False
    print("Client", addr, "says:", message)
    return True

  def main(self):
    print("Server ready, waiting connections...")
    t = True
    while(t):
      rr,oo,ee = select.select(self.clients,[],[])
      for x in rr:
        if x == self.s:
          cli, addr = self.s.accept()
          self.clients.append(cli)
        else:
          cli, addr = x.getpeername()
          t = self.message(x, addr)
    self.s.close()

a = Multiple()
a.main()
print("Closed")
