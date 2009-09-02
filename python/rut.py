#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Developed by WalterCool! under GPL-2 License
# Feel free of modify (using GPL-2 rules) or reporting bugs
# mailto: waltercool [at] slash [dot] cl
# http://www.slash.cl
#
# This code is a bit bigger than 1st instance, for obvious reasons (ifs and function)

def rut(rut):
  while len(rut) < 8: rut = '0' + rut
  temp = int(rut[0]) * 3 + int(rut[1]) * 2 + int(rut[2]) * 7 + int(rut[3]) * 6 + int(rut[4]) * 5 + int(rut[5]) * 4 + int(rut[6]) * 3 + int(rut[7]) * 2
  temp = (temp%11 -11) * -1
  if temp == 10: return('K')
  elif temp == 11: return('0')
  else: return(temp)

if __name__ == '__main__':
  print( rut( input('Ingrese un rut: ') ) )

