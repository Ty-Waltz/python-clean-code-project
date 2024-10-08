
class User:
        def __init__(self, name, library_id):
            self.__name = name
            self.__library_id = library_id
            self.__borrowed_books = []

        def get_name(self):
            return self.__name

        def get_library_id(self):
            return self.__library_id

        def borrow_book(self, book):
            if book.is_available():
                book.borrow()
                self.__borrowed_books.append(book.get_title())
                return True
            return False

        def return_book(self, book):
            if book.get_title() in self.__borrowed_books:
                book.return_book()
                self.__borrowed_books.remove(book.get_title())
                return True
            return False

        def __str__(self):
            books = ', '.join(self.__borrowed_books) if self.__borrowed_books else "No books borrowed"
            return f"Name: {self.__name}, Library ID: {self.__library_id}, Borrowed Books: {books}"
        
      
    
        def save_to_db(self, cursor):
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            values = (self.name, self.library_id)
            cursor.execute(query, values)