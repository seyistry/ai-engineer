import numpy as np

# Create a 2D array (3 rows, 4 columns)
def create_converted_array(arr):
	arr2d = np.array(arr)
	converted = np.where(arr2d % 2 == 0, arr2d**2, -1)
	return converted

try:
	user_input = input("Enter a 2D array (e.g., [[1,2,3,4],[5,6,7,8],[9,10,11,12]]): ")
	# Safely evaluate the input string to a Python list
	user_array = eval(user_input)

except (ValueError, SyntaxError):
	print("Invalid input. Please enter a valid 2D array.")
else:
	print(create_converted_array(user_array))
