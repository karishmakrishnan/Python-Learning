s1 = "I love python"
s1_sp = s1.split()
s1_rev = str()
def Reversed(x):
    str1  = x
    str1_rev = str()
    i = len(str1) -1
    while i >= 0:
        str1_rev = str1_rev+str1[i]
        i = i-1
    # print(str1_rev)
    return str1_rev

for x in s1_sp:
    s1_rev = s1_rev+" "+Reversed(x)

print("String before reverse: ",s1)
print("String after reverse: ", s1_rev)




