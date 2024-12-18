from datetime import datetime
from models import db, Borrow, Book

# Check if a book is overdue
def check_overdue(borrow_id):
    borrow = Borrow.query.get(borrow_id)

    if not borrow:
        return {"error": "Borrow record not found"}

    today = datetime.today().date()

    if borrow.return_date is None:  # If the book hasn't been returned yet
        if borrow.borrow_date < today:
            # Mark the book as overdue
            borrow.overdue = 1
            db.session.commit()
            return {"message": f"Book {borrow.book.title} is overdue."}
    else:  # If the book has been returned, check if it was overdue
        if borrow.return_date < today:
            borrow.overdue = 1
            db.session.commit()
            return {"message": f"Book {borrow.book.title} was overdue."}

    return {"message": f"Book {borrow.book.title} is not overdue."}

# Mark a book as returned and check if it's overdue
def return_book(borrow_id, return_date=None):
    borrow = Borrow.query.get(borrow_id)

    if not borrow:
        return {"error": "Borrow record not found"}

    if return_date is None:
        return_date = datetime.today().date()

    borrow.return_date = return_date

    # Check if the book is overdue
    if borrow.return_date < borrow.borrow_date:
        borrow.overdue = 1
    db.session.commit()

    book = Book.query.get(borrow.book_id)
    book.available = 1  # Mark the book as available

    db.session.commit()

    return {"message": f"Book '{book.title}' returned successfully!"}

