"""**Task6: Attendance Tracker**
	- Write a Python program that;

	- Stores the days of the week in a tuple.

	- Stores the months of the year in another tuple.

	- Asks the user to enter:

	- Student's name

	- Gender

	- Course Track

	- Current month number (1-12)

	- Current day number (1-7)

"""
# Implementation

# Store days of the week and months of the year in tuples
days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Get user input
student_name = input("Enter student's name: ")
gender = input("Enter gender: ")
course_track = input("Enter course track: ")

month_num = int(input("Enter current month number (1-12): "))

day_num = int(input("Enter current day number (1-7): "))

# Display attendance information
print("\nAttendance Record")
print(f"Name: {student_name}")
print(f"Gender: {gender}")
print(f"Course Track: {course_track}")
print(f"Month: {months_of_year[month_num - 1]}")
print(f"Day: {days_of_week[day_num - 1]}")