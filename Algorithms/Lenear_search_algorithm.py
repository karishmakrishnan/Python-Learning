# Lenear search algorithm

list1 = [2,4,6,7,3,5,8,9,0]

# Leanear search, search the element using loop(brute force algo)
# best case O(1)
# worsr case O(n)
# lenear serch return index and target value 

found = False
Target = 8
i = 0
index = 0
while(i < len(list1)):
    if (list1[i] == Target):
        found = True
        index = i
        break
    else:
        i +=1
if(found == True):
    print(f"The target:{Target} is preset at index:{index} ")
else:
    print(f"The target {Target} is not present in given list")




