"""Task1: Fruit collector
- Ask the user to enter 5 favourite fruits. Store them in a set and display the set.
"""

#Implementation
fruits = set()
for i in range(5):
    fruit = input("Enter your favourite fruit: ")
    fruits.add(fruit)
print("Your favourite fruits are:", fruits)