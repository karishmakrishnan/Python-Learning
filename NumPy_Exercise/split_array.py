# split array
# The return value of the array_split() method is a list containing each of the split as an array.
# If you split an array into 3 arrays, you can access them from the result just like any array element:
import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

# # Use the array_split() method, pass in the array you want to split and the number of splits you want to do.
# arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
# newarr = np.array_split(arr, 3)
# print(newarr)

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr, 3)
# print(newarr)

# specifying the axis you want to split
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=0)
print("axis split",newarr)

# hsplit() --horizontal split
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)#column split
print("horizontal split",newarr)

# vsplit() and dsplit()
newarr1 = np.vsplit(arr,2)
print(newarr1)

# # ('dsplit only works on arrays of 3 or more dimensions')
# newarr2 = np.dsplit(arr,2)
