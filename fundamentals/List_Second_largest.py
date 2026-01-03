nums = [10,40,20,5,40,30]

uneque_nums = list()
nums.sort()

for i in range(len(nums)):
    if(i == 0 or nums[i] != nums[i-1]):
        uneque_nums.append(nums[i])

uneque_nums.sort()
print(uneque_nums)

print("Second Largest number: ", uneque_nums[-2])
