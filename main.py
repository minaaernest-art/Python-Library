from models import Book, Category
from library import Library

library = Library()

category = Category(1, "Programming")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)

library.add_category(category)
library.add_book(book)

results = library.search_books("category", "programming")

print("Search results:")
for book in results:
    print(f"{book.title} by {book.author}")