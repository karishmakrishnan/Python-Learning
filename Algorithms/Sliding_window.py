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