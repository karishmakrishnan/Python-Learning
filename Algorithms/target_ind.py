# return the target val's index from list

# lenear search with o(n)
nums = [4,5,6,7,0,1,2]
target = 0
result = 0

for index, num in enumerate(nums):
    if num == target:
        result = index
print(result)

left = 0
right = len(nums) - 1

# binary search with o(logn)
# while left <= right:
    
#     mid = ...

#     if nums[mid] == target:
#         return mid

#     if left half sorted:
#         if target in left half:
#             move right
#         else:
#             move left
#     else:
#         right half sorted
#         if target in right half:
#             move left
#         else:
#             move right

def findIndex(nums, target):
    while left <= right:
        mid = left + right // 2

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid
        else:
            right = mid
def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if left half is sorted
        if nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Otherwise right half is sorted
        else:

            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

