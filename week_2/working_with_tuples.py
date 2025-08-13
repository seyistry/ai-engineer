"""working with tuples
"""

# Ordered
colors = ("red", "green", "blue")
print(colors[0])  # red

# Immutable ( uncomment and run. This will cause an error)
# colors[1] = "yellow"  #  TypeError

# Allow duplicates
numbers = (1, 2, 2, 3)
print(numbers)  # (1, 2, 2, 3)

# Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)  # ('apple', 3, True, 5.6)

# Nested tuples
nested = (("a", "b"), (1, 2))
print(nested)  # (('a', 'b'), (1, 2))

# 1. Indexing

fruits = ("apple", "banana", "cherry")
print(fruits[1])   # banana
print(fruits[-1])  # cherry

# 2. Slicing

print(fruits[0:2])   # ('apple', 'banana')
print(fruits[::-1])  # ('cherry', 'banana', 'apple')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)  # (1, 2, 3, 4)
