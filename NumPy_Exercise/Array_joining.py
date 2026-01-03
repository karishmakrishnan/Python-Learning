# Array joining

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
# the array dimention should be same for concatenate()
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print("new array",arr)

# stack() can use to join array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)##shape(3,2)each colum from both array 
print("new array2:",arr)


# NumPy provides a helper function: hstack() to stack along rows.
arr1 = np.array([[1, 2, 3],[11,22,33]])
arr2 = np.array([[4, 5, 6],[66,77,88]])
arr = np.hstack((arr1, arr2))#horizontal stack same as axis = 0 and 
print("horizontal new array2:",arr)

# NumPy provides a helper function: vstack()  to stack along columns.
arr1 = np.array([[4, 5, 6],[66,77,88]])
arr2 = np.array([[1, 2, 3],[11,22,33]])
arr = np.vstack((arr1, arr2))

print("Vertical new array2:",arr) ##palce the one below another shape(2,3)

# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])# 3 elements so dim will become 3
arr = np.dstack((arr1, arr2))
print("new dstack array2:",arr)