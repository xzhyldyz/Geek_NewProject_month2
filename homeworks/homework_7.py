import sqlite3

def create_table():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("DROP TABLE IF EXISTS genres")
    conn.execute("""
         CREATE TABLE IF NOT EXISTS books (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             author TEXT,
             publication_year INTEGER,
             number_of_pages INTEGER,
             number_of_copies INTEGER,
             genre_id INTEGER,
             FOREIGN KEY(genre_id)
             REFERENCES genres(id)
        )
    """)
    conn.execute("""
    CREATE TABLE genres (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

def add_book(name,author,publication_year,genre,number_of_pages, number_of_copies):
    conn.execute(
        "INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies) VALUES (?,?,?,?,?)",
        (name, author, publication_year, number_of_pages, number_of_copies)
    )
    conn.commit()

def delete_book(book_id):
    conn.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,))
    conn.commit()

def add_genre(name):
    conn.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()

def get_all_books():
    result = conn.execute("SELECT * FROM "
                          "books JOIN genres ON books.genre_id = genres.id ORDER BY books.id")
    return result.fetchall()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")

    create_table()

    add_genre("Роман")
    add_genre("Повесть")
    add_genre("Психология")

    add_book("Martin Iden","Jack London", 1909,1, 500, 1000000)
    add_book("Вишневый сад", "А.П. Чехов", 1903, 2, 90, 900000)
    add_book("Лисы в винограднике", "Л. Фейхтвангер", 1947, 1, 550, 800000)
    add_book("Первый учитель", "Ч. Айтматов", 1962, 2, 120, 700000)
    add_book("Белый клык", "Джек Лондон", 1906, 1, 350, 600000)
    add_book("Война и мир", "Л. Толстой", 1869, 1, 1500, 2000000)
    add_book("Как завоевать друзей ...", "Д. Карнеги", 1936, 3, 300, 500000)
    add_book("До встречи с тобой", "Д. Мойес", 2012, 1, 500, 400000)
    add_book("Бегущий за ветром", "Х. Хоссейн", 2003, 1, 390, 300000)
    add_book("Атомные привычки", "Д. Клир", 2018, 3, 320, 200000)

    delete_book(2)
    delete_book(7)

    print(get_all_books())

    conn.close()