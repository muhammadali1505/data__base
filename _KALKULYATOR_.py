from tkinter import *
root = Tk()
root.config(bg="white")

ishora = ''
firstNum = ''
def cal(number):
    getNum = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, getNum+str(number))

def dev():
    global ishora, firstNum
    ishora='bolish'
    firstNum = entry.get()
    entry.delete(0, END)

def ast():
    global ishora, firstNum
    ishora='kopaytir'
    firstNum = entry.get()
    entry.delete(0, END)

def plus():
    global ishora, firstNum
    ishora='qoshish'
    firstNum = entry.get()
    entry.delete(0, END)

def subtract():
    global ishora, firstNum
    ishora='ayrish'
    firstNum = entry.get()
    entry.delete(0, END)

def result():
    newNum = entry.get()
    entry.delete(0, END)
    if ishora=='bolish':
        entry.insert(0, f"{int(firstNum)/int(newNum)}")
    elif ishora=='kopaytir':
        entry.insert(0, f"{int(firstNum)*int(newNum)}")
    if ishora=='qoshish':
        entry.insert(0, f"{int(firstNum)+int(newNum)}")
    elif ishora=='ayrish':
        entry.insert(0, f"{int(firstNum)-int(newNum)}")

entry = Entry(root, width=25, font=('consolas', 24))
backSpace = Button(root, text='C', font=('consolas', 24),
                   command=lambda : entry.delete(len(entry.get())-1, END))
point = Button(root, text='P', font=('consolas', 24), command=lambda : entry.delete(0, END))
devide = Button(root, text='/', font=('consolas', 24), command=dev)
multiply = Button(root, text='*', font=('consolas', 24),command=ast)
minus = Button(root, text='-', font=('consolas', 24),command=subtract)
plus = Button(root, text='+',font=('consolas', 24),command=plus)
equel = Button(root, text='=', font=('consolas', 24), command=result)



btn1 = Button(root, text=1, font=('consolas', 24), command=lambda : cal(1))
btn2 = Button(root, text=2, font=('consolas', 24), command=lambda : cal(2))
btn3 = Button(root, text=3, font=('consolas', 24), command=lambda : cal(3))
btn4 = Button(root, text=4, font=('consolas', 24), command=lambda : cal(4))
btn5 = Button(root, text=5, font=('consolas', 24), command=lambda : cal(5))
btn6 = Button(root, text=6, font=('consolas', 24), command=lambda : cal(6))
btn7 = Button(root, text=7, font=('consolas', 24), command=lambda : cal(7))
btn8 = Button(root, text=8, font=('consolas', 24), command=lambda : cal(8))
btn9 = Button(root, text=9, font=('consolas', 24), command=lambda : cal(9))
btn0 = Button(root, text=0, font=('consolas', 24), command=lambda : cal(0))
# btn00= Button(root, text=00,font=('consolas', 24), command=lambda : cal(00))

entry.grid(row=0, column=0, columnspan=4, pady=15, padx=15)
backSpace.grid(row=1, column=0)
point.grid(row=1, column=1)
devide.grid(row=1, column=2)
multiply.grid(row=1, column=3)
minus.grid(row=2, column=3)
# subtract.grid(row=1, column=3)
plus.grid(row=3, column=3)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=2, column=2)
btn4.grid(row=3, column=0)
btn5.grid(row=3, column=1)
btn6.grid(row=3, column=2)
btn7.grid(row=4, column=0)
btn8.grid(row=4, column=1)
btn9.grid(row=4, column=2)
btn0.grid(row=5, column=0)
# btn00.grid(row=5,column=1)

equel.grid(row=5, column=3, columnspan=2)

root.mainloop()
