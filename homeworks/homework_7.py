import sqlite3

def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("""
         CREATE TABLE IF NOT EXISTS books (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             author TEXT,
             publication_year INTEGER,
             genre TEXT,
             number_of_pages INTEGER,
             number_of_copies INTEGER
        )
    """)


def add_book(name,author,publication_year,genre,number_of_pages, number_of_copies):
    conn.execute(
        "INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?,?,?,?,?,?)",
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def delete_book(book_id):
    conn.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")

    create_table()

    add_book("Martin Iden","Jack London", 1909, "Roman",500, 1000000)
    add_book("Вишневый сад", "А.П. Чехов", 1903, "Пьеса", 90, 900000)

    delete_book(2)

    conn.close()