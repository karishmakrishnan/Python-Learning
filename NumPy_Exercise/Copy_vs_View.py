import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr)
x= arr.copy()
y = arr.view()
print(x)
print(y)

x[4] = 600
y[4] = 500

print(x)
print(y)
print(arr)

print(x.base)
print(y.base)

