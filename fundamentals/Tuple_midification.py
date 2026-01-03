t = (1,2,3,4,5)

t2 = list(t)

i = 0
t2_len = len(t2)

while( i < t2_len):
    print(i)
    if(t2[i] == 3):
        t2 .pop(i)
        break
    i = i+1
t2.append(10)

t = tuple(t2)

print(type(t))
print(t)