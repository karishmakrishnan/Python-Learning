list1 = [11,2,34,5,86,78,90,11,23]

def remove_duplicate(l1):
    unique = []
    for i in range(len(l1)):
        if l1[i] not in l1:
            unique.append(l1[i])
    return unique
print("The list before removing duplicate: ",list1)
print("The list after removing duplicate: ",remove_duplicate(list1))
