# selection sort
arr = [7,2,4,2,5,6,5,8,3,9]
key = arr[0]
j = float('-inf')
for i in range(1,len(arr)-1,1):
    j = i+1
    # key = arr[i - 1]
    if j <= len(arr) - 1:
        if key > arr[i]:
            temp = key
            key = arr[i]
            arr[i] = temp
        else:
            key = arr[i]
        if key > arr[j]:
            temp = key
            key = arr[j]
            arr[j] = key
        else:
            key = arr[j]
print(f"Array after the sort is:", arr)
        