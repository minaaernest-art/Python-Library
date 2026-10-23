from models import User, Book, Rating

user = User(1, "Ahmed", "ahmed@example.com")
book = Book(1, "Clean Code", "Robert C. Martin", 1, 3)
rating = Rating(user.user_id, book.book_id, 9, "A very useful book")

print("User:", user.name)
print("Book:", book.title)
print("Rating:", rating.score)
print("Review:", rating.review)