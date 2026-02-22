import heapq

nums = [1,1,1,2,2,3]
k = 2

heapq.heapify(nums)
print(nums)
freq_list = []

freq = {}
for num in nums:
    if num not in freq:
        freq[num] = 1
    else:
        freq[num] += 1
for key,val in freq.items():
    heapq.heappush(freq_list, (val, key))
    if len(freq_list) > k:
        heapq.heappop(freq_list)
result = [num for (count, num) in freq_list]
print(result)