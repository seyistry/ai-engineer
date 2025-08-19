"""**Task3: Online Store Cart Calculation**

- Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

- Start with an empty cart total (cart_total = 0).

- Use assignment operators (+=) to add the price of some items into cart_total.

- Print the list of items and the total price using an f-string like this:

```
Items: ['Book', 'Pen', 'Bag']
Total Price: ₦600
```
"""

items = ["Book", "Pen", "Bag"]
prices = [500, 100, 2000]
cart_total = 0

# Adding item prices to the cart total
cart_total += prices[0]  # Book
cart_total += prices[1]  # Pen

# Print the items and total price
print(f"Items: {items}")
print(f"Total Price: ₦{cart_total}")
