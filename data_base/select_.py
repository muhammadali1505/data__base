"""
pip install pysqlite3
"""

import sqlite3
conn = sqlite3.connect('people.db')

conn.commit()
conn.close()
print('Successfully...')