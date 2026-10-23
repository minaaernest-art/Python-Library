class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Email must contain @ and a dot.")
        self._email = value


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


class Book:
    def __init__(self, book_id, title, author, category_id, available_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category_id = category_id
        self.available_copies = available_copies

    @property
    def available_copies(self):
        return self._available_copies

    @available_copies.setter
    def available_copies(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Available copies must be a non-negative integer.")
        self._available_copies = value

        class Rating:
             def __init__(self, user_id, book_id,score, review):
              self.user_id = user_id
              self.book_id = book_id
              self.score = score
              self.review = review

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or not 1 <= value <= 10:
            raise ValueError("Rating score must be an integer from 1 to 10.")
        self._score = value

class Rating:
    def __init__(self, user_id, book_id, score, review):
        self.user_id = user_id
        self.book_id = book_id
        self.score = score
        self.review = review

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int) or not 1 <= value <= 10:
            raise ValueError("Rating score must be an integer from 1 to 10.")
        self._score = value      