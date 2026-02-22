#  heapq in python
import heapq

nums = [3,2,5,1,6,8]
heapq.heapify(nums) #smallest element will be at the index 0
# By default it is min heap
heapq.heappush(nums, 10)
smallest = heapq.heappop(nums)
smallest2 = heapq.heappushpop(nums, 9)
print(smallest)
print(smallest2)
print(nums)

# simulate max heap
# We invert numbers to get max heap
max_heap = []

nums = [5, 1, 3, 7]
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

print((max_heap))

# find k smallest from list
nums = [3,4,2,5,6]
k = 3

heapq.heapify(nums)
ksmall = heapq.nsmallest(k, nums)
print(ksmall)

# find k largest from list

klarge = heapq.nlargest(k, nums)
print(klarge)