# 2 pointer array
# pair sum(sorted array)

arr = [1,3,4,6,6,11,23]
target = 15

left = 0
right = len(arr) - 1
current_sum = 0
pair_arr = []
is_found = False

while(left < right):
    current_sum = arr[left] + arr[right]
    if(current_sum == target):
        pair_arr.append(arr[left])
        pair_arr.append(arr[right])
        is_found = True
        break;
    elif(current_sum < target):
        left +=1
    elif(current_sum > target):
        right -=1
if is_found:
    print(f"The target is found in given array and the pair is:", pair_arr)
else:
    print("The target pair is not found in the given array")
