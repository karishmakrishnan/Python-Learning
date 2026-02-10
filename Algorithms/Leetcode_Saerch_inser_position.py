# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

nums = [1,3,5]
target = 3
left = 0
right = len(nums) - 1
mid = (left + right) // 2
position = 0
while(left <= right):
    mid = (left + right) // 2
    print(mid)
    if (nums[mid] == target or nums[mid] - 1 == target):
        position = mid
        break
    if nums[mid] + 1 == target:
        position = mid + 1
        break
    elif(nums[mid] > target):
        right = mid - 1
    elif(nums[mid] < target):
        left = mid + 1
print(position)