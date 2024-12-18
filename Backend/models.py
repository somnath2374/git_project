from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    available = db.Column(db.Integer, default=1)  # 1 means available, 0 means borrowed

    def __repr__(self):
        return f"<Book {self.title} by {self.author}>"

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

# Borrow model to track book borrowing
class Borrow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date)
    overdue = db.Column(db.Integer, default=0)  # 1 if overdue, 0 if not

    user = db.relationship('User', backref=db.backref('borrows', lazy=True))
    book = db.relationship('Book', backref=db.backref('borrows', lazy=True))

    def __repr__(self):
        return f"<Borrow {self.user.name} borrowed {self.book.title}>"
