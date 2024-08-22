
from library_book import Book
from library_user import User
from library_author import Author
from utils import validate_input


def main_menu():
    print("1. Book Operations")
    print("2. User Operations")
    print("3. Author Operations")
    print("4. Quit")
    return validate_input(r"^[1-4]$", "Enter your choice: ")

def book_operations(library):
    print("Book Operations:")
    print("1. Add a new book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Search for a book")
    print("5. Display all books")
    choice = validate_input(r"^[1-5]$", "Enter your choice: ")

    if choice == "1":
        title = validate_input(r"^[\w\s]+$", "Enter book title: ")
        author = validate_input(r"^[\w\s]+$", "Enter author name: ")
        genre = validate_input(r"^[\w\s]+$", "Enter genre: ")
        publication_date = validate_input(r"^\d{4}-\d{2}-\d{2}$", "Enter publication date (YYYY-MM-DD): ")
        book = Book(title, author, genre, publication_date)
        library["books"].append(book)
        print(f"Book '{title}' added successfully!")

    elif choice == "2":
        library_id = validate_input(r"^\w+$", "Enter user ID: ")
        user = next((user for user in library["users"] if user.get_library_id() == library_id), None)
        if user:
            title = validate_input(r"^[\w\s]+$", "Enter book title: ")
            book = next((book for book in library["books"] if book.get_title() == title), None)
            if book and user.borrow_book(book):
                print(f"Book '{title}' borrowed successfully!")
            else:
                print(f"Book '{title}' is not available or does not exist.")
        else:
            print("User not found.")

    elif choice == "3":
        library_id = validate_input(r"^\w+$", "Enter user ID: ")
        user = next((user for user in library["users"] if user.get_library_id() == library_id), None)
        if user:
            title = validate_input(r"^[\w\s]+$", "Enter book title: ")
            book = next((book for book in library["books"] if book.get_title() == title), None)
            if book and user.return_book(book):
                print(f"Book '{title}' returned successfully!")
            else:
                print(f"Book '{title}' was not borrowed by this user.")
        else:
            print("User not found.")

    elif choice == "4":
        title = validate_input(r"^[\w\s]+$", "Enter book title: ")
        book = next((book for book in library["books"] if book.get_title() == title), None)
        if book:
            print(book)
        else:
            print("Book not found.")

    elif choice == "5":
        print("\nList of Books:")
        for book in library["books"]:
            print(book)

def user_operations(library):
    print("\nUser Operations:")
    print("1. Add a new user")
    print("2. View user details")
    print("3. Display all users")
    choice = validate_input(r"^[1-3]$", "Enter your choice: ")

    if choice == "1":
        name = validate_input(r"^[\w\s]+$", "Enter user name: ")
        library_id = validate_input(r"^\w+$", "Enter library ID: ")
        user = User(name, library_id)
        library["users"].append(user)
        print(f"User '{name}' added successfully!")

    elif choice == "2":
        library_id = validate_input(r"^\w+$", "Enter library ID: ")
        user = next((user for user in library["users"] if user.get_library_id() == library_id), None)
        if user:
            print(user)
        else:
            print("User not found.")

    elif choice == "3":
        print("\nList of Users:")
        for user in library["users"]:
            print(user)

def author_operations(library):
    print("Author Operations:")
    print("1. Add a new author")
    print("2. View author details")
    print("3. Display all authors")
    choice = validate_input(r"^[1-3]$", "Enter your choice: ")

    if choice == "1":
        name = validate_input(r"^[\w\s]+$", "Enter author name: ")
        biography = input("Enter biography: ")
        author = Author(name, biography)
        library["authors"].append(author)
        print(f"Author '{name}' added successfully!")

    elif choice == "2":
        name = validate_input(r"^[\w\s]+$", "Enter author name: ")
        author = next((author for author in library["authors"] if author.get_name() == name), None)
        if author:
            print(author)
        else:
            print("Author not found.")

    elif choice == "3":
        print("List of Authors:")
        for author in library["authors"]:
            print(author)

if __name__ == "__main__":
    library = {
        "books": [],
        "users": [],
        "authors": []
    }

    while True:
        choice = main_menu()
        if choice == "1":
            book_operations(library)
        elif choice == "2":
            user_operations(library)
        elif choice == "3":
            author_operations(library)
        elif choice == "4":
            print("Exiting the Library Management System.")
            break