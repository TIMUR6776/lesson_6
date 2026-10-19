import sqlite3

DB_NAME = 'univercity.db'

def create_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            mark REAL,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_into(name, mark, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, mark, age) VALUES (?, ?, ?)",
        (name, mark, age)
    )
    conn.commit()
    conn.close()

def update_info():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age = 25 WHERE id = 3")
    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE age = 41")
    conn.commit()
    conn.close()

def get_students_by_age(age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE age > ?", (age,))
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    create_db()
    insert_into('Иванов', 65, 18)
    insert_into('Лукашов', 5, 19)
    update_info()
    delete()

    print("Студенты старше 18:")
    for student in get_students_by_age(18):
        print(student)