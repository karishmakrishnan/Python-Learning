# Vectorization
# same like broadcasting vectorization is replacing loop in python nad
# making it much faster 
import numpy as np

arr = np.array([1,8,3])

result = []

# normal python looping
for x in arr:
    result.append(x+10)
print(result)

# using broadcasting or vectorization
result = arr+20
print(result)

# Numpy treats array as batches and applies operation to each elements at once.
print(arr*20)#element vectorization
print(arr+10)
print(np.sqrt(arr))
print(np.log(arr))

# operations beteen array
arr2 = np.array([10,20,30])
print(arr+arr2)
print(arr*arr2)

# uFuncs(universal functions)
print("Addition:",np.add(arr,arr2))
print("Substraction:",np.subtract(arr,arr2))
print(np.multiply(arr,11))
print(np.power(arr,2))
print(np.sqrt(arr))
print(np.exp(arr))
print(np.log(arr))

filter_arr = arr[(arr>0) & (arr<5)]
print(filter_arr)

print("Random operations in numpy")
##random operations in numpy
print(np.random.rand(3,4))
print(np.random.randint(1,50,10))
print(np.random.choice(arr2))
print(np.random.shuffle(arr))
