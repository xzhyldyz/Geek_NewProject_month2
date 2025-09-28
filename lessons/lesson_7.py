import sqlite3

def crate_table():
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
         CREATE TABLE IF NOT EXISTS students (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             age INTEGER,
             city TEXT
        )
    """)

def add_student(name, age, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)",
        (name, age, city)
    )
    conn.commit()

def delete_student(student_id):
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,))
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect("database.db")

    crate_table()
    
    add_student("Aibek", 23, "Bishkek")
    add_student("Aisulu", 19, "Karakol")

    delete_student(1)

    conn.close()

