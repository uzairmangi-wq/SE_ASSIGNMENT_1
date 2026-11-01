
import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/students"

st.title("Student Management System")
st.write("Manage Student Records")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["View Students", "Add Student", "Update Student", "Delete Student"]
)

if menu == "View Students":
    st.subheader("All Students")

    response = requests.get(API_URL)

    if response.status_code == 200:
        students = response.json()
        st.dataframe(students)

elif menu == "Add Student":
    st.subheader("Add New Student")

    name = st.text_input("Student Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    if st.button("Add Student"):
        data = {
            "name": name,
            "department": department,
            "email": email
        }

        response = requests.post(API_URL, json=data)

        if response.status_code == 201:
            st.success("Student added successfully!")
        else:
            st.error(response.json().get("error", "Something went wrong"))

elif menu == "Update Student":
    st.subheader("Update Student")

    student_id = st.number_input("Student ID", min_value=1, step=1)
    name = st.text_input("New Name")
    department = st.text_input("New Department")
    email = st.text_input("New Email")

    if st.button("Update Student"):
        data = {
            "name": name,
            "department": department,
            "email": email
        }

        response = requests.put(
            f"{API_URL}/{student_id}",
            json=data
        )

        if response.status_code == 200:
            st.success("Student updated successfully!")
        else:
            st.error(response.json().get("error", "Something went wrong"))

elif menu == "Delete Student":
    st.subheader("Delete Student")

    student_id = st.number_input("Student ID", min_value=1, step=1)

    if st.button("Delete Student"):
        response = requests.delete(f"{API_URL}/{student_id}")

        if response.status_code == 200:
            st.success("Student deleted successfully!")
        else:
            st.error(response.json().get("error", "Something went wrong"))
