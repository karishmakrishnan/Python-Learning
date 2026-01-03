nums = [1,2,2,3,4,4,5,6,7,7]
k = int()
i = int()
Unique_nums = list()

len_nums = len(nums)

# mylogic
# for i in range(len_nums):
#     k = i+1
#     if(k < len_nums):
#         if(nums[i] != nums[k]):
#             Unique_nums.append(nums[i])
#     if(i == len_nums-1):
#         if(nums[i] != nums[i-1]):
#             Unique_nums.append(nums[i])

for i in range(len_nums):
    if(i == 0 or (nums[i] != nums[i-1])):
        Unique_nums.append(nums[i])
print("List without duplicates :",Unique_nums)
