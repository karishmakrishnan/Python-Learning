# Remove duplicates but preserve order
L1 = [1,2,3,4,5,5,1,2,6,7,4,8,9]
new_list = []

for i in L1:
    if i not in new_list:
        new_list.append(i)
print("List without duplicates and preserved order:", new_list)

L2 = [1, 2, 4, 5, 6]
min_val = min(L2)
max_val = max(L2)
L2_range = list(range(min_val,max_val,1))
missing_num = [x for x in L2_range if x not in L2]
print("missing numbers in the list:", missing_num)


