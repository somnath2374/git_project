import sqlite3
from datetime import datetime

def borrow_book(user_id, book_id):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()

    # Check if the book is available
    cursor.execute("SELECT available FROM books WHERE id=?", (book_id,))
    available = cursor.fetchone()[0]
    if available == 1:
        borrow_date = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO borrows (user_id, book_id, borrow_date) VALUES (?, ?, ?)",
                       (user_id, book_id, borrow_date))
        cursor.execute("UPDATE books SET available = 0 WHERE id=?", (book_id,))
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False
