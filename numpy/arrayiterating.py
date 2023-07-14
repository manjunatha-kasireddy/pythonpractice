import numpy as np
a = np.array([1, 2, 3])
for x in a:
  print(x)
b = np.array([[1, 2, 3], [4, 5, 6]])
for x in b:
  print(x)
c = np.array([[1, 2, 3], [4, 5, 6]])
for x in c:
  for y in x:
    print(y)
d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(d):
  print(x)
e = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(e):
  print(idx, x)
