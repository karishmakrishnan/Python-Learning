dict_new = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

reverse_dict = dict()

for x in dict_new:
    reverse_dict.update({dict_new[x] : x})

print("Reverse of Dictionary: ",reverse_dict)