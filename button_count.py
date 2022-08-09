from tkinter import *

root = Tk()
count = 0

def onClickButtoncount():
    global count
    count+=1
    print(count,'- marta bosildi')

button1 = Button(root, text='Clik 1', bg='red',command=onClickButtoncount)
button1.pack()

root.mainloop()
