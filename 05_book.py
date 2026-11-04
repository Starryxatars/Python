class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Book ID : {self.book_id}")
        print(f"Title   : {self.title}")
        print(f"Author  : {self.author}")
        print(f"Price   : Rs. {self.price:.2f}")
        print("-" * 35)


b1 = Book(101, "Python Crash Course", "Eric Matthes", 599.00)
b2 = Book(102, "Wings of Fire", "A. P. J. Abdul Kalam", 250.00)
b3 = Book(103, "Clean Code", "Robert C. Martin", 899.50)

for b in (b1, b2, b3):
    b.display()
