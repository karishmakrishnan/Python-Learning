nums = [1,4,7,8,12,3]
even_count = 0
odd_count = 0

nums_length = len(nums)

for x in nums:
    if (x%2 == 0):
        even_count += 1
    else:
        odd_count += 1

print("Even: ", even_count)
print("Odd: ", odd_count)
