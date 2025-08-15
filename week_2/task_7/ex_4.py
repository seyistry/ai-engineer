"""Task4: Unique Members Registration
- Ask the user to enter three names separated by commas.

- Convert them to a set to ensure uniqueness.

- Create a dictionary where each name is a key and its length is the value.

- Requirements:

- Use `.split(",")` and `set()` to remove duplicates.

- Use dictionary comprehension `{name: len(name) for name in set_of_names}`.
"""

# Implementation
names_input = input("Enter three names separated by commas: ")
set_of_names = set(names_input.split(","))

# Create dictionary with name lengths
name_lengths = {name.strip(): len(name.strip()) for name in set_of_names}

# Print the dictionary
print("\nUnique Members and their Name Lengths:")
for name, length in name_lengths.items():
    print(f"{name}: {length}")
