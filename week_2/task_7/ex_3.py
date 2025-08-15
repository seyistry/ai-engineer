"""Task3: Days and Activities Pairing
- Store days of the week in a tuple and ask the user to input an activity for three specific days.

- Use dictionary comprehension to pair days and activities.

- Print the dictionary.

- Requirements:

- Use a tuple for days.

- Use {day: activity for day, activity in `zip(..., ...)`}.
Tip: Research on how to use `zip()`
"""

# Implementation
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
activities = []

# Get activities for specific days
for day in days[:3]:  # Only for the first three days
    activity = input(f"Enter an activity for {day}: ")
    activities.append(activity)

# Pair days and activities using dictionary comprehension
day_activity = {day: activity for day, activity in zip(days[:3], activities)}

# Print the dictionary
print("\nDays and Activities:")
for day, activity in day_activity.items():
    print(f"{day}: {activity}")
