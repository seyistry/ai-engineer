from ex_1 import create_random_array

# Create a random 2D NumPy array (e.g., 6x6) using a function from ex_1.py
# This array will be used for all the following operations.
arr = create_random_array()

# 1. Select the first two rows of the array (all columns):
# arr[:2, :] means:
#   - :2 selects rows with index 0 and 1 (the first two rows)
#   - : selects all columns in those rows
# The result is a 2xN subarray (N = number of columns, e.g., 6)
first_two_rows = arr[:2, :]

# 2. Select the last two columns of the array (all rows):
# arr[:, -2:] means:
#   - : selects all rows
#   - -2: selects the last two columns (e.g., columns 4 and 5 if there are 6 columns)
# The result is an Mx2 subarray (M = number of rows, e.g., 6)
last_two_columns = arr[:, -2:]

# 3. Select all even numbers from the array:
# arr % 2 == 0 creates a boolean array of the same shape as arr,
#   where each element is True if the corresponding value in arr is even, False otherwise.
# arr[arr % 2 == 0] uses boolean indexing to extract all elements where the condition is True.
# The result is a 1D array containing all even numbers from the original array, in row-major order.
all_even_numbers = arr[arr % 2 == 0]
