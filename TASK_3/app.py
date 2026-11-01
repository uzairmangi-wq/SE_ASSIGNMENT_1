
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Uzair Mangi", "department": "IT"},
    {"id": 2, "name": "Ali Ahmed", "department": "HR"}
]

users = {
    "employee": {
        "password": "emp123",
        "role": "Employee"
    },
    "admin": {
        "password": "admin123",
        "role": "Administrator"
    }
}

tokens = {}


# Check login and role
def login_required(admin_only=False):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            token = request.headers.get("Authorization")

            if not token or token not in tokens:
                return jsonify({"error": "Please login first"}), 401

            if admin_only and tokens[token] != "Administrator":
                return jsonify({"error": "Admin access required"}), 403

            return function(*args, **kwargs)

        return wrapper

    return decorator


# Login endpoint
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Username and password required"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users or users[username]["password"] != password:
        return jsonify({"error": "Invalid username or password"}), 401

    token = username + "_token"
    tokens[token] = users[username]["role"]

    return jsonify({
        "message": "Login successful",
        "role": users[username]["role"],
        "token": token
    })


# View employees - Both roles
@app.route("/employees", methods=["GET"])
@login_required()
def view_employees():

    return jsonify(employees)


# Add employee - Admin only
@app.route("/employees", methods=["POST"])
@login_required(admin_only=True)
def add_employee():

    data = request.get_json()

    if not data or "name" not in data or "department" not in data:
        return jsonify({"error": "Name and department required"}), 400

    new_id = max([employee["id"] for employee in employees], default=0) + 1

    employee = {
        "id": new_id,
        "name": data["name"],
        "department": data["department"]
    }

    employees.append(employee)

    return jsonify({
        "message": "Employee added successfully",
        "employee": employee
    }), 201


# Update employee - Admin only
@app.route("/employees/<int:employee_id>", methods=["PUT"])
@login_required(admin_only=True)
def update_employee(employee_id):

    data = request.get_json()

    for employee in employees:

        if employee["id"] == employee_id:

            employee["name"] = data.get("name", employee["name"])
            employee["department"] = data.get("department", employee["department"])

            return jsonify({"message": "Employee updated", "employee": employee})

    return jsonify({"error": "Employee not found"}), 404


# Delete employee - Admin only
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
@login_required(admin_only=True)
def delete_employee(employee_id):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return jsonify({"message": "Employee deleted successfully"})

    return jsonify({"error": "Employee not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5002)
