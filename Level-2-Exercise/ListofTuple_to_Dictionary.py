list_tuple = [("a",1), ("b",2), ("c",3)]

new_dict = dict()
i = 0
for x in list_tuple:
    while(i < len(list_tuple)):
        if list_tuple[i][0] not in new_dict:
            new_dict[list_tuple[i][0]] = list_tuple[i][1]
            i +=1

print("List of tuple after converting to Dictionary", new_dict)
