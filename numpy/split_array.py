import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
a1 = np.array_split(a, 3)
print(a1)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
b1 = np.array_split(b, 3)
print(b)
c = np.array([1, 2, 3, 4, 5, 6])
c1 = np.array_split(c, 3)

print(c1[0])
print(c1[1])
print(c1[2])