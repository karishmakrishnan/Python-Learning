# binary search
lst = [1,2,4,6,7,9,11,34,56,78,98]
target = 12
found = False

left = 0
right = len(lst) - 1
# mid = len(lst)//2 
# print(mid)
while (left <= right):
    # print(mid)
    mid = (left+right) // 2
    if(lst[mid] == target):
        found = True
        break
    if(target > lst[mid]):
        left = mid + 1
    else:
        right = mid - 1
print(f"The target {target} found is: {found}")




