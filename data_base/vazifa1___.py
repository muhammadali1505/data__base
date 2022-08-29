import sqlite3
conn = sqlite3.connect('pythonUsers.db')

conn.commit()
conn.close()
print('Successfully...')