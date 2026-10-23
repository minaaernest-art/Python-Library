from models import User, Book
from library import Library
from models import User, Book, Rating
from storage import save_library, load_library
from models import User, Book, Rating, Category
from sqlite_storage import save_library_to_sqlite, load_library_from_sqlite

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

save_library(library)

new_library = Library()
load_library(new_library)

print("Loaded books:")
for book in new_library.books:
    print(f"{book.title} by {book.author} (copies: {book.available_copies})")
    print("\nRecommended books:")

category = Category(1, "Programming")
library.add_category(category)

save_library_to_sqlite(library)

loaded_library = Library()
load_library_from_sqlite(loaded_library)

print("Books loaded from SQLite:")
for book in loaded_library.books:
    print(book.title)