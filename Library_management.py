# ------------------------- Class Definition -----------------------
class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__is_available = True
        self.__borrowed_by = None  # New: To track who borrowed it

    def borrow(self, user_name):
        if self.__is_available:
            self.__is_available = False
            self.__borrowed_by = user_name
            print(f"✅ '{self.__title}' has been borrowed by {user_name}")
        else:
            print(f"❌ Book is already borrowed by {self.__borrowed_by}")

    def return_book(self):
        if not self.__is_available:
            print(f"✅ '{self.__title}' returned by {self.__borrowed_by}")
            self.__is_available = True
            self.__borrowed_by = None
        else:
            print("❌ Book was not borrowed.")

    def display(self):
        status = 'Available' if self.__is_available else f'Borrowed by {self.__borrowed_by}'
        print(f"{self.__book_id} - {self.__title} by {self.__author} | {status}")

# ------------------------- Data Storage ---------------------------
books = {}

# ------------------------- Functions ------------------------------
def add_book():
    book_id = input('Enter Book ID: ')
    if book_id in books:
        print("⚠️ Book ID already exists.")
        return
    title = input('Enter Book Title: ')
    author = input('Enter Author Name: ')
    books[book_id] = Book(book_id, title, author)
    print("✅ Book registered successfully!")

def borrow_book():
    book_id = input('Enter Book ID to borrow: ')
    if book_id in books:
        user = input('Enter your name: ')
        books[book_id].borrow(user)
    else:
        print("❌ Book not found.")

def return_book():
    book_id = input('Enter Book ID to return: ')
    if book_id in books:
        books[book_id].return_book()
    else:
        print("❌ Book not found.")

def show_books():
    if not books:
        print("📚 No books in the library.")
    else:
        print("---------- Library Books ----------")
        for book in books.values():
            book.display()

# ------------------------ Menu Loop -------------------------------
def main():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Show All Books")
        print("5. Exit")

        choice = input('Enter your choice: ')
        if choice == '1':
            add_book()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            show_books()
        elif choice == '5':
            print("👋 Thank you for using the Library System.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# ------------------------- Run Program ----------------------------
if __name__ == '__main__':
    main()
