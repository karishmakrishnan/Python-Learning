# insertion sort
arr = [8,3,5,4,6,1]
key = arr[0]
j = float('-inf')
for i in range(1,len(arr),1):
    j = i -1
    key = arr[i]
    k = i+1
    # print(i)
    print(key)
    while j >=0 & arr[j] > key:
        # 1. shift
        arr[j+1] = arr[j]
        # insert key 
        arr[j] = key
        j -=1
        # print(arr)
    # if (k <= len(arr)-1):  
    #     if (arr[k] > key):
    #     # shift
    #         arr[k - 1] = arr[k]
    #         arr[k] = key
    #         # print(arr)
print(f"Array after the sort is:", arr)
        