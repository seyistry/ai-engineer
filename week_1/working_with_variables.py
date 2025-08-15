"""
This script demonstrates basic variable usage in Python.
"""

# Define variables
name = "Alice"
age = 30
height = 5.5

# Print variables
print("Name:", name)
print("Age:", age)
print("Height:", height)

int_age = int(age)
print("Age as integer:", int_age)

# float()

# str()

# bool()


# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")