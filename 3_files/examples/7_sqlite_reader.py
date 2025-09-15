import sqlite3

conn = sqlite3.connect("test.db")

cursor = conn.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER
# )
# """)
#
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
#
# conn.commit()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print(rows)  # [(1, 'Alice', 25)]

conn.close()
