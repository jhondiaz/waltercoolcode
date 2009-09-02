#!/usr/bin/python3
# -*- coding: utf-8 -*-

rut = input('Ingrese su rut: ')
while len(rut) < 8: rut = '0' + rut
temp = int(rut[0]) * 3 + int(rut[1]) * 2 + int(rut[2]) * 7 + int(rut[3]) * 6 + int(rut[4]) * 5 + int(rut[5]) * 4 + int(rut[6]) * 3 + int(rut[7]) * 2 
print((temp%11 -11) * -1)
