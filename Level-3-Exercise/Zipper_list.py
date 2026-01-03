# merge 2 list like a zipper
nums = [1,2,3,4]
chars = ['a','b','c']
zipp_list = list()
Empty = None

j = int()

# max_list = nums if len(nums) > len(chars) else chars
# min_list = nums if len(nums) < len(chars) else chars
# # print(max_list)
# print(len(max_list))

# for i in range(0,len(max_list),1):
#     j = i
#     # print(i)
#     if j < len(min_list):
#         # print(i)
#         zipp_list.append((max_list[i],min_list[j]))
#     elif j >= len(min_list):
#         zipp_list.append((max_list[i],None))

# print("The given lists after zipping: ", zipp_list)

# 1. find the max length of the given String
# 2. loop through it and check for the i value is exceeding the max
# 3. update the zipper list

max_len = max(len(nums), len(chars))
for i in range(max_len):
    integer = nums[i] if i < len(nums) else None
    char = chars[i] if i < len(chars) else None
    zipp_list.append((integer,char))
print("The given lists after zipping: ", zipp_list)


        
    


