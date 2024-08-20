class Book:
    def __init__(self, title, author, genre, publication_date):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__is_available = True

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def is_available(self):
        return self.__is_available

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):
        self.__is_available = True

    def __str__(self):
        status = "Available" if self.__is_available else "Borrowed"
        return f"Title: {self.__title}, Author: {self.__author}, Genre: {self.__genre}, " \
               f"Publication Date: {self.__publication_date}, Status: {status}"