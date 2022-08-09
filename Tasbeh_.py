from tkinter import *
root = Tk()
root.config(bg="black")
root.geometry('330x380')
root.resizable(False, False)
style = ('consolas', 24)
frame = Frame(root, width=200, bg='red')
Data_text = ['Subhanalloh','Alhamdulillah', 'Allohu Akbar']
count = 0
i = 0
label_1 = Label(root, text='ﷺ', font=("Arign",50),
              bg= 'black',fg='lime')

label_2 = Label(root, text=Data_text[i], font=style,
              bg= 'black',fg='white')

label_3 = Label(root, text=count, font=style,
              bg= 'black',fg='lime')
def onClickButton():
    global count
    global i
    try:
        if count != 33:
            count += 1
        else:
            count = 0
            i += 1
            label_2.config(text=Data_text[i])
        label_3.config(text=count)
    except:
        i = 0
        label_2.config(text=Data_text[i])
button = Button(root, text="⭕", font=style,
                activeforeground='lime',bg= 'black',fg='lime',
                activebackground='black', command=onClickButton)
label_1.pack()
frame.pack()
label_2.pack(pady=15)
label_3.pack(pady=15)
button.pack(pady=50)

root.mainloop()
