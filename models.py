class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email


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