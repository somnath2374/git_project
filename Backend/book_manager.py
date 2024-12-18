import sqlite3

def search_books(query):
    conn = sqlite3.connect('database/library.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR isbn LIKE ?", 
                   ('%' + query + '%', '%' + query + '%', '%' + query + '%'))
    books = cursor.fetchall()
    conn.close()
    return [{"id": book[0], "title": book[1], "author": book[2], "isbn": book[3]} for book in books]
