import tkinter
def a(e):
    b = 'Key {}, (code {}) was pressed'.format(e.keysym, e.keycode)
    lvar.set(b)
root = tkinter.Tk()
root.title('Key event')
lvar = tkinter.StringVar()
lbl = tkinter.Label(root, text="coordinates", textvariable=lvar)
lbl.place(x=20, y=20)
root.bind('<Key>', a)
root.geometry("300x250+300+300")
root.mainloop()
