from tkinter import *
from PIL import ImageTk, Image

root = Tk()


rasm = Image.open('images.jpg').resize((500, 200))
NewImage = ImageTk.PhotoImage(rasm)
rasm1 = Image.open('images1.jpg').resize((500, 200))
NewImage1 = ImageTk.PhotoImage(rasm1)
rasm2 = Image.open("imgpy.jpg").resize((500, 200))
NewImage2 = ImageTk.PhotoImage(rasm2)
rasm3 = Image.open("Py.png").resize((500, 200))
NewImage3 = ImageTk.PhotoImage(rasm3)

def n():
    label.config(image=NewImage1)
    label1.config(image=NewImage3)



label = Label(root, image=NewImage)
label.pack()
label1 = Label(root, image=NewImage2)
label1.pack()


btn = Button(root, text='>', bg='grey', command=n)
btn.pack(side=RIGHT)
btn1 = Button(root, text='<', bg='grey', command=n)
btn1.pack(side=LEFT)


root.mainloop()
