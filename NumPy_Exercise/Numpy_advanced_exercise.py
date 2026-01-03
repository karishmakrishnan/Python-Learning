# Numpy advanced exercise

# scaling of shape(5,4) with shape(4,)
import numpy as np

arr1 =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,10]])
arr2 =np.array([50,60,70,80])
newarr = arr1*arr2
print("scaling each column after broadcasting: ", newarr)

# add column vector shape(3,1) to shape(3,5)
arr3 = np.array([[1,2,3,4,22],[5,6,7,8,33],[9,10,11,12,44]])
arr4 = [[100],[200],[300]]
newarr = arr3+arr4
print("After column vector addition: ",newarr)

# Create a 3x10 mathrix using broadcasting
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr5 = np.array([[0],[0],[0]])
arr5 = arr5+arr
print("The 3x10 mathrix with values 0-9: ",arr5)

# pairewise difference matrix
a = np.array([2,5,8])
column_matrix = a.reshape(3,1)
pair_diff_matrix = a-column_matrix
print("pairewise difference matrix: ",pair_diff_matrix)

# Normalizing the matrix column x-mean/std
A = np.array([[1,3,4],[6,4,2],[8,9,7]])

mean_clm = A.mean(axis=0)
std_clm = A.std(axis=0)

normlzd = (A - mean_clm)/std_clm

print("The normalized array is: ",normlzd)

# power of -ve integer in an array
A = np.array([1,2,-3,7,-8])
B = np.array(0)
power = np.where(A<0,A**2,A)
print("Power of -ve integer in array: ",power)

# (A^2+B^2)^1/2
A = np.array([[1,2,3,4],[3,4,5,3]])
B = np.array([[2,2,2,2],[5,5,5,5]])
power_sum = (A**2) +(B**2)
newarr = power_sum**(1/2)
print("The array (A^2+B^2)^1/2: ",newarr)

# count the number in between mean and std
A = np.array([1,2,3,4])
mean = A.mean()
std = A.std()
count = A[(A>=std) & (A<=mean)]
print(count)



