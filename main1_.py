# from tkinter import *
# root = Tk()
# root.geometry("440x540")
# root.maxsize(640,740)
# root.minsize(200,250)
# root.config(bg='black')
#
#
# root.mainloop()


from tkinter import Button,Tk

root = Tk()
count = 0


def onClickButtoncount():
    global count
    count+=1

    print(count)
    button1.config(text=count)

button1 = Button(root, text='Clik Me', bg='grey',command=onClickButtoncount)
button1.pack()

root.mainloop()
