from models import User, Book, Rating
from library import Library

library = Library()

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)
rating = Rating(user.user_id, book.book_id, 9, "A very useful book")

library.add_user(user)
library.add_book(book)
library.add_rating(rating)

library.display_ratings()