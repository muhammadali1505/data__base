import sqlite3
conn = sqlite3.connect("people.db")

getdata = conn.execute("SELECT * FROM student;")
print(getdata)

conn.commit()
conn.close()
