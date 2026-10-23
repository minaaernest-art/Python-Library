import sqlite3


def save_library_to_sqlite(library, database_name="library.db"):
    connection = sqlite3.connect(database_name)

    try:
        connection.execute("PRAGMA foreign_keys = ON")

        connection.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS books (
                book_id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category_id INTEGER NOT NULL,
                available_copies INTEGER NOT NULL CHECK (available_copies >= 0),
                FOREIGN KEY (category_id) REFERENCES categories(category_id)
            );

            CREATE TABLE IF NOT EXISTS ratings (
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                score INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
                review TEXT,
                PRIMARY KEY (user_id, book_id),
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            );

            CREATE TABLE IF NOT EXISTS reading_history (
                user_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id),
                FOREIGN KEY (book_id) REFERENCES books(book_id)
            );
        """)

        # نحذف البيانات القديمة بالترتيب المناسب قبل حفظ نسخة المكتبة الحالية.
        connection.execute("DELETE FROM reading_history")
        connection.execute("DELETE FROM ratings")
        connection.execute("DELETE FROM books")
        connection.execute("DELETE FROM categories")
        connection.execute("DELETE FROM users")

        connection.executemany(
            "INSERT INTO users (user_id, name, email) VALUES (?, ?, ?)",
            [(u.user_id, u.name, u.email) for u in library.users],
        )

        connection.executemany(
            "INSERT INTO categories (category_id, name) VALUES (?, ?)",
            [(c.category_id, c.name) for c in library.categories],
        )

        connection.executemany(
            """INSERT INTO books
               (book_id, title, author, category_id, available_copies)
               VALUES (?, ?, ?, ?, ?)""",
            [
                (b.book_id, b.title, b.author, b.category_id, b.available_copies)
                for b in library.books
            ],
        )

        connection.executemany(
            "INSERT INTO ratings (user_id, book_id, score, review) VALUES (?, ?, ?, ?)",
            [
                (r.user_id, r.book_id, r.score, r.review)
                for r in library.ratings
            ],
        )

        connection.executemany(
            """INSERT INTO reading_history (user_id, book_id, date, status)
               VALUES (?, ?, ?, ?)""",
            [
                (
                    record.user_id,
                    record.book_id,
                    record.date.isoformat(),
                    record.status.value,
                )
                for record in library.reading_history
            ],
        )

        connection.commit()

    finally:
        connection.close()