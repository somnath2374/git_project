from flask import Flask, request, jsonify
from src.book_manager import search_books
from src.borrow_manager import borrow_book
from src.user_manager import get_user_by_email
from src.models import create_db

app = Flask(__name__)

# Create the database if it doesn't exist
create_db()

# Route to search books
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    books = search_books(query)
    return jsonify({"books": books})

# Route to borrow a books
@app.route('/borrow', methods=['POST'])
def borrow():
    data = request.get_json()
    user_email = data.get('email')
    book_id = data.get('book_id')

    # Check if user exists
    user = get_user_by_email(user_email)
    if not user:
        return jsonify({"message": "User not found!"}), 404
    
    # Borrow the book
    if borrow_book(user['id'], book_id):
        return jsonify({"message": "Book borrowed successfully!"})
    else:
        return jsonify({"message": "Book not available!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
