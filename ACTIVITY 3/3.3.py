import os
os.makedirs("ACTIVITY 3", exist_ok=True)

lname = input("Enter your last name: ")
fname = input("Enter your first name: ")
age = input("Enter your age: ")
num = input("Enter contact number: ")
course = input("Enter course: ")

student_info = (
    f"Last Name: {lname}\n"
    f"First Name: {fname}\n"
    f"Age: {age}\n"
    f"Contact Number: {num}\n"
    f"Course: {course}\n\n"
)

with open("ACTIVITY 3/students.txt", "a") as file:
    file.write(student_info)

print("Student information has been saved to 'ACTIVITY 3/students.txt'.")
