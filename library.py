class Library:
    def __init__(self):
        self.users = []
        self.books = []
        self.categories = []

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