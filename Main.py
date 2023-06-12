import sqlite3

connection = sqlite3.connect("sqliteDB/chinook.db")
print(connection.total_changes)
cursor = connection.cursor()
rows = cursor.execute("SELECT * FROM employees").fetchall()
print(rows[2])
for i in rows:
    print(i[3])
