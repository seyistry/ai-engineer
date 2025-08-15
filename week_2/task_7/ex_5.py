"""Task5: Contact Quick Lookup
- Store three names and their phone numbers in two separate tuples.

- Create a dictionary from them using `dict(zip(...))`.

- Ask the user for a name and display the corresponding number (or an error message).

- Requirements:

- Use `zip()` and d`ict()` to combine tuples.

- Use `.get()` for safe retrieval.

- No loops.
"""

# Implementation
names = ("Alice", "Bob", "Charlie")
phone_numbers = ("123-456-7890", "987-654-3210", "555-555-5555")

# Create dictionary using zip
phone_book = dict(zip(names, phone_numbers))

# Lookup
name_to_lookup = input("Enter a name to lookup: ")
print(f"Phone number for {name_to_lookup}: {phone_book.get(name_to_lookup, 'Not found')}")
