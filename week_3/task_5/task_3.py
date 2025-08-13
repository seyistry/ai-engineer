"""**Task3: Tuple Operations**
	- Create a tuple of 5 Nigerian states entered by the user.

	- Print the first state and last state.

	- Check if "Lagos" is in the tuple and print "Yes" or "No".

	- Print the number of states entered.
	- (Hint: use the tuple membership)
"""

# Implementation
states = (
    input("Enter the name of the first Nigerian state: "),
    input("Enter the name of the second Nigerian state: "),
    input("Enter the name of the third Nigerian state: "),
    input("Enter the name of the fourth Nigerian state: "),
    input("Enter the name of the fifth Nigerian state: ")
)

# Print the first state and last state
print("The first state is:", states[0])
print("The last state is:", states[-1])

# Check if "Lagos" is in the tuple
if "Lagos" in states:
    print("Yes")
else:
    print("No")

# Print the number of states entered
print("Number of states entered:", len(states))
