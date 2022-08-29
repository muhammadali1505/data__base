# import sqlite3
# from tkinter import *
#
# root = Tk()
# conn = sqlite3.connect('pythonUser.db')
# cur = conn.cursor()
# getData = cur.execute('SELECT * FROM pythonUsers;')
# conn.commit()
# listbox = Listbox(root, font='cosolas 24')
# count = 0
# for i in getData:
#     listbox.insert(count, i)
#     count += 1
# conn.close()
# listbox.pack()
# root.mainloop()
#
#

import sqlite3
conn = sqlite3.connect('helperr.db')
conn.execute('create table  if not exists username(fullname text not null);')

getUser = input('Fullname: '),

conn.execute("INSERT INTO username VALUES(?);", getUser)

conn.commit()
conn.close()


import sqlite3
conn = sqlite3.connect('helperr.db')

getData = conn.execute("SELECT * FROM username;")
print(getData.fetchall())

conn.commit()
conn.close()
