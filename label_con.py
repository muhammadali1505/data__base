from tkinter import *

root = Tk()
count = 0


def onClickButtoncount():
    global count
    count += 1
    label.config(text=count)


label = Label(root, text='Zero')
label.pack()

button1 = Button(root, text='ADD', command=onClickButtoncount, bg='grey')
button2 = Button(root, text='remove', command=onClickButtoncount, bg='red')

button1.pack()
button2.pack()

root.mainloop()
