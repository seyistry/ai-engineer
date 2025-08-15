"""Task1: Student Bio Data Storage

- Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.

- Courses should be stored as a list.

- Display the bio-data neatly using escape sequences.

- Requirements:

- Use `input()` to collect details.

- Use dictionary operations `(dict[key] = value)` to store data.

- Use `print()` formatting with `\n` and `\t` for better output.
"""

# Implementation
student_bio = {}

# Collect student details
student_bio["Name"] = input("Enter student's name: ")
student_bio["Age"] = input("Enter student's age: ")
student_bio["Gender"] = input("Enter student's gender: ")

# Collect courses
courses = []
while True:
    course = input("Enter a course (or 'done' to finish): ")
    if course.lower() == 'done':
        break
    courses.append(course)
student_bio["Courses"] = courses

# Display bio-data
print("\nStudent Bio Data:")
for key, value in student_bio.items():
    print(f"{key}:\t{value}")