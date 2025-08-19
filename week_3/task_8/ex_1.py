
"""
Task1
- Explain each output of the program below.
- Give 3 usecases or scenarios where you can apply the program below.
- Write the code for 1 of the 3 use cases.

Explanation of outputs:
1. num1 == num2 : Checks if the two numbers are equal.
2. num1 != num2 : Checks if the two numbers are not equal.
3. num1 > num2  : Checks if the first number is greater than the second.
4. num1 < num2  : Checks if the first number is less than the second.

Use cases:
1. User Age Verification
2. Score Comparison
3. Inventory Check

Below is the code for the 'Score Comparison' use case:
"""


# Score Comparison Example
score1 = int(input("Enter score for Student 1: "))
score2 = int(input("Enter score for Student 2: "))

# Check if scores are equal
# True if both students have the same score
print(f"Student 1 == Student 2 : {score1 == score2}")
# Check if scores are not equal
# True if scores are different
print(f"Student 1 != Student 2 : {score1 != score2}")
# Check if Student 1 scored higher
# True if Student 1 scored higher
print(f"Student 1 > Student 2 : {score1 > score2}")
# Check if Student 1 scored lower
# True if Student 1 scored lower
print(f"Student 1 < Student 2 : {score1 < score2}")
