class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

class Library:

    def __init__(self):
        self._books = []

    def add_book(self):
        self._books.append(Book)

    def check_out_book(self,title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return True
                else:
                    return False
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return True
                else:
                    return False
        return False

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
                
