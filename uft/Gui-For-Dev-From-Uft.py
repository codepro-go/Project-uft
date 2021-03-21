from tkinter import *
from tkinter import ttk

#new window created
class main_window():
  def __init__(self, root):
    root.title("UFT")
    root.geometry("300x300")
    def file_opener():
      Input1 = Entry().pack()
      file = open(Input1, "r")
      
    Welcome = Label(text='Files To uft format ').pack()
    BTN1 = Button(root, text='Choose File', command = file_opener).pack()
    BTN2 = Button(root, text="Convert").pack()

def main():
  root1 = Tk()
  main_window(root1)


main()
