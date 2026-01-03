l1 = [1,2,3,4,5,6,90,31,3,6,90,7,4,3]
l2 = [4,5,6,7]
common_list = list()

for x in l2:
    for y in l1:
        if(x == y and x not in common_list):
            common_list.append(x)

print("The common elements are:", common_list)

