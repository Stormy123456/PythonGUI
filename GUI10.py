from tkinter import *
from tkinter import ttk

root = Tk()
root.title("เครื่องคิดเลข")

content = " "
txt_input = StringVar(value="0")

def btn(number):
    global content
    content = content+str(number)
    txt_input.set(content)

def result():
    global content
    calculate = float(eval(content))
    txt_input.set(calculate)
    content = str(calculate)

def clear():
    global content
    content = " "
    txt_input.set("")
    display.insert(0,"0")


# แสดงผล
display = Entry(font=('arial',22,'bold'),fg="white",bg="green",textvariable=txt_input,justify="right")
display.grid(columnspan=4)

# รับค่าผ่านปุ่ม
btn7=Button(fg="black",font=('arial,30,bold'),text="7",command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8=Button(fg="black",font=('arial,30,bold'),text="8",command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9=Button(fg="black",font=('arial,30,bold'),text="9",command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnC=Button(fg="black",bg="orange",font=('arial,30,bold'),text="C",command=clear,padx=30,pady=15).grid(row=1,column=3)

btn4=Button(fg="black",font=('arial,30,bold'),text="5",command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5=Button(fg="black",font=('arial,30,bold'),text="5",command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6=Button(fg="black",font=('arial,30,bold'),text="6",command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
btnPlus=Button(fg="black",bg="orange",font=('arial,30,bold'),text="+",command=lambda:btn("+"),padx=32,pady=15).grid(row=2,column=3)

btn1=Button(fg="black",font=('arial,30,bold'),text="1",command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2=Button(fg="black",font=('arial,30,bold'),text="2",command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3=Button(fg="black",font=('arial,30,bold'),text="3",command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
btnMinus=Button(fg="black",bg="orange",font=('arial,30,bold'),text="-",command=lambda:btn("-"),padx=34,pady=15).grid(row=3,column=3)

btnDot=Button(fg="black",font=('arial,30,bold'),text=".",command=lambda:btn("."),padx=33,pady=15).grid(row=4,column=0)
btn0=Button(fg="black",font=('arial,30,bold'),text="0",command=lambda:btn(0),padx=31,pady=15).grid(row=4,column=1)
btnDivision=Button(fg="black",bg="orange",font=('arial,30,bold'),text="/",command=lambda:btn("/"),padx=33,pady=15).grid(row=4,column=2)
btnMultiply=Button(fg="black",bg="orange",font=('arial,30,bold'),text="x",command=lambda:btn("*"),padx=33,pady=15).grid(row=4,column=3)

btnOpen=Button(fg="black",font=('arial,30,bold'),text="(",command=lambda:btn("("),padx=32,pady=15).grid(row=5,column=0)
btnClose=Button(fg="black",font=('arial,30,bold'),text=")",command=lambda:btn(")"),padx=32,pady=15).grid(row=5,column=1)
btnResult=Button(fg="black",bg="cyan",font=('arial,30,bold'),text="=",command=result,padx=74,pady=15).grid(row=5,column=2,columnspan=2)


root.mainloop()