#Library 
# Parent class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        print("Title :", self.title)
        print("Author :", self.author)


# Child class
class IssuedBook(Book):
    def __init__(self, title, author, issued_to, issued_date):
        super().__init__(title, author)   # Calling parent constructor
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_issued_book_details(self):
        self.display_book_details()   # Calling parent method
        print("Issued To :", self.issued_to)
        print("Issued Date :", self.issued_date)


# Creating object for IssuedBook
issued_book1 = IssuedBook("The God of Small Things ","Arundhati Roy","Shreelakshmi H","03-02-2026")

# Display
issued_book1.display_issued_book_details()
