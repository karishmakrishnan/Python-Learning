# Sliding window
# Process a contiguous subarray / substring by moving a window instead of recomputing from scratch.
# When to use sliding window

# Contiguous data (array / string)
# Subarrays or substrings
# Problems asking:
# max / min
# sum / average
# longest / shortest
# count under a condition

# 2 types: fixed size and variable size

# fixed size sliding window
# Find maximum sum of subarray of size k

arr = [2,3,42,5,2,5,7,8,12,3]
k =3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]
    if window_sum > max_sum:
        max_sum = window_sum
print(max_sum)

# variable size sliding window
# unlike fixed size in variable size sliding window the subarray size is not constant.
# wxpand the array, once the condition is satisfied shrink it 
# start → expand → condition satisfied → shrink → record answer
# right → expands window
# left → shrinks window
# Condition controls movement

# #### pattern
# left = 0

# for right in range(len(arr)):
#     # 1. Expand window (include arr[right])
#     condition_is_true = True
#     while condition_is_true:
#         # 2. Update answer
#         # 3. Shrink window (exclude arr[left])
#         left += 1
#         pass

# Smallest subarray with sum ≥ target
arr = [2, 3, 1, 2, 4, 3]
target = 45

left = 0
window_sum = 0
min_val = float('inf')

for right in range(len(arr)):
    window_sum += arr[right]
    while window_sum >= target:
        min_val = min(min_val, (right-left) + 1)
        window_sum -= arr[left]
        left += 1
print(min_val)