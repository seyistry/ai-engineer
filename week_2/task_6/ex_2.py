"""Task2: Unique Name Collector
- Write a program that collects the names of people
  attending a seminar (no duplicates allowed) 
  and displays them in alphabetical order.
"""

# Implementation
names = set()
while True:
    name = input("Enter the name of an attendee (or 'done' to finish): ")
    if name.lower() == 'done':
        break
    names.add(name)
print("Attendees:", sorted(names))
