import numpy as np
a = np.array([41, 42, 43, 44, 87, 96, 10])
b = [True, False, True, False, True, True, False]
c = a[b]
print(c)
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)