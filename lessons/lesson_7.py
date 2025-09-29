import sqlite3



def create_table():
    conn.execute("DROP TABLE IF EXISTS students")

    conn.execute("""
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)
    conn.execute("""
         CREATE TABLE IF NOT EXISTS students (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             age INTEGER,
             city TEXT,
             department_id INTEGER,
             FOREIGN KEY(department_id)
             REFERENCES department(id)
        )
    """)

def add_student(name, age, city, department_id):
    conn.execute(
        "INSERT INTO students (name: str, age: int, city: str, department_id: int) VALUES (?, ?, ?)",
        (name, age, city, department_id)
    )
    conn.commit()

def delete_student(student_id: int):
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,))
    conn.commit()

def get_all_students():
    result = conn.execute("SELECT name, age FROM students ORDER BY age LIMIT 2")
    return result.fetchall()

def get_student(name: str):
    result = conn.execute("SELECT * FROM students WHERE name = ?", (name,))
    return result.fetchall()

def update_student(student_id: int, new_name: str):
    conn.execute("UPDATE students SET name = ? WHERE id = ?", (new_name, student_id))

def add_department(name: str):
    conn.execute("INSERT INTO department (name) VALUES (?)", (name,))
    conn.commit()

if __name__ == '__main__':
    conn = sqlite3.connect("database.db")

    create_table()

    add_department("Backend")
    add_department("Frontend")
    
    add_student("Aibek", 23, "Bishkek", 1)
    add_student("Aisulu", 19, "Karakol", 2)
    add_student("Maksat", 22, "Bishkek", 1)

    delete_student(1)
    update_student(4, "Meerim")

    print(get_all_students())

    conn.close()