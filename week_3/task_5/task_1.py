"""Create and Display
	- Ask the user to enter three favorite Nigerian dishes (one at a time).

	- Store them in a tuple called dishes.

	- Print the tuple in a single line, separating items with commas.

	- Use the \n escape sequence to print each dish on a new line.
"""

# Implementation
dishes = (
    input("Enter your first favorite Nigerian dish: "),
    input("Enter your second favorite Nigerian dish: "),
    input("Enter your third favorite Nigerian dish: ")
)

# Print the tuple in a single line
print("Your favorite Nigerian dishes are:")
print(", ".join(dishes))

# Print each dish on a new line
print("\n".join(dishes))