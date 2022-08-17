from tkinter import Label,Tk
root = Tk()
label1 = Label(root,text='option1',bg='teal',fg='black')
label2 = Label(root,text='option2',bg='red',fg='black')
label3 = Label(root,text='option3',bg='green',fg='black')
label4 = Label(root,text='option4',bg='yellow',fg='black')
label5 = Label(root,text='option5',bg='orange',fg='black',width=11)

label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=0,column=2)
label4.grid(row=1,column=0)
label5.grid(row=1,column=1,columnspan=2)

root.mainloop()



# from tkinter import *
# root = Tk()
# root.geometry('400x500')
#
# def f():
#     print(entry.get())
#     entry.delete(0, END)
#
# entry = Entry(root,width=20,font=('consolas',24))
# btn = Button(root,text='Get',font=('consolas',24),command=f)
#
# entry.pack()
# btn.pack()
#
# root.mainloop()
