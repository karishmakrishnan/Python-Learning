# # Array_sort
import numpy as np

arr = np.array([3, 2, 0, 1])
print("Sorted int array",np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print("Sorted string array",np.sort(arr))

arr = np.array([True, False, True])  #f=0,t=1 so it will sort the order of 0-1
print("Sorted bool array",np.sort(arr))

# 2D array sorting
arr = np.array([[3, 2, 4], [5, 0, 1]])#--the inside array will be sorted
print("Sorted 2D array: ",np.sort(arr))

# Getting some elements out of an existing array and creating a new array out of them is called filtering.
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]##x will remove element of arr at the position of false
print("Filtered array: ",newarr)

# Filter array with condition
arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print("Filtere array: ",filter_arr)
print("Filtered array: ",newarr)

# Filter array for even number
# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print("Filtere array: ",filter_arr)
print("Filtered array of even number: ",newarr)

# One line solutoion
arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# One line solution for even numbers
arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)