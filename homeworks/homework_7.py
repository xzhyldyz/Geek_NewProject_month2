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
    add_book("Лисы в винограднике", "Л. Фейхтвангер", 1947, "Роман", 550, 800000)
    add_book("Первый учитель", "Ч. Айтматов", 1962, "Повесть", 120, 700000)
    add_book("Белый клык", "Джек Лондон", 1906, "Роман", 350, 600000)
    add_book("Война и мир", "Л. Толстой", 1869, "Роман", 1500, 2000000)
    add_book("Как завоевать друзей ...", "Д. Карнеги", 1936, "Психология", 300, 500000)
    add_book("До встречи с тобой", "Д. Мойес", 2012, "Роман", 500, 400000)
    add_book("Бегущий за ветром", "Х. Хоссейн", 2003, "Роман", 390, 300000)
    add_book("Атомные привычки", "Д. Клир", 2018, "Саморазвитие", 320, 200000)

    delete_book(2)
    delete_book(7)

    conn.close()