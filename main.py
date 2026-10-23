from models import User, Book

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)

print("User:", user.name, "-", user.email)
print("Book:", book.title, "-", book.author)
print("Available copies:", book.available_copies)