"""Task3: Simulate a football match ticket system

- Store all seat numbers (1 to 50) in a set.

- Ask users to "book" a seat by entering the number.

- Remove booked seats from the set.

- Show remaining seats after each booking.
"""

# Implementation
seats = set(range(1, 51))
while True:
    print("Available seats:", seats)
    seat = int(input("Enter a seat number to book (1-50) or 0 to exit: "))
    if seat == 0:
        break
    if seat in seats:
        seats.remove(seat)
        print("Seat", seat, "booked successfully.")
    else:
        print("Invalid seat number or already booked.")
