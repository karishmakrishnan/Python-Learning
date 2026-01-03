nums = [10,20,30,40,50]
i = 1
squares = [i*i for i  in range(1, 11)]
print(squares)

nums.append(60)
print(nums)
x = 0

while(x < len(nums)):
    if(nums[x] == 30):
        nums.pop(x)
    if(nums[x] == 20):
        nums[x] = 25
    x = x+1
print(nums)
nums_rev = list()

num_len = len(nums)
i = num_len - 1

while( i >=0):
    print(i)
    nums_rev.append(nums[i])
    i = i - 1

print(nums_rev)