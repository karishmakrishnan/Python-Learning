#removing consecutive duplicates

nums = [1,1,2,2,2,3,1,1]
k = int()
unique = list()
for i in range(len(nums)):
    k = i -1
    if(i == 0):
        unique.append(nums[i])
    elif(nums[i] != nums[k]):
        unique.append(nums[i])
    
print("The list after removing consecutive duplicates", unique)

