nums = [2, 7, 11, 15]
target = 18

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