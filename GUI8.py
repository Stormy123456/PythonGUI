from tkinter import *
from tkinter import ttk

root = Tk()
root.title("My GUI")
root.geometry("500x400+700+300")

Label(text="ที่อยู่",font=20).grid(row=0,column=0)
choice = StringVar(value="เลือกจังหวัด")
combo=ttk.Combobox(textvariable=choice)
combo["values"]=("กรุงเทพ","นนทบุรี","สมุทรสาคร","ปถุมธานี")
combo.grid(row=0,column=1)

def selectCity():
    label2 = Label(text="คุณได้เลือก = "+choice.get(),font=20)
    label2.grid(row=2,column=1)

button1 = Button(text="ส่งข้อมูล",command=selectCity)
button1.grid(row=1,column=1)

root.mainloop()