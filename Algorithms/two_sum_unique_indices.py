nums = [3, 2, 4, 6, 1, 5]
target = 7

def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        cmp = target - num
        if cmp in nums and cmp not in lookup:
            lookup[cmp] = [i]
    for i, num in enumerate(nums):
        if num in lookup:
            lookup[num].append(i)
    return lookup

print(two_sum(nums,target))

seen = {}
pair = []

for index, num in enumerate(nums):
    compliment = target - num
    if compliment in seen:
        for cmp_ind in seen[compliment]:
            pair.append((index, cmp_ind))
    if num in seen:
        seen[num].append(index)
    else:
        seen[num] = [index]
print(seen)
print(pair)