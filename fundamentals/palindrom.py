x=1212  
if (x<0):
    print("False")
rev = 0
input1 = x
if (x > 0):
    while(x> 0):
        
        reminder = x%10
        # print(reminder)
        rev = (rev*10)+reminder
        # print(rev)
        print(x)
        x= x//10
        
print(input1 == rev)
