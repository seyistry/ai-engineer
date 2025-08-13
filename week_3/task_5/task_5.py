"""**Task5: Modify Tuple Indirectly**
	- Ask a user to enter three items for their shopping list.

	- Store in a tuple shopping_list.

	- Convert it to a list, then ask for two more items to add.

	- Convert back to a tuple and print the updated list using join() to display items separated by " | ".
"""

# Implementation
shopping_list = (
    input("Enter the first item for your shopping list: "),
    input("Enter the second item for your shopping list: "),
    input("Enter the third item for your shopping list: ")
)

# Convert to a list and add two more items
shopping_list = list(shopping_list)
shopping_list.append(input("Enter the fourth item for your shopping list: "))
shopping_list.append(input("Enter the fifth item for your shopping list: "))

# Convert back to a tuple
shopping_list = tuple(shopping_list)

# Print the updated shopping list
print("Updated Shopping List:")
print(" | ".join(shopping_list))
