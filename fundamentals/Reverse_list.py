nums = [1,2,3,4]
nums_rev = list()

nums_length = len(nums)
i = nums_length - 1

while (i >= 0):
    nums_rev.append(nums[i])
    i -=1
print("Reverse array:", nums_rev)

