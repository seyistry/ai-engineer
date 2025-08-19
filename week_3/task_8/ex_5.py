"""Task5: Store Inventory Update
- Create a dictionary called store with items and their available quantities. Example:
```
store = {"Book": 10, "Pen": 20, "Bag": 5}
```


- Ask the user to input the item they want to buy (e.g., "Pen").

- Ask the user to input the quantity they want to purchase.

- Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

- Print the updated dictionary in this format:

```
Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
```
"""

# Create a dictionary to store item quantities
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Print the initial store inventory
print(f"Before purchase: {store}")

# Get user input for item and quantity
item_to_buy = input("Enter the item you want to buy: ")
quantity = int(input("Enter the quantity you want to purchase: "))

# Update the store inventory
if item_to_buy in store:
    store[item_to_buy] -= quantity

# Print the updated store inventory
print(f"After purchase: {store}")
