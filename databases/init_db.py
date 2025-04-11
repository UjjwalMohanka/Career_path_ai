import sqlite3

conn = sqlite3.connect('database/users.db')
c = conn.cursor()

# Create users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    skills TEXT,
    goal TEXT
)
''')

conn.commit()
conn.close()
