"""
pip install pysqlite3
"""

import sqlite3
conn = sqlite3.connect('user1.db')
conn.execute("create tabel if not exists data(name text not null);")

getUser = input("Fullname: ")
conn.execute("INSERT INTO data VALUES(?)",)

conn.commit()
conn.close()
print('Successfully...')
