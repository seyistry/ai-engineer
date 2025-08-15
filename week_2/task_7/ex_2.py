"""Task2: Super Market Price List
- Create a program that stores items and their prices in a dictionary.

- Items should come from a list.

- Prices are entered by the user.

- Display all items and prices, then allow the user to update the price of an item.

- Requirements:

- Use dictionary update method `.update()` or assignment.

- Use `.keys()` to display available items.

- Use input validation (no advanced functions).
"""

# items
items = ["Rice", "Beans", "Milk", "Pasta", "Bread"]

# prices
prices = {}

# Get prices for each item
for item in items:
    while True:
        try:
            price = float(input(f"Enter price for {item}: "))
            prices[item] = price
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Display all items and prices
print("\nSuper Market Price List:")
for item, price in prices.items():
    print(f"{item}: ${price:.2f}")

# Update price for an item
while True:
    item_to_update = input("\nEnter the item to update the price (or 'done' to finish): ")
    if item_to_update.lower() == 'done':
        break
    if item_to_update in prices:
        while True:
            try:
                new_price = float(input(f"Enter new price for {item_to_update}: "))
                prices[item_to_update] = new_price
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    else:
        print("Item not found.")

# Final price list
print("\nUpdated Super Market Price List:")
for item, price in prices.items():
    print(f"{item}: ${price:.2f}")
