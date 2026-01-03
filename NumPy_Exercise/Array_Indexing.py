# array indexing is same as accessing the array
# indexing start with 0 and negative indexing start with -1
import numpy as np

print("Accessing the elements of 1-D array")
arr1 = np.array([1,2,3,4,5])
first = arr1[0]
second = arr1[1]
print(first,second)

print("Accessing the elements of 2-D array")
arr2 = np.array([[1,2,3],[9,7,4]])
first_3 = arr2[0,2]
second_2 = arr2[1, 1]
print(first_3,second_2)

print("Accessing the elements of 3-D array")
arr3 = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])
# access element 60
element1 = arr3[1,0,1]

# access element 30
element2 = arr3[0,1,0]

print(element1,element2)


