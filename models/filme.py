import sqlite3

conn = sqlite3.connect('database/banco_dados.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        ano INTEGER NOT NULL,
        avaliacao REAL,
        assistido BOOLEAN DEFAULT FALSE
    );
''')

conn.commit()
conn.close()