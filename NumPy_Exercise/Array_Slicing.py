import numpy as np

# slicing in array means taking elements from one position to another
# [start:end] inclused from start to end-1 index

arr1 = np.array([1,2,3,4,5,6])
print(arr1)
# take array from index 1,4
# print("Index 1 to 4:",arr1[1:4])
# print("Starting from 2 to till end:",arr1[2:])
# print("starting from first to 4:",arr1[:4])

# print("-ve slicing")
# print("element position 2 till last",arr1[-3:-1])

# print("Adding steps in slicing")
# arr2 = np.array([1,2,3,4,5,6,7,8,9])
# print(arr2)
# print("Adding step 2:", arr2[3:9:2])
# print("Adding step to full array:",arr2[::2])

# print("2-D array slicing")
# arr3 = np.array([[1,2,3,4],[6,7,8,9]])
# print(arr3)

# print("Slice the second element from index 1 to4:",arr3[:,1:4:2])
# print("Slice the first element from 2 to 4:",arr3[0,2:4])
# print("From both element print index 1 to4:",arr3[:,1:4])
# print("Slice the second element from index 1 to4:",arr3[:,:])

print("3-D array slicing")
arr3 = np.array([[[1,2,3,4],[6,7,8,9]],[[11,22,33,44],[55,66,77,88]]])
print("Slice the second position from index 1 to4:",arr3[1,:,1:4])
print("Slice the first position, first array from 2 to 4:",arr3[0,0,2:4])
print("From all layer print index 1 to4:",arr3[:,:,1:4])
print("Last layer last emelent:",arr3[1,1,3:4])
