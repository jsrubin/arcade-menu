from Tkinter import *

class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button1 = Button(frame, 
                         text="Hello",
                         command=self.run_ssft2)
    self.photo1=PhotoImage(file="ssft2.gif")
    self.button1.config(image=self.photo1)
    self.button1.grid(row=0, column=0)
    self.button2 = Button(frame,
                         text="Hello",
                         command=self.run_simpsons)
    self.photo2=PhotoImage(file="simpsons.gif")
    self.button2.config(image=self.photo2)
    self.button2.grid(row=0, column=1)
    self.button3 = Button(frame, 
                         text="Hello",
                         command=self.run_tmnt)
    self.button3.grid(row=1, column=0)
    self.photo3=PhotoImage(file="tmnt.gif")
    self.button3.config(image=self.photo3)
    self.button4 = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button4.grid(row=1, column=1)

  def run_ssft2(self):
    print "Starting Super Street Fighter 2!"

  def run_simpsons(self):
    print "Starting Simpsons!"

  def run_tmnt(self):
    print "Starting Teenage Mutant Ninja Turtles!"

root = Tk()
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

app = App(root)
root.mainloop()