import sqlite3

conn = sqlite3.connect('people.db')

conn.execute('''CREATE TABLE "student" (
  "id"  INTEGER NOT NULL,
  "name"  TEXT NOT NULL,
  "age"  INTEGER NOT NULL
);''')
conn.commit()
conn.close()
print('Running...')
