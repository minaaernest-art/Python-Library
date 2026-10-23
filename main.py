from models import User, Book
from library import Library

library = Library()

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)

library.add_user(user)
library.add_book(book)

library.borrow_book(user.user_id, book.book_id)
library.complete_book(user.user_id, book.book_id)

print("Reading history:")
library.display_reading_history(user.user_id) 

print("\nBooks already read:")
for book in library.get_completed_books(user.user_id):
    print(book.title)