import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.dtype)

arr2 = np.array([23,45,78], dtype="S")
print(arr2)
print(arr2.dtype)

nee_arr = arr1.astype("f")
print(nee_arr)
