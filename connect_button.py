# from tkinter import *
#
# root = Tk()
# root.geometry("200x150")
#
#
# def onClickButton():
#     print("OnClick button 1")
#
#
# button1 = Button(root, text='Clik 1', bg='red', width=10, height=5, command=onClickButton)
# button1.pack()
# root.mainloop()


from tkinter import Tk,Button

root = Tk()
button = Button(root, text='Click Me',bg='green')
button.pack()

root.mainloop()