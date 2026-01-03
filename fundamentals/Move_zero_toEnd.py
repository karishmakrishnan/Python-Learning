l1 = [0,1,0,3,12]

for x in range(len(l1)):
    if(l1[x] == 0):
        l1.append(l1[x])
        l1.pop(x)

print("After moving '0' to the end: ", l1)
