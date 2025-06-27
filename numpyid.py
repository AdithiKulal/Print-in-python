import numpy as np
students = np.array([
    [1, 14, 160],
    [2, 13, 155],
    [3, 14, 158]
])
sorted_indices = np.lexsort((students[:, 1], students[:, 2]))
sorted_students = students[sorted_indices]
print("ID Age Height")
print(sorted_students)