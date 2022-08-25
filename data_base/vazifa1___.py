import sqlite3
conn = sqlite3.connect('pythonUser.db')

conn.commit()
conn.close()
print('Successfully...')