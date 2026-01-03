# Array search

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)

# To find the index of even numbers
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)


# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be
# inserted to maintain the search order.
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 5)
print(x)

# search from right side
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

# search for multiple values
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)