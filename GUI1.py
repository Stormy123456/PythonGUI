from tkinter import *

# หน้าจอที่ 1
root = Tk()
root.title("My GUI")
root.geometry("500x400+700+300") # กำหนดขนาดหน้าจอ



# ใส่ข้อความ
myLabel = Label(root,text="Welcome !",fg="red",font=20,bg="yellow").pack()
# myLabel2 = Label(root,text="Stormy",fg="green",font=20,bg="pink").pack()

def showMessage():
    message = txt.get()
    Label(root,text=message,fg="white",font=20,bg="black").pack()

def openWindow():
    # หน้าจอที่ 2
    myWindow = Tk()
    myWindow.title("My Secon GUI")
    myWindow.geometry("500x300+700+300")
    myLabel = Label(myWindow, text="Welcome To 2nd GUI !", fg="red", font=20, bg="yellow").pack()

# กล่องข้อความ
txt=StringVar()
myText=Entry(root,textvariable=txt).pack()

# ใส่ปุ่ม
button1 = Button(root,text="ตกลง",fg="white",bg="green",command=showMessage).pack()
button2 = Button(root,text="เปิดรายงาน",fg="white",bg="gray",command=openWindow).pack()

root.mainloop()