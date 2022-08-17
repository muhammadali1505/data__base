# from tkinter import *
#
# root = Tk()
# root.config(bg="black")
#
# data = 0
# action = ""
#
#
# def number(digit: str):
#     global enter
#     enter.insert(index=END, string=digit)
#
#
# def fun_plus():
#     global action, data
#     data += int(enter.get())
#     action += "plus"
#     enter.delete(0, END)
#
#
# def fun_minus():
#     global action, data
#     data += int(enter.get())
#     action += "minus"
#     enter.delete(0, END)
#
#
# def fun_multiplay():
#     global action, data
#     data += int(enter.get())
#     action += "multiplay"
#     enter.delete(0, END)
#
#
# def fun_devide():
#     global action, data
#     data += int(enter.get())
#     action += "devide"
#     enter.delete(0, END)
#
#
# def fun_equal():
#     global data, action
#     if action == "plus":
#         print(data)
#         print(enter.get())
#         data += int(enter.get())
#     elif action == "minus":
#         data -= int(enter.get())
#     enter.delete(0, END)
#     enter.insert(END, str(data))
#     if action == "multiplay":
#         print(data)
#         print(enter.get())
#         data += int(enter.get())
#     elif action == "devide":
#         data -= int(enter.get())
#     enter.delete(0, END)
#     enter.insert(END, str(data))
#
#
# enter = Entry()
# enter.pack()
#
# button1 = Button(text="1", command=lambda: number("1"))
# button2 = Button(text="2", command=lambda: number("2"))
# button3 = Button(text="3", command=lambda: number("3"))
# button4 = Button(text="4", command=lambda: number("4"))
# button5 = Button(text="5", command=lambda: number("5"))
# button6 = Button(text="6", command=lambda: number("6"))
# button7 = Button(text="7", command=lambda: number("7"))
# button8 = Button(text="8", command=lambda: number("8"))
# button9 = Button(text="9", command=lambda: number("9"))
# button0 = Button(text="0", command=lambda: number("0"))
#
#
# # button1.grid(row=0, column=0)
# # button2.grid(row=0, column=1)
# # button3.grid(row=0, column=2)
# # button4.grid(row=1, column=0)
# # button5.grid(row=1, column=1)
# # button6.grid(row=1, column=2)
# # button7.grid(row=2, column=0)
# # button8.grid(row=2, column=1)
# # button9.grid(row=2, column=2)
#
#
#
# # .grid(row=0, column=0)
# # .grid(row=0, column=1)
# # .grid(row=0, column=2)
# # .grid(row=1, column=0)
# # .grid(row=1, column=1)
# # .grid(row=1, column=2)
# # .grid(row=2, column=0)
# # .grid(row=2, column=1)
# # .grid(row=2, column=2)
# # .grid(row=3, column=1, columnspan=2
#
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()
# button5.pack()
# button6.pack()
# button7.pack()
# button8.pack()
# button9.pack()
# button0.pack()
#
#
# plus = Button(text="+", command=fun_plus)
# minus = Button(text="-", command=fun_minus)
# multiplay = Button(text="*", command=fun_multiplay)
# devide = Button(text="/", command=fun_devide)
# equal = Button(text="=", command=fun_equal)
# equal.pack()
#
#
# plus.pack()
# minus.pack()
# multiplay.pack()
# devide.pack()
#
#
# mainloop()



from tkinter import *


root = Tk()
root.geometry('500x550')
root.config(bg='grey')

data = 0
action = ""


def number(digit: str):
    global enter
    enter.insert(index=END, string=digit)

def minus():
    global action, data
    data += int(enter.get())
    action += 'minus'
    enter.delete(0, END)


def fun_plus():
    global action, data
    data += int(enter.get())
    action += "plus"
    enter.delete(0, END)

def multiply():
    global action, data
    data += int(enter.get())
    action += 'multiplication'
    enter.delete(0, END)

def devide():
    global action, data
    data += int(enter.get())
    action += 'bolish'
    enter.delete(0, END)


def fun_equal():
    global data, action
    if action == "plus":
        # print(data)
        # print(enter.get())
        data += int(enter.get())
    elif action == "minus":
        data -= int(enter.get())
    elif action == 'multiplication':
        data *= int(enter.get())
    elif action == 'bolish':
        data /= int(enter.get())
    enter.delete(0, END)
    enter.insert(END, str(data))



enter = Entry()
enter.pack()

button1 = Button(text="1", command=lambda: number("1"))
button2 = Button(text="2", command=lambda: number("2"))
button3 = Button(text="3", command=lambda: number("3"))
button4 = Button(text="4", command=lambda: number("4"))
button5 = Button(text="5", command=lambda: number("5"))
button6 = Button(text="6", command=lambda: number("6"))
button7 = Button(text="7", command=lambda: number("7"))
button8 = Button(text="8", command=lambda: number("8"))
button9 = Button(text="9", command=lambda: number("9"))
button0 = Button(text="0", command=lambda: number("0"))
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button0.pack()


plus = Button(text="+", command=fun_plus)
minus = Button(text="-", command=minus)
equal = Button(text="=", command=fun_equal)
multiplayy = Button(text='*', command=multiply)
drvide = Button(text='/', command=devide)
drvide.pack()
multiplayy.pack()
plus.pack()
minus.pack()
equal.pack()

root.mainloop()