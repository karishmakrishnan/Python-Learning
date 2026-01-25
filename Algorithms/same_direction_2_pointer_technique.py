# same direction 2 pointer technique
# slow->fast->
# often sorted not always
# remove lements, compress data, filter in place

# remove duplicates from sorted array
arr = [1,2,2,3,4,5,6,6,7,8,8,9]
slow = 0

for fast in range(1, len(arr)):
    if arr[fast] != arr[slow]:
        slow += 1
        print(slow)
        arr[slow] = arr[fast]
print(arr[: slow+1])

# move all 0 to end
arr = [1,0,2,3,4,0,5]
slow = 0

for fast in range(len(arr)):
    if arr[fast] != 0:
        arr[slow] = arr[fast]
        slow += 1
while slow < len(arr):
    arr[slow] = 0
    slow += 1
print(arr)