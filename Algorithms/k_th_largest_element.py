import heapq
nums = [3,2,1,5,6,4]
k = 2

def find_kth_large(nums, k):
    heapq.heapify(nums)
    k_large_elements = heapq.nlargest(k, nums)
    for i in range(k):
        kth_large = heapq.heappop(k_large_elements)
    return kth_large
print("the kth lrgest elemnt form the list, ", find_kth_large(nums, k))


# without using built in function
def findKthLargest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]