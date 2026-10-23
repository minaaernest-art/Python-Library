from models import Rating
from models import ReadingRecord, ReadingStatus
class Library:
    def __init__(self):
        self.users = []
        self.books = []
        self.categories = []
        self.ratings = []
        self.reading_history = []

    def add_user(self, user):
        self.users.append(user)

    def add_book(self, book):
        self.books.append(book)

    def add_category(self, category):
        self.categories.append(category)

    def get_category_name(self, category_id):
        for category in self.categories:
            if category.category_id == category_id:
                return category.name
        return ""

    def search_books(self, search_type, query):
        query = query.strip().lower()
        results = []

        for book in self.books:
            if search_type == "title" and query in book.title.lower():
                results.append(book)

            elif search_type == "author" and query in book.author.lower():
                results.append(book)

            elif search_type == "category":
                category_name = self.get_category_name(book.category_id).lower()
                if query in category_name:
                    results.append(book)

        return results
    
    def add_rating(self, rating):
       user_exists = any(user.user_id == rating.user_id for user in self.users)
       book_exists = any(book.book_id == rating.book_id for book in self.books)

       if not user_exists:
          raise ValueError("User does not exist.")

       if not book_exists:
          raise ValueError("Book does not exist.")

       for existing_rating in self.ratings:
           if (
              existing_rating.user_id == rating.user_id
              and existing_rating.book_id == rating.book_id
         ):
              raise ValueError("This user has already rated this book.")

       self.ratings.append(rating)

    def display_ratings(self):
       for rating in self.ratings:
          print(
            f"User {rating.user_id} rated book {rating.book_id}: "
            f"{rating.score}/10 - {rating.review}"
            )   
    
    def borrow_book(self, user_id, book_id):
      user_exists = any(user.user_id == user_id for user in self.users)
      book = next((book for book in self.books if book.book_id == book_id), None)

      if not user_exists:
          raise ValueError("User does not exist.")
      if book is None:
        raise ValueError("Book does not exist.")
      if book.available_copies <= 0:
        raise ValueError("No copies are available.")

      book.available_copies -= 1
      record = ReadingRecord(user_id, book_id, ReadingStatus.BORROWED)
      self.reading_history.append(record)


    def complete_book(self, user_id, book_id):
      for record in self.reading_history:
        if (
            record.user_id == user_id
            and record.book_id == book_id
            and record.status == ReadingStatus.BORROWED
        ):
            record.status = ReadingStatus.COMPLETED
            return

      raise ValueError("No borrowed record found for this user and book.")      
    
    def display_reading_history(self, user_id):
      for record in self.reading_history:
        if record.user_id == user_id:
            print(
                f"Book ID: {record.book_id}, "
                f"Date: {record.date.strftime('%Y-%m-%d %H:%M')}, "
                f"Status: {record.status.value}"
            )