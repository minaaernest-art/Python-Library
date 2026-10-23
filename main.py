from models import User, Book
from library import Library

library = Library()

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)

library.add_user(user)
library.add_book(book)

print("Users:")
library.display_users()

print("\nBooks:")
library.display_books()