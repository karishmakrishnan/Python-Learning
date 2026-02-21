# using 2 pointer for sorted array
nums = [3, 2, 4]
target = 6

result = []

left = 0
right = 1

while(right != len(nums) - 1):
    if nums[left] + nums[right] == target:
        result.append(left)
        result.append(right)
        break
    if nums[left] + nums[right] < target:
        left += 1
        right += 1
print(result)

# using dict for unsorted array
def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]

        lookup[num] = i
print(two_sum(nums, target))