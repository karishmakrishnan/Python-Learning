# insertion sort
arr = [8,3,5]
key = arr[0]
j = float('-inf')
for i in range(1,len(arr),1):
    j = i -1
    key = arr[i]
    k = i+1
    if j >=0 & arr[j] > key:
        # 1. shift
        arr[j+1] = arr[j]
        # insert key 
        arr[j] = key
    if (k < len(arr)) & arr[k] > key:
        # shift
        arr[k - 1] = arr[k]
        arr[k] = key
print(f"Array after the sort is:", arr)
        