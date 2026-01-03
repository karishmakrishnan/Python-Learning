input_list = [1,2,2,3,1,4]
unique_list = list()

for x in input_list:
    if x not in unique_list:
        unique_list.append(x)

print("The list after removing duplicate and keeping the order",unique_list)

