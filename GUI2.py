from tkinter import *
import tkinter.messagebox

# หน้าจอที่ 1
root = Tk()
root.title("My GUI")
root.geometry("500x400+700+300")

# สร้างเมนู
mainMenu = Menu()
root.config(menu=mainMenu)

# สร้างหน้าต่างใหม่
def  showWindown():
    window = Tk()
    window.title("New Windown")
    window.geometry("200x200+850+400")
    window.mainloop()

def aboutProgram():
    tkinter.messagebox.showinfo("Message!","Developed by Stormy")

def exitProgram():
    confirm = tkinter.messagebox.askquestion("Confirm Message!","Are you sure about close program ?")
    if confirm =="yes":
        root.destroy()

# เพิ่มเมนูย่อย
menuItem = Menu()
menuItem.add_command(label="New File",command = showWindown)
menuItem.add_command(label="Open File")
menuItem.add_command(label="Save File")
menuItem.add_command(label="About",command=aboutProgram)
menuItem.add_command(label="Exit",command=exitProgram)
# เพิ่มเมนูหลัก
mainMenu.add_cascade(label="File",menu=menuItem)
mainMenu.add_cascade(label="Edit")
mainMenu.add_cascade(label="View")

root.mainloop()