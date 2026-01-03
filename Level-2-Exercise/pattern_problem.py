n=5
for i in range(1,n+1,1):
    print("*"*i)

for i in range(1,n+1,1):
    np = (n+1)-i
    print(" "*np+"*"*i)

for i in range(1,n+1,1):
    np = (n+1)-i
    print(" "*np+"* "*i)

for i in range(n,0,(-1)):
    np = (n+1)-i
    print(" "*np+"* "*i)

# print("\n")
for i in range(1,n+2,1):
    np = (n+1)-i
    print("* "*i)
for i in range(n,0,(-1)):
    np = (n+1)-i
    print("* "*i)


for i in range(1,n+1,1):
    np = n-i
    print(" "*np+"*"*i)
