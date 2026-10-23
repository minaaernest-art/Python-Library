class Library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_user(self, user):
        self.users.append(user)

    def add_book(self, book):
        self.books.append(book)

    def display_users(self):
        for user in self.users:
            print(f"{user.user_id}: {user.name} - {user.email}")

    def display_books(self):
        for book in self.books:
            print(
                f"{book.book_id}: {book.title} by {book.author} "
                f"(available copies: {book.available_copies})"
            )