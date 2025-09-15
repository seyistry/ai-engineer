import numpy as np

# Problem: Given
# A = [[2, -1, 3],
#      [0,  4, 1]]  -> shape (2,3)
# B = [[ 1,  2],
#      [-2,  0],
#      [ 5, -3]]   -> shape (3,2)

# Construct matrices
A = np.array([[2, -1, 3], [0, 4, 1]])
B = np.array([[1, 2], [-2, 0], [5, -3]])

# (a) shapes
print("Matrix A shape (rows, cols):", A.shape)
print("Matrix B shape (rows, cols):", B.shape)

# (b) Multiplication compatibility
# For AB: A (2x3) * B (3x2) -> defined (result 2x2)
can_AB = A.shape[1] == B.shape[0]
# For BA: B (3x2) * A (2x3) -> defined (result 3x3)
can_BA = B.shape[1] == A.shape[0]
print('\nCan compute AB?', can_AB)
print('Can compute BA?', can_BA)

# (c) Compute if defined
if can_AB:
    AB = A @ B
    print('\nAB =')
    print(AB)

if can_BA:
    BA = B @ A
    print('\nBA =')
    print(BA)

# Document results in brief
print('\nNotes:')
print('- AB is 2x2 because inner dimensions (3) match, outer are (2,2).')
print('- BA is 3x3 because inner dimensions (2) match, outer are (3,3).')
