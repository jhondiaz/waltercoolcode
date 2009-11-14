    
def messages(message,title): #Messages
  if debugMode == True:
    print("Im on messages method")
  global gui
  if gui is "PyQt4":
    QMessageBox.information(None ,title,message)
  elif gui is "Tk":
    tkMB.showinfo(title, message)
  elif gui is "Gtk":
    d = gtk.MessageDialog(parent=defgui,buttons=gtk.BUTTONS_CLOSE, message_format=message)
    d.run()
    d.destroy()
  else:
    print("* " + message)
  return True


def login(video):
  if debugMode == True:
    print("Im on login method")
  if gui is "PyQt4": #A login with Qt4 GUI
    global mail, passw
    #Objects
    login = QDialog()
    login_mailtext = QLabel("Email:")
    login_mail = QLineEdit(mail)
    login_passtext = QLabel("Password:")
    login_passw = QLineEdit()
    login_passw.EchoMode = 2
    login_Ok = QPushButton("Ok")
    login_cancel = QPushButton("Cancel")
    login_grid = QGridLayout()
  
    #Connection to grid
    login_grid.addWidget(login_mailtext,0,0)
    login_grid.addWidget(login_mail,0,1)
    login_grid.addWidget(login_passtext,1,0)
    login_grid.addWidget(login_passw,1,1)
    login_grid.addWidget(login_Ok,2,0)
    login_grid.addWidget(login_cancel,2,1)
    login.setLayout(login_grid)
    
    #Method
    def accept():
      global mail, passw
      mail = login_mail.text()
      passw = login_passw.text()
      if mail != "" and passw != "":
	      login.close()
	      return work(video)
      
    #Signals
    login.connect(login_Ok, SIGNAL("clicked()"), accept)
    login.connect(login_cancel, SIGNAL("clicked()"), SLOT("close()") )
    
    #Options and execution
    login_passw.setEchoMode(2)
    login.setWindowTitle("NicoLogin")
    login.show()
    login.exec_()

  elif gui is "Gtk": #A login with GTK GUI
    #Method
    def accept(widget):
      global mail, passw
      mail = login_mail.get_text()
      passw = login_passw.get_text()
      if mail != "" and passw != "":
	      login.destroy()
	      return work(video)
    def close(widget):
      login.destroy()

    #Objects
    login = gtk.Window()
    layout = gtk.Table(2,3,True)
    login_mailtext = gtk.Label()
    login_mail = gtk.Entry()
    login_passtext = gtk.Label()
    login_passw = gtk.Entry()
    login_Ok = gtk.Button("Ok")
    login_cancel = gtk.Button("Cancel")
    
    #Grid
    layout.attach(login_mailtext,0,1,0,1)
    layout.attach(login_mail,1,2,0,1)
    layout.attach(login_passtext,0,1,1,2)
    layout.attach(login_passw,1,2,1,2)
    layout.attach(login_Ok,0,1,2,3)
    layout.attach(login_cancel,1,2,2,3)

    #Options and Run
    login_Ok.connect("clicked",accept)
    login_cancel.connect("clicked",close)
    login.connect("destroy", gtk.main_quit)
    login_mailtext.set_text("Email:")
    login_mail.set_text(mail)
    login_passtext.set_text("Password:")
    login_passw.set_visibility(False)
    login.add(layout)
    login.show_all()
    gtk.main()

  elif gui is "Tk": #A login with Tk GUI
    #Method
    def accept(*args):
      global mail, passw
      mail = login_mail.get()
      passw = login_passw.get()
      if mail != "" and passw != "":
	      login.destroy()
	      return work(video)
	
    #Objects
    login = Tk.Toplevel()
    login_mailtext = Tk.Label(login, text="Email:")
    login_passtext = Tk.Label(login, text="Password:")
    login_mail = Tk.Entry(login)
    login_passw = Tk.Entry(login, show="*")
    login_Ok = Tk.Button(login, text="Ok", command=accept)
    login_cancel = Tk.Button(login, text="Cancel", command=login.destroy)
    
    #Connection to grid    
    login_mailtext.grid(row=0)
    login_passtext.grid(row=1)
    login_mail.grid(row=0, column=1)
    login_passw.grid(row=1, column=1)
    login_Ok.grid(row=2)
    login_cancel.grid(row=2, column=1)
    
    #Options and execution
    login_mail.focus()
    login.bind("<Return>", accept)
    login.mainloop()
  else: #A login without GUI
    while mail == "" or passw == "":
      mail = raw_input("\nEmail: ")
      passw = getpass.getpass(prompt="Password: ")
      return work(video)
  return False
    
def guiPyQt4(): 
  from PyQt4.QtCore import SIGNAL, SLOT
  from PyQt4.QtGui import QDialog, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
  app = QApplication(sys.argv)
  widget = QWidget()
  if debugMode == True:
    print("Im using PyQt4 mode")
  
  #Objets
  label = QLabel(deflabel)
  box = QLineEdit(defvid)
  button = QPushButton("&Watch it!")

  #Layouts
  grid = QGridLayout()
  grid.addWidget(label,0,0)
  grid.addWidget(box,1,0)
  grid.addWidget(button,1,1)
  widget.setLayout(grid)
  
  #Methods
  def gotowork():
    if box.text() != "": work(str(box.text()))
    
  #Signals and others!
  widget.connect(button, SIGNAL("clicked()"), gotowork)
  box.selectAll()
  widget.setWindowTitle(deftit)
  widget.show()
  defgui = app
  app.exec_()

def guiGtk():
  import gtk
  if debugMode == True:
    print("Im using Gtk mode")

  #Methods
  def gotowork(widget):
    if box.get_text() != "":
      video = box.get_text()
      work(video)
  #Objects
  app = gtk.Window()
  label = gtk.Label()
  box = gtk.Entry()
  button = gtk.Button("Watch It")

  #Layouts
  layout = gtk.Table(2,2,True)
  layout.attach(label, 0,1,0,1)
  layout.attach(box,1,2,0,1)
  layout.attach(button,1,2,1,2)

  #Signals and others!
  button.connect("clicked",gotowork)
  label.set_text(deflabel)
  box.set_text(defvid)

  app.connect("destroy", gtk.main_quit)
  app.add(layout)
  app.set_title(deftit)
  app.set_size_request(350, 50)
  app.show_all()
  defgui = app
  gtk.main()

def guiTk():
  import Tkinter as Tk
  import tkMessageBox as tkMB
  
  if debugMode == True:
    print("Im using Tk mode")
  global defgui
  #Methods
  def gotowork(*args):
    if box.get() != "":
      video = box.get()
      work(video)
      
  #Objets
  root = Tk.Tk()
  frame = Tk.Frame(root)
  label = Tk.Label(frame, text=deflabel)
  box = Tk.Entry(frame)
  button = Tk.Button(frame, text="Watch It!", command=gotowork)
  #Layouts
  label.grid(row=0)
  box.grid(row=1)
  button.grid(row=1, column=1)
  #Signals and others!
  root.title(deftit)
  root.minsize(350,50)
  box.insert(0, defvid)
  box.select_range(0, Tk.END)
  box.focus()
  box.bind("<Return>", gotowork)
  frame.pack()
  defgui = root
  root.mainloop()
  
def console(): #Console only.
  if debugMode == True:
    print("Im using console mode")
  while True:
    print("\nWrite exit for quit of the application\n")
    video = raw_input("Video Address: ")
    if (video == "exit" or video == "quit" or video == "q"):
      break
    elif (len(video) == 0):
      pass
    else:
      try:
        work(video)
      except:
	raise

def bashmode(): #Method for std input
  sys.argv.reverse()
  sys.argv.pop()
  sys.argv.reverse()
  if debugMode == True:
    print("Using bashmode")
  for video in sys.argv:
    try:
      work(video)
    except:
      raise

