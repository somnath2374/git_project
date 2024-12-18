// Function to search for books
function searchBooks() {
    const query = document.getElementById('search-query').value;
    fetch(`http://localhost:5000/search?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const bookList = document.getElementById('books');
            bookList.innerHTML = ''; // Clear previous results
            data.books.forEach(book => {
                const li = document.createElement('li');
                li.textContent = `${book.title} by ${book.author}`;
                bookList.appendChild(li);
            });
        })
        .catch(error => console.error('Error fetching books:', error));
}

// Function to borrow a book
document.getElementById('borrow-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const userEmail = document.getElementById('user-email').value;
    const bookId = document.getElementById('book-id').value;
    
    fetch('http://localhost:5000/borrow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: userEmail, book_id: bookId })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error('Error borrowing book:', error));
});
