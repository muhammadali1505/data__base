import sqlite3
conn = sqlite3.connect("people.db")

# conn.execute("insert into student(id, name, age) values(1, "Tursunov Imron", 12)")
# conn.execute("insert into student(id, name, age) values(2, "Muqumov Kamron", 15)")
conn.execute("insert into student(id, name, age) values(3, 'Sirojiddinov Azizbek', 15)")

conn.commit()
conn.close()

print("OK")