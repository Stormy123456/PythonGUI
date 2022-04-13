# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, Image


win = Tk()

win.geometry("700x350")

def on_click():
   # label.after(1000, label.destroy())
   label1.destroy()
   label.destroy()

label1 = Label(text="Hello",font=20)
label1.pack()
label = Label(win, text=" Deleting a Label in Python Tkinter", font=('Helvetica 15'))
label.pack(pady=20)

ttk.Button(win, text="Delete", command=on_click).pack()

win.mainloop()