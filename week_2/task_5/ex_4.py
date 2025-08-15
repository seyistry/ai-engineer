"""**Task4: Tuple Unpacking**
	- Ask a user for their;

	- First name

	- Age

	- Favorite color

	- Home town

	- Store them in a tuple profile and unpack into variables.

	- Print and use  escape sequence to align each piece of information nicely.
"""

# Implementation
profile = (
    input("Enter your first name: "),
    input("Enter your age: "),
    input("Enter your favorite color: "),
    input("Enter your home town: ")
)

# Unpack the tuple into variables
first_name, age, favorite_color, home_town = profile

# Print the information with alignment
print("Profile Information:")
print(f"First Name:      {first_name}")
print(f"Age:            {age}")
print(f"Favorite Color: {favorite_color}")
print(f"Home Town:     {home_town}")
