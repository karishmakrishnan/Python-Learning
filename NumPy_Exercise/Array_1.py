import numpy as np

arrays = np.array([1,2,3,4,5]) #list to array
print(arrays)
print(type(arrays))
print(np.__version__)

arrays = np.array((1,2,3,4,5,6,7,8,9))
print(arrays)

# Dimensions of arrays=====================
print("====================Dimentios of array====================")
print("0-D Array")
# nested array: are arrays that have arrays as their elements.
arr = np.array(42)#0-D array
print(arr)
print(arr.ndim)

print("1-D Array")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

print("2-D Array")
# Each elements in an array is an array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

print("3-D Array")
# Each elements in an array is 2-D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(arr.ndim)

print("Defining the dimensions of array")
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
