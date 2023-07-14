import numpy as np
a = np.array([1, 2, 3, 4])
print(a.dtype)
b = np.array(['apple', 'banana', 'cherry'])
print(b.dtype)
c = np.array([1, 2, 3, 4], dtype='S')
print(c)
print(c.dtype)
d = np.array([1, 2, 3, 4], dtype='i4')
print(d)
print(d.dtype)
# e = np.array(['a', '2', '3'], dtype='i')
f = np.array([1, 0, 3])
n = f.astype(bool)
print(n)
print(n.dtype)