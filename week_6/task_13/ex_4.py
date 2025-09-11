import numpy as np

identity_matrix = np.eye(4)
print(identity_matrix)

replace_diagonal = identity_matrix.copy()
np.fill_diagonal(replace_diagonal, np.random.randint(1, 11, 4))

print(replace_diagonal)