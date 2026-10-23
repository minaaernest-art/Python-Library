from models import User, Book
from library import Library

library = Library()

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)

library.add_user(user)
library.add_book(book)

results = library.search_books("title", "clean")

print("Search results:")
for book in results:
    print(f"{book.title} by {book.author}")