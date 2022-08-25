import sqlite3
from tkinter import *

root = Tk()
conn = sqlite3.connect('pythonUser.db')
cur = conn.cursor()
getData = cur.execute('select * from pythonUsers;')
conn.commit()
listbox = Listbox(root, font='cosolas 24')
count = 0
for i in getData:
    listbox.insert(count, i)
    count += 1
conn.close()
listbox.pack()
root.mainloop()


# CREATE TABLE "pythonUsers" (
# 	"data"	TEXT NOT NULL
# );