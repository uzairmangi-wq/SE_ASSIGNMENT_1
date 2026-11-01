
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def create_database():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return "Student Management API is Running!"


# GET: Retrieve all students
@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()
    conn.close()

    student_list = []

    for student in students:
        student_list.append(dict(student))

    return jsonify(student_list)


# GET: Retrieve a specific student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))

    student = cursor.fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))


# POST: Add a new student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    department = data.get("department")
    email = data.get("email")

    if not name or not department or not email:
        return jsonify({"error": "All fields are required"}), 400

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, department, email) VALUES (?, ?, ?)",
        (name, department, email)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully"}), 201


# PUT: Update an existing student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get("name")
    department = data.get("department")
    email = data.get("email")

    if not name or not department or not email:
        return jsonify({"error": "All fields are required"}), 400

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, department=?, email=? WHERE id=?",
        (name, department, email, id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    conn.close()

    return jsonify({"message": "Student updated successfully"})


# DELETE: Remove a student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return jsonify({"error": "Student not found"}), 404

    conn.close()

    return jsonify({"message": "Student deleted successfully"})


if __name__ == "__main__":
    create_database()
    app.run(debug=True)
