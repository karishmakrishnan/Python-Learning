nums = [3,2,4]
target = 6
Max= len(nums)
i = 0
j = 0

for i in range(Max):
    for j in range(i+1, Max):
        if(nums[i]+nums[j]==target):
            print(f"[{i},{j}]")
# class Solution(object):
#     def twoSum(self, nums, target):
#       max = int(len(nums))
#       j=0
#       i=0
#       for i in range(max):
#         for j in range(i+1,max):
#             if(nums[i]+nums[j] == target):
#                 return i,j
