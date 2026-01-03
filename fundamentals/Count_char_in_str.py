str1 = "mississippi"
count_char = dict()
for x in str1:
    if x in count_char:
        count_char[x] +=1
    else:
        count_char[x] = 1
print("Charector and its string: ",count_char)