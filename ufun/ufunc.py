from math import log
import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
def myadd(x, y):
      return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([41, 96, 30, 54], [5, 6, 7, 8]))
a1 = np.array([10, 20, 30, 40, 50, 60])
a2 = np.array([3, 7, 9, 8, 2, 33])
n = np.divmod(a1, a2)
print(n)
b = np.trunc([-3.1666, 3.6667])
print(b)
c = np.around(3.1666, 2)
print(c)
d = np.arange(1, 10)
print(np.log10(d))
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
e1 = np.array([1, 2, 3])
e2 = np.array([1, 2, 3])
n = np.sum([e1, e2])
print(n)
f = np.array([17, 52, 73])
g = np.cumsum(f)
print(g)
h = np.array([41, 54, 96])
x = np.lcm.reduce(h)
print(x)
i = np.array([48, 54, 96])
x = np.gcd.reduce(i)
print(x)
a = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(a)
print(x)
a = np.array([96, 54, 41, 60])
x = np.deg2rad(a)
print(x)