# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.

import numpy as np

arr = np.array([1,2,3,4,5,6])

for x in arr:
    print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

arr  = np.array([[[1,2,4],[10,20,79]],[[1,2,3],[4,5,6]]]) #--arr[0],arr[1]-->x value inpython code

for x in arr:
   print(x)

#to print the element by element
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)

# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.

# NumPy does not change the data type of the element in-place (where the element is in array) 
# so it needs some other space to perform this action, 
# that extra space is called buffer, and in order to enable 
# it in nditer() we pass flags=['buffered'].
      
arr = np.array([1, 2, 3])
print("Array iteratting")
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):#iterating both array,skipping second element
  print(x)

# Enumerated Iteration Using ndenumerate() to get the index values aswell
  
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)