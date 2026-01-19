# Remove duplicates but preserve order
L1 = [1,2,3,4,5,5,1,2,6,7,4,8,9]
new_list = []

for i in L1:
    if i not in new_list:
        new_list.append(i)
print("List without duplicates and preserved order:", new_list)

# Array contains numbers from 1 to n, one missing.
L2 = [1, 2, 4, 5, 6]
min_val = min(L2)
max_val = max(L2)
L2_range = list(range(min_val,max_val,1))
missing_num = [x for x in L2_range if x not in L2]
print("missing numbers in the list:", missing_num)

# Using set to remove duplicates but order not preserved
L3 = [1,2,3,4,5,5,1,2,6,7,4,8,9]
new_list_set = list(set(L3))    
print("List without duplicates but order not preserved:", new_list_set) 
# Using dict.fromkeys() to remove duplicates but order preserved
L4 = [1,2,3,4,5,5,1,2,6,7,4,8,9]
new_list_dict = list(dict.fromkeys(L4)) 
print("List without duplicates and preserved order using dict:", new_list_dict)


