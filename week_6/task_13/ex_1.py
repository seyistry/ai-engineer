import numpy as np

def create_random_array():
	# Create a 6x6 array with random integers between 1 and 50
	arr = np.random.randint(1, 50, size=(6, 6))
	print(arr)
	return arr