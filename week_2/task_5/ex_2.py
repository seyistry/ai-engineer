"""**Task2: Tuple and Input**

	- Ask the user for 5 best friends' names.

	- Store them in a tuple friends.

	- Print the tuple in reverse order.
"""

# Implementation
friends = (
    input("Enter the name of your first best friend: "),
    input("Enter the name of your second best friend: "),
    input("Enter the name of your third best friend: "),
    input("Enter the name of your fourth best friend: "),
    input("Enter the name of your fifth best friend: ")
)

# Print the tuple in reverse order
print("Your best friends' names in reverse order are:")
print(friends[::-1])
