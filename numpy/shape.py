import numpy as np
a = np.array([1, 35, 41,54,44], ndmin=6)
print(a)
print('shape of array :', a.shape)

# reshaping
b = np.array([11, 24, 53, 74,55, 86, 57, 68, 49, 10, 11, 12])

c = b.reshape(2, 3, 2)

print(c)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)