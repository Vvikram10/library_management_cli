# 📚 Library Management System - Python CLI Project

A beginner-friendly **Console-based Python Project** using **Object-Oriented Programming (OOP)** to manage a simple library system. It allows users to add books, borrow/return them, and view all available/borrowed books.

---

## 🚀 Features

✅ Add books to the library  
✅ Borrow a book (with user name tracked)  
✅ Return a borrowed book  
✅ View current library catalog  
✅ Tracks who borrowed which book  
✅ Built using Python’s OOP concepts  
✅ No external dependencies  

---

## 🧠 Concepts Used

- 🔁 Loops and Conditional Logic
- 🧱 Classes and Objects
- 🔐 Encapsulation (private variables)
- 📋 Dictionary for Data Management
- 🖥️ CLI Menu System

---
====== Library Management System ======
1. Add Book
2. Borrow Book
3. Return Book
4. Show All Books
5. Exit
Enter your choice: 1
Enter Book ID: 1
Enter Book Title: my story
Enter Author Name: vikram
✅ Book registered successfully!

====== Library Management System ======
1. Add Book
2. Borrow Book
3. Return Book
4. Show All Books
5. Exit
Enter your choice: 1
Enter Book ID: 2
Enter Book Title: your story 
Enter Author Name: pari
✅ Book registered successfully!

====== Library Management System ======
Enter your choice: 4
---------- Library Books ----------
1 - my story by vikram | Available
2 - your story  by pari | Available

Enter your choice: 2
Enter Book ID to borrow: 1
Enter your name: shubham
✅ 'my story' has been borrowed by shubham

Enter your choice: 4
---------- Library Books ----------
1 - my story by vikram | Borrowed by shubham
2 - your story  by pari | Available

Enter your choice: 2
Enter Book ID to borrow: 1
Enter your name: shubhi
❌ Book is already borrowed by shubham

Enter your choice: 3
Enter Book ID to return: 1
✅ 'my story' returned by shubham

Enter your choice: 4
---------- Library Books ----------
1 - my story by vikram | Available
2 - your story  by pari | Available

Enter your choice: 5
👋 Thank you for using the Library System.

## 📂 Project Structure


---

## 💻 How to Run

> You just need Python 3 installed!

```bash
python library_management.py

