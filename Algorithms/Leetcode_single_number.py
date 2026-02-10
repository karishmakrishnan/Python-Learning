# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

nums = [2,2,1]
frequency = {}
single_number = 0
for num in nums:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
for num in frequency:
    if frequency[num] == 1:
        single_number = num
        break
print(single_number)