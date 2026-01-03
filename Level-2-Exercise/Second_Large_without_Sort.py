nums = [12,57,84,90,10,12,86,90]
first_large = 0
second_large = 0

unique = list()
def MakeListUnique(numlist):
    for x in numlist:
        if x not in unique:
            unique.append(x)
    return unique

def LargeInList(numList):
    Large_in_List = 0
    if len(numList) == 2:
        return x if x>numList[0] else numList[1]
    else:
        for x in numList:
            if (x > Large_in_List):
                Large_in_List = x
    return Large_in_List

unique = MakeListUnique(nums)
first_large = LargeInList(unique)

print(unique)
# print(first_large)

for x in unique:
    if x >= second_large and x < first_large:
        second_large = x
print("The second large element: ",second_large)