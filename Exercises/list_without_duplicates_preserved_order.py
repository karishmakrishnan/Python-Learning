# Remove duplicates but preserve order
L1 = [1,2,3,4,5,5,1,2,6,7,4,8,9]
new_list = []

for i in L1:
    if i not in new_list:
        new_list.append(i)
print("List without duplicates and preserved order:", new_list)


