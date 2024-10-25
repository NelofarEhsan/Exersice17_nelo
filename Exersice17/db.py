#C:\Python2024\SQLite\Mydatabase
import sqlite3

def connect():
    return sqlite3.connect('movies.db')

def create_tables():
    conn = connect()
    cur = conn.cursor()
    # Create tables if not exists
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Movie (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        year INTEGER,
        minutes INTEGER,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Category (id)
    )
    ''')
    conn.commit()
    conn.close()

def get_categories():
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Category')
    categories = cur.fetchall()
    conn.close()
    return categories

def get_movies_by_category(category_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM Movie WHERE category_id = ?', (category_id,))
    movies = cur.fetchall()
    conn.close()
    return movies

def insert_category(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute('INSERT INTO Category (name) VALUES (?)', (name,))
    conn.commit()
    conn.close()

def insert_movie(name, year, minutes, category_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Movie (name, year, minutes, category_id)
        VALUES (?, ?, ?, ?)
    ''', (name, year, minutes, category_id))
    conn.commit()
    conn.close() 