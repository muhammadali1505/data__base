from tkinter import *

root = Tk()
root.geometry("400x500")
root.config(bg="turquoise")

dataStorage = []


def addData():

    dataStorage.append(entry.get())
    entry.delete(0, END)
    # if add==dataStorage:



entry = Entry(root, font=("consolas", 28), bg="white", fg="black")
entry.grid(row=0, column=0, pady=20,padx=15,columnspan=2 )

add = Button(root, text="ADD",bg="green",command=addData,font=("consolas",28),width=5)
add.grid(row=1,column=1,sticky="E",padx=15)

show = Button(root, text="SHOW",bg="lime",command=lambda : print(dataStorage),font=("consolas",28),width=5)
show.grid(row=1,column=0,sticky="W",padx=15)

root.bind("<Return>",lambda event: addData())
root.bind("Space",lambda evenr: print(dataStorage))
root.bind("<Escape>",lambda event: quit())

root.mainloop()
