num = 9874
modulus = int()
sum  = 0

while(num != 0):
    # print(num)
    modulus = num%10
    sum = sum + modulus
    num = num//10


print("Sum of digit od num: ", sum)

