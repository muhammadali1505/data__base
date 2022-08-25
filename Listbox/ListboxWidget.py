# # from tkinter import *
# # root = Tk()
# # listbox = Listbox(root)
# # listbox.insert(0, "Banan")
# # listbox.insert(1, "Apelsin")
# # listbox.insert(2, "Kivi")
# # listbox.insert(3, "Mandarin")
# #
# # listbox.pack()
# #
# # root.mainloop()
#
# # from tkinter import *
# # root = Tk()
# # root.config(bg="grey")
# # data = ["Axmad","Imron","Kamron","Yosimhon","Ali","Bahodir","Zafar"]
# # listbox = Listbox(root, bg="white",fg="black",font=("consolas",24))
# # for i in data:
# #     index = data.index(i)
# #     listbox.insert(index,i)
# # listbox.pack()
# #
# # root.mainloop()
# from tkinter import *
# root = Tk()
# listbox = Listbox(root)
# listbox.insert(0, "Banan")
# listbox.insert(1, "Apelsin")
# listbox.insert(2, "Kivi")
# listbox.insert(3, "Mandarin")
# def getStorgeID():
#     getID = Listbox.curselection()[0]
#     print(getID)
#
# button = Button(root,text="ID",command=getStorgeID)
# button.pack()
# listbox.pack()
#
# root.mainloop()
from tkinter import *
root = Tk()
listbox = Listbox(root)
listbox.insert(0, 'Banana')
listbox.insert(1, 'Apelsin')
listbox.insert(2, 'Kivi')
listbox.insert(3, 'Mandarin')
def getStorageId():
    getId = listbox.curselection()[0]
    print(getId)

btn = Button(root, text='ID', command=getStorageId)
listbox.pack()
btn.pack()

root.mainloop()
