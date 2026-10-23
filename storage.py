import json
from pathlib import Path


def save_library(library, filename="library_data.json"):
    data = {
        "users": [
            {
                "user_id": user.user_id,
                "name": user.name,
                "email": user.email,
            }
            for user in library.users
        ],
        "categories": [
            {
                "category_id": category.category_id,
                "name": category.name,
            }
            for category in library.categories
        ],
        "books": [
            {
                "book_id": book.book_id,
                "title": book.title,
                "author": book.author,
                "category_id": book.category_id,
                "available_copies": book.available_copies,
            }
            for book in library.books
        ],
        "ratings": [
            {
                "user_id": rating.user_id,
                "book_id": rating.book_id,
                "score": rating.score,
                "review": rating.review,
            }
            for rating in library.ratings
        ],
        "reading_history": [
            {
                "user_id": record.user_id,
                "book_id": record.book_id,
                "date": record.date.isoformat(),
                "status": record.status.value,
            }
            for record in library.reading_history
        ],
    }

    Path(filename).write_text(
        json.dumps(data, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


def load_library(library, filename="library_data.json"):
    from datetime import datetime
    from models import User, Category, Book, Rating, ReadingRecord, ReadingStatus

    data = json.loads(Path(filename).read_text(encoding="utf-8"))

    library.users = [
        User(item["user_id"], item["name"], item["email"])
        for item in data["users"]
    ]

    library.categories = [
        Category(item["category_id"], item["name"])
        for item in data["categories"]
    ]

    library.books = [
        Book(
            item["book_id"],
            item["title"],
            item["author"],
            item["category_id"],
            item["available_copies"],
        )
        for item in data["books"]
    ]

    library.ratings = [
        Rating(item["user_id"], item["book_id"], item["score"], item["review"])
        for item in data["ratings"]
    ]

    library.reading_history = []

    for item in data["reading_history"]:
        record = ReadingRecord(
            item["user_id"],
            item["book_id"],
            ReadingStatus(item["status"]),
        )
        record.date = datetime.fromisoformat(item["date"])
        library.reading_history.append(record)

    return library