# insertion sort
arr = [8,3,5,4,6,1]
key = arr[0]
j = float('-inf')
for i in range(1,len(arr),1):
    j = i -1
    key = arr[i]
    # print(key)
    while j >=0 and arr[j] > key:
        # 1. shift
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
print(f"Array after the sort is:", arr)
        