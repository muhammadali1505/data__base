from tkinter import *
root=Tk()
root.config(bg='turquoise')
data = []
temp = int()
def add():
    global temp
    if entry.get()!='':
        data.append(entry.get())
        listbox.insert(temp, f"{temp+1}.{entry.get()}")
        entry.delete(0, END)
        temp+=1
    else:
        pass
def del1():
    global temp
    if entry.get()!='':
        data.append(entry.get())
        listbox.insert(temp, f"{temp-1}.{entry.get()}")
        entry.delete(0, END)
        temp-=1
    else:
        pass

entry = Entry(root, font=('consolas', 24), bg='white', fg='black')
button = Button(root, text='Add', font=('consolas', 24), command=add)
button1=Button(root, text="Del",font=('consolas', 24), command=del1)
listbox = Listbox(root, bg='white', fg='black',font=('consolas', 24))

entry.grid(row=0, column=0, sticky='n', pady=30, padx=15)
button.grid(row=1, column=0, sticky='n', pady=30, padx=15)
button1.grid(row=1,column=1,pady=30,padx=15)
listbox.grid(row=0, column=1, rowspan=2, padx=30, pady=30)

root.bind('<Return>', lambda event: add())
root.mainloop()
