"""**Task4: Student Record**
- Create an empty dictionary called student.

- Ask the user to input their name and age, then store them in the dictionary.

- Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

- Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

- Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

- Print out the complete record in this format:

```
Student Record:
Name: John
Age: 16
Scores: [70, 85, 90]
Passed: True
Teenager: True
```
"""

# Create an empty dictionary to store student information
student = {}

# Get student details
student['name'] = input("Enter your name: ")
student['age'] = int(input("Enter your age: "))
student['scores'] = [int(x) for x in input("Enter your scores (comma-separated): ").split(",")]

# Calculate average score and determine pass status
average_score = sum(student['scores']) / len(student['scores'])
student['passed'] = average_score >= 50

# Check if the student is a teenager (age between 13 and 19 inclusive)
student['teenager'] = 13 <= student['age'] <= 19

# Print the complete student record
print("Student Record:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")