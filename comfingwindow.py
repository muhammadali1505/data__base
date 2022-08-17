from tkinter import Tk,Button

root = Tk()
root.geometry("300x400")
root.config(bg='green')

# color = ['blue','black','grey','orange']
def f():
    root.config(bg="red")

btn = Button(root, text='Next Color',command=f)
btn.pack()


root.mainloop()
