from models import User, Book
from library import Library
from models import User, Book, Rating

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

rating = Rating(user.user_id, book.book_id, 9, "A very useful book")
library.add_rating(rating)

average = library.calculate_average_rating(book.book_id)
print("Average rating:", average)   
print("Popular authors:", library.most_popular_authors())
print("Popular categories:", library.most_popular_categories())

print("\nRecommended books:")
for book in library.recommend_books(user.user_id):
    print(book.title) 

    book2 = Book(2, "The Pragmatic Programmer", "Andrew Hunt", 1, 2)
    library.add_book(book2)