import numpy as np
a = np.array([1, 2, 3, 4])
print(a[2] + a[3])
b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', b[0, 1])
c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(c[0, 1, 2])