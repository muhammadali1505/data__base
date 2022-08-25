import sqlite3

conn = sqlite3.connect("user1.db")

conn.execute('''CREATE TABLE "user" (
  "name"  TEXT NOT NULL,
);''')
conn.commit()
conn.close()
print('Running...')
