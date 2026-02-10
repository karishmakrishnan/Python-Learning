# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 43
nums = [9]
def array_to_int(nums):
    ml = 1
    sum = nums[len(nums)-1]
    for i in range(len(nums)-2, -1, -1):
        ml = ml * 10
        sum = sum + (nums[i]* ml)
    print(sum)
    return sum
def int_to_array(num):
    nums = []
    while(num != 0):
        nums.append(num % 10)
        num = num // 10
    return list(reversed(nums))
sum_array = 0
if len(nums) == 1:
    sum_array = nums[0] + 1
else:
    sum_array = array_to_int(nums) + 1
print(int_to_array(sum_array))

