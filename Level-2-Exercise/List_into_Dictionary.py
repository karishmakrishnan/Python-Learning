key_list = ["name", "age", "city"]
value_list = ["Asha", 25, "Delhi"]

key_value = dict()

for i in range(len(key_list)):
    if(key_list[i] not in key_value):
        key_value[key_list[i]]  = value_list[i]

print("After merging key and value list into Dict: ",key_value)
