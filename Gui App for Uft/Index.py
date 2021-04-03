from tkinter import *
from tkinter import ttk

#new window created
class main_window():
  ###########error
  def __init__(self, root):
    root.title("UFT")
    root.geometry("300x300")
    def file_opener():
      Input1 = Entry().pack()
      file = open(Input1, "r")
      for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
   ##########error   
    Welcome = Label(text='Files To uft format ').pack()
    BTN1 = Button(root, text='Choose File', command = file_opener).pack()
    BTN2 = Button(root, text="Convert").pack()

def main():
  root1 = Tk()
  main_window(root1)


main()



# Instead of this we can also do this
from tkinter import *
from tkinter import ttk

class main_window():
  def __init__(self, root):
    #ok here is the root window fonts
    root.title("UFT")
    def file_opener():
      Input = Entry().pack()
      file = open(Input1,"r")
      #here the file opens but we need to make it in uft format also i dont know how but it should also hold muilti files we can combine into one file.
    btn1 = Button(text="openfile", Command=file_opener)
def main():
  root = Tk()
  main_window(root)



