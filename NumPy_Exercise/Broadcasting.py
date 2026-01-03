# Broadcasting
# way of doing operation on array of different shape without looping

# For 2 arrays to broadcast
# 1. Dimension should be equal
# 2. One dimension is 1 ->ok
# 3. Otherwise error
import numpy as np

arr = np.array([1,2,3])
print((arr+5).base)

# Axis of one dimentional array
# 1D array has 0 axis
# [1,2,3,4]
# --------->axis 0
# shape=(4,)

# 2D array  |
# [1,2,3,4] |axis 1      shape = (2,4)
# [5,6,7,8] |
    # axis 0        # >
# --------->

# 3D array

# [[[1,2,3],[4,5,6],[5,6,7]]] -->axis 0, axis1, axis2
# shape = (1,3,3)
print(np.shape([[[1,2,3],[4,5,6],[5,6,7]]])) 

arr1 = np.array([[1,2,3],[6,7,8]])
arr2 = np.array([1,2,3])

print(arr1+arr2)

A = np.array([10,20,30])
B = np.array([5])
print(A+B)


arr1 = np.array([[1,2,3],[6,7,8]])
arr2 = np.array([1,2])

arr1+arr2 #==>gives error, expect 3 values in 1D