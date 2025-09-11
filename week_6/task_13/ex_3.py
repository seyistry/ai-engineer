from ex_1 import create_random_array

arr = create_random_array()

reshaped_arr = arr.reshape(3, 2, 6)

print("Original Array (6x6):")
print(arr)

print("\nReshaped Array (3x2x6):")
print(reshaped_arr)


flatted_arr = reshaped_arr.flatten()

print("\nFlattened Array (1D):")
print(flatted_arr)


