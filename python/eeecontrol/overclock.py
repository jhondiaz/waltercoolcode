#!/usr/bin/python3
import sys,time
FSB = '/proc/eee/fsb'

try:
  filebuffer = open(FSB, 'r+')
  param = sys.argv[1] #If something...
except IndexError:
  param = ''
except:
  raise

def reverse_lookup(d, v):
  for k in d:
    if d[k] == v:
      return k
  raise ValueError

def set(value): #Save it!
  filebuffer.seek(0)
  filebuffer.write(value)
  time.sleep(1) #Avoid corruption

def reach(objective, current, disi):
  if current < objective: #If less
    while current < objective:
      set( reverse_lookup(disi, current+1) )
      current += 1
  elif current > objective: #If greater
    while current > objective:
      set( reverse_lookup(disi, current-1) )
      current -= 1
  print('Now on ' + reverse_lookup(disi,current))
  return True

def menu(current):
  print('Current: ', current)
  print('1) Low')
  print('2) Normal')
  print('3) High')
  print('4) Very High')
  print('5) Exit')
  value = input('Choose: ')
  if value == '5':
    sys.exit(1)
  elif value == '4':
    value = 5
  elif value == '3':
    value = 4
  return int(value)

def main():
  global param
  disi = {'40 24 0\n':0, '60 24 0\n':1, '70 24 0\n':2, '85 24 0\n':3, '100 24 1\n':4, '105 24 1\n':5}
  current = disi[filebuffer.readline()] #Read the current value
  if param == 'menu':
    param = menu(current)
  else:
    if current is 2:
      param = 4
    else:
      param = 2

  ready = reach(param,current,disi)
  return ready

if __name__ == '__main__':
  main()
