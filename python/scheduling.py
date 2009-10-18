#!/usr/bin/python3

listpro = []
listsched = ["FCFS","Round Robin","SJF","A-SJF"] #Supported scheduling
sched = "FCFS" #Default schedule

totalpro = 0 #Number of process... like Linux!
RRHelper = ["4",None] #Default Round Robin Helper = Used quantum, Current process
time = 0 #Thats processor time

#EXTRA FUNCTIONS
def itemfind(f, seq): #Get position from a item on list
  for pos in range( 0,len(seq) ):
    if f == seq[pos]: 
      return pos
  return -1  #I want know if i cant find something too
#END EXTRA FUNCTIONS

class process():
  number = 0
  length = 0
  completed = 0
  name = ""
  quantum = 0

  def __init__(self,number,length):
    self.number = str(number)
    self.length = int(length)
  def add(self): #Add a task
    self.completed+=1
    if self.length == self.completed: #If maxed... return True
      return True
    else:
      return False

def FCFS(): #FCFS scheduling
  existProc = listpro[0]
  if listpro[0].add(): #If process finished
    listpro.pop(0)
    return "Process " + str(existProc.number) + " has been finished!"
  return True
  
def RR(): #Round Robin scheduling... im a bit lost... i must comment all.
  numProc = itemfind(RRHelper[1],listpro) #numProc is Process array number.
  if numProc == -1:
    RRHelper[1] = listpro[0] #Just assign first process if Process fault.
    numProc = 0
  existProc = listpro[numProc] #existProc is current process pointer.
  if RRHelper[1].add(): #If process finished, add data too.
    listpro.pop(numProc)
    if len(listpro) > 0: #Avoid a error with listpro = 0 and listpro[existProc+1] because is not there
      try:  #A small algorithm for change process
        RRHelper[1] = listpro[numProc]
        newProc = numProc+1
      except IndexError:  #If i was on last item... just back to 0
        RRHelper[1] = listpro[0]
        newProc = listpro[0].number

    return "Process " + str(existProc.number) + " has been finished!
  RRHelper[1].quantum+=1
  if RRHelper[1].quantum == int(RRHelper[0]): #If quantum is fully used.
    RRHelper[1].quantum = 0 #Reset quantum
    try:  #Copy/Paste from above algorithm
      RRHelper[1] = listpro[numProc+1]
      newProc = numProc+1
    except IndexError:  
      RRHelper[1] = listpro[0]
      newProc = listpro[0].number
    
    if newProc != existProc.number:
      return "Process " + str(existProc.number) + " quantum maxed... using process " + str(newProc)
  return True
  
def SJF(): #Shortest Job First scheduling
  print("Not implemented")
  return True
  
def ASJF(): #Apropiative Shortest Job First
  print("Not implemented")
  return True
  
def insert(): #Add a process
  global totalpro,listpro
  length = input("Insert length of your process: ")
  listpro.append( process(totalpro,length) )
  print("Process " + str(totalpro) + " added.")
  totalpro+=1
  return True

def remove(): #Remove a process
  x = input("Write process number if you want kill it: ")
  for a in range(0,len(listpro)):
    if x == listpro[a].number:
      print("Process " + listpro[a].number + " deleted.")
      listpro.pop(a)
      return True
  print("I just cant find it...")
  return False
  
def data(): #Show useful data
  global listpro
  print("** Data")
  print("*Sched: " + sched)
  if sched == "Round Robin":
    print("*Round Robin Data: Quantum: " + str(RRHelper[1].quantum) + "/" + RRHelper[0])
  for a in range(0,len(listpro)):
    print("*Process " + listpro[a].number + " on " + str(listpro[a].completed) + "/" + str(listpro[a].length))
  print("")
  return True
  
def changeScheduling(): #Change your current scheduling
  global sched
  if len(listpro) > 0:
    print("* You are going to change a schedule with added process... be aware!")

  print("Supported schedules",listsched)
  s = input("Current scheduling: " + sched + " New scheduling: ")
  if listsched.count(s) > 0:
    sched = s
    if sched == "Round Robin":
      RRHelper[1] = listpro[0]
    print("Using " + sched + " scheduling")
    return True
  else:
    print("Not Supported")
    return False
  
def changeQuantum(): #Change a quantum
  q = input("Current quantum: " + RRHelper[0] + " New quantum: ")
  RRHelper[0] = q
  print("Using a new quantum with value " + RRHelper[0])
  
def help():
  print('*Little help')
  print('--Write "Quit/Exit/Q" for exit')
  print('--Write "Insert/Add" for add a process')
  print('--Write "Delete/Remove/Del" for delete a process')
  print('--Write "Data" if you want details')
  print('--Write "Scheduling/Sched" for scheduling change')
  print('--Write "Quantum/Quan" for quantum change\n')
  return True
  
def main():
  global time, sched
  print("Welcome to Scheduling game!")
  while True:
    sel = input('Current schedule: ' + sched + ', time: ' + str(time) + ', press "h" for help. Command: ').capitalize()
    if sel == "H":
      help()
    elif sel == "Quit" or sel == "Exit" or sel == "Q":
      break
    elif sel == "Insert" or sel == "Add":
      try:
        insert()
      except ValueError:
        print("* Please, just use numbers")
    elif sel == "Delete" or sel == "Remove" or sel == "Del":
      remove()
    elif sel == "Data":
      data()
    elif sel == "Scheduling"or sel == "Sched":
      changeScheduling()
    elif sel == "Quantum" or sel == "Quan":
      changeQuantum()
    elif len(listpro) > 0:
      if sched == "FCFS":
        results = FCFS()
      elif sched == "Round Robin":
        results = RR()
      elif sched == "SJF":
        results = SJF()
      elif sched == "A-SJF":
        results = ASJF()
      else:
        results = "You are bugged! Defaulting to FCFS"
        sched = "FCFS"  
      if results is not True:
        print("* A message from " + sched + ": " +results)
      time+=1
  print("Thanks for use this scheduling game!")
  return True
      
if __name__ == '__main__':
  main()
