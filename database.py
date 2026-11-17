import sqlite3

db = sqlite3.connect('baza.db')
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS contact(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ism VARCHAR(50),
    familya VARCHAR(50),
    yosh INTEGER,
    raqam TEXT,
    adress VARCHAR(100)
)
""")