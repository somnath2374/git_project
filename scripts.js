document.addEventListener('DOMContentLoaded', () => {
  loadSampleBooks();
  loadSampleTransactions();
});

function loadSampleBooks() {
  const books = [
      { cover: 'images/book1.jpg', title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', genre: 'Fiction' },
      { cover: 'images/book2.jpg', title: 'To Kill a Mockingbird', author: 'Harper Lee', genre: 'Fiction' },
      { cover: 'images/book3.jpg', title: '1984', author: 'George Orwell', genre: 'Dystopian' }
  ];

  books.forEach(book => addBookToTable(book));
}

function loadSampleTransactions() {
  const transactions = [
      { book: 'The Great Gatsby', member: 'John Doe', dateBorrowed: '2023-01-01', dateReturned: '2023-01-10' },
      { book: 'To Kill a Mockingbird', member: 'Jane Smith', dateBorrowed: '2023-02-01', dateReturned: '2023-02-10' }
  ];

  transactions.forEach(transaction => addTransactionToTable(transaction));
}

function promptBookDetails(existingData = {}) {
  const title = prompt('Enter book title:', existingData.title || '');
  const author = prompt('Enter book author:', existingData.author || '');
  const genre = prompt('Enter book genre:', existingData.genre || '');
  const cover = prompt('Enter book cover image URL:', existingData.cover || '');
  
  return { title, author, genre, cover };
}

function addBook() {
  const { title, author, genre, cover } = promptBookDetails();
  
  if (title && author && genre && cover) {
      const book = { cover, title, author, genre };
      addBookToTable(book);
  }
}

function addBookToTable(book) {
  const table = document.querySelector('#books tbody');
  const row = document.createElement('tr');

  row.innerHTML = `
      <td><img src="${book.cover}" alt="${book.title}" width="50"></td>
      <td>${book.title}</td>
      <td>${book.author}</td>
      <td>${book.genre}</td>
      <td>
          <button class="editBook">Edit</button>
          <button class="deleteBook">Delete</button>
      </td>
  `;

  table.appendChild(row);
}

document.querySelector('#books tbody').addEventListener('click', (event) => {
  if (event.target.classList.contains('editBook')) {
      const row = event.target.closest('tr');
      const { title, author, genre, cover } = promptBookDetails({
          title: row.cells[1].innerText,
          author: row.cells[2].innerText,
          genre: row.cells[3].innerText,
          cover: row.cells[0].querySelector('img').src
      });

      if (title && author && genre && cover) {
          row.cells[0].querySelector('img').src = cover;
          row.cells[0].querySelector('img').alt = title;
          row.cells[1].innerText = title;
          row.cells[2].innerText = author;
          row.cells[3].innerText = genre;
      }
  } else if (event.target.classList.contains('deleteBook')) {
      const row = event.target.closest('tr');
      row.remove();
  }
});

function addTransaction() {
  const book = prompt('Enter book title:');
  const member = prompt('Enter member name:');
  const dateBorrowed = prompt('Enter date borrowed (YYYY-MM-DD):');
  const dateReturned = prompt('Enter date returned (YYYY-MM-DD):');

  if (book && member && dateBorrowed && dateReturned) {
      const transaction = { book, member, dateBorrowed, dateReturned };
      addTransactionToTable(transaction);
  }
}

function addTransactionToTable(transaction) {
  const table = document.querySelector('#transactions tbody');
  const row = document.createElement('tr');

  row.innerHTML = `
      <td>${transaction.book}</td>
      <td>${transaction.member}</td>
      <td>${transaction.dateBorrowed}</td>
      <td>${transaction.dateReturned}</td>
      <td>
          <button class="editTransaction">Edit</button>
          <button class="deleteTransaction">Delete</button>
      </td>
  `;

  table.appendChild(row);
}

document.querySelector('#transactions tbody').addEventListener('click', (event) => {
  if (event.target.classList.contains('editTransaction')) {
      const row = event.target.closest('tr');
      const book = prompt('Edit book title:', row.cells[0].innerText);
      const member = prompt('Edit member name:', row.cells[1].innerText);
      const dateBorrowed = prompt('Edit date borrowed  (YYYY-MM-DD):', row.cells[2].innerText);
      const dateReturned = prompt('Edit date returned  (YYYY-MM-DD):', row.cells[3].innerText);

      if (book && member && dateBorrowed && dateReturned) {
          row.cells[0].innerText = book;
          row.cells[1].innerText = member;
          row.cells[2].innerText = dateBorrowed;
          row.cells[3].innerText = dateReturned;
      }
  } else if (event.target.classList.contains('deleteTransaction')) {
      const row = event.target.closest('tr');
      row.remove();
  }
});

function addMember() {
  const name = prompt('Enter member name:');
  const email = prompt('Enter member email:');
  const membershipDate = prompt('Enter membership date (YYYY-MM-DD):');

  if (name && email && membershipDate) {
      const member = { name, email, membershipDate };
      addMemberToTable(member);
  }
}

function addMemberToTable(member) {
  const table = document.querySelector('#members tbody');
  const row = document.createElement('tr');

  row.innerHTML = `
      <td>${member.name}</td>
      <td>${member.email}</td>
      <td>${member.membershipDate}</td>
      <td>
          <button class="editMember">Edit</button>
          <button class="deleteMember">Delete</button>
      </td>
  `;

  table.appendChild(row);
}

document.querySelector('#members tbody').addEventListener('click', (event) => {
  if (event.target.classList.contains('editMember')) {
      const row = event.target.closest('tr');
      const name = prompt('Edit member name:', row.cells[0].innerText);
      const email = prompt('Edit member email:', row.cells[1].innerText);
      const membershipDate = prompt('Edit membership date (YYYY-MM-DD):', row.cells[2].innerText);

      if (name && email && membershipDate) {
          row.cells[0].innerText = name;
          row.cells[1].innerText = email;
          row.cells[2].innerText = membershipDate;
      }
  } else if (event.target.classList.contains('deleteMember')) {
      const row = event.target.closest('tr');
      row.remove();
  }
});

function searchBooks() {
  const input = document.getElementById('searchBook');
  const filter = input.value.toLowerCase();
  const table = document.querySelector('#books tbody');
  const rows = table.getElementsByTagName('tr');

  for (let i = 0; i < rows.length; i++) {
      const title = rows[i].getElementsByTagName('td')[1].innerText.toLowerCase();
      if (title.includes(filter)) {
          rows[i].style.display = '';
      } else {
          rows[i].style.display = 'none';
      }
  }
}
