# find duplicate without using set
nums = [1,2,3,2,4,1,5,1]
isduplicate = False
duplicates = list()
element_count = dict()
for num in nums:
    if num in element_count:
        element_count[num] +=1
    else:
        element_count[num] = 1
# print(element_count)
for key in element_count:
    if(element_count[key] > 1):
        duplicates.append(key)

print("The input list: ",nums)
print("The duplicates in input list: ",duplicates)

# for i in range(len(nums)):
#     j = i+1 if i+1 < (len(nums)) else i
#     if(i == j):
#         break
#     for j in range(len(nums)):
#         if(nums[i] == nums[j]):
#             isduplicate = True
#     if ((isduplicate == True) and nums[i] not in duplicates):
#         duplicates.append(nums[i])
#     isduplicate = False
# print("The input list: ",nums)
# print("The duplicates in input list: ",duplicates)

