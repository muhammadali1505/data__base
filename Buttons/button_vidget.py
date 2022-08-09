from tkinter import *

root = Tk()
root.geometry("200x150")


def OnClickButton1():
    print('buton 1 bosildi')


button1 = Button(root, text='Clik 1', bg='red', command=OnClickButton1)


def OnClickButton2():
    print('buton 2 bosildi')


button2 = Button(root, text='Clik 2', bg='yellow', command=OnClickButton2)


def OnClickButton3():
    print('buton 3 bosildi')


button3 = Button(root, text='Clik 3', bg='grey', command=OnClickButton3)
button1.pack()
button2.pack()
button3.pack()

root.mainloop()




# count = 0
# def msg():
#     global count
#     count += 1
#
# msg()
# print(count)



