from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import  *

root = Tk()
root.title("My GUI")
root.geometry("500x400+700+300")

def selectColor():
    color = askcolor()
    print(color[1])
    myLabel = Label(text="Hello Python",bg=color[1]).pack()

def selectFile():
    color = color[1]
    fileopen = askopenfilename()
    fileContent = open(fileopen,encoding="utf8")
    myLabel = Label(text=fileContent.read()).pack()
    return myLabel


button1 = Button(text="เลือกสี",command=selectColor).pack()
button2 = Button(text="เลือกไฟล์",command=selectFile).pack()
root.mainloop()