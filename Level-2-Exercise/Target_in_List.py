target = 9
nums = [ 2, 7, 11, 15]
find = 0
i = 0
nums_size = len(nums)
j = 0
pair = list()

while(i < nums_size):
    find = abs(target - nums[i])
    for j in range(j+1, nums_size):
        if(nums[j] == find):
            pair.append(nums[i])
            pair.append(nums[j])
    i +=1

print(pair)