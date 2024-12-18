import sqlite3

def create_db():
    # Connect to SQLite database
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()

    # Create books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        available INTEGER DEFAULT 1
    )''')

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )''')

    # Create borrows table
    cursor.execute('''CREATE TABLE IF NOT EXISTS borrows (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        book_id INTEGER,
        borrow_date DATE,
        return_date DATE,
        overdue INTEGER DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(book_id) REFERENCES books(id)
    )''')

    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database and tables created successfully!")

if __name__ == '__main__':
    create_db()
