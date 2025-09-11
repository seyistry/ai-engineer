import numpy as np

arr_3X4 = np.random.randint(1, 10, (3, 4))
print(arr_3X4)

arr_4X3 = np.random.randint(1, 10, (4, 3))
print(arr_4X3)

multiplication_result = arr_3X4 @ arr_4X3
print(multiplication_result)