# Class Definition
class Book:
    
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available

    #to display book details
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print("---------------------------")

    #to issue books
    def issue_book(self, quantity):
        if quantity <= self.copies_available:
            self.copies_available -= quantity
            print(quantity, "copies issued successfully.")
        else:
            print("Not enough copies available")

    #to add copies
    def add_copies(self, quantity):
        self.copies_available += quantity
        print(quantity, "copies added successfully.")

    #o calculate total value
    def book_value(self):
        return self.price * self.copies_available


# Main Program


book1 = Book(201, "Introduction to Artificial Intelligence", "Stuart Russell", 880, 6)
book2 = Book(202, "Fundamentals of Database Systems", "Ramez Elmasri", 990, 4)
book3 = Book(203, "Computer Networks Essentials", "Larry Peterson", 760, 7)

library = [book1, book2, book3]

print("Library Collection")
print("=================")
for book in library:
    book.display_book()

# Issue copies
print("Issuing Books")
book1.issue_book(3)

# Add copies
print("Adding Copies")
book2.add_copies(1)

# Display updated books
print("\nUpdated Book Details")
for book in library:
    book.display_book()

# Calculate total library value
total_value = 0
for book in library:
    total_value += book.book_value()

print("Total value of all books in library:", total_value)