# Boolen

print(5>6)
print(10==12)
print(5>3)

if (10> 5):
    print("10 is greater")
else:
    print("10 is nor greater")

print(bool("hello"))
print(bool(123))
def MyFunction():
    return False
print(MyFunction())

# built in bool function isinstance()

x = 100
print(isinstance(x, int))

# operators in python
print(10+20)
print(20-10)
print(20/12)
print(20//12)
print(23*2)
print(10**3)
print(45%2)

# Assignment operator
print("assigment operator")

x=20
print(x)
x +=5  # x=x+5
print(x)
x *=10 # x=x*10
print(x)
x /=10 #x=x/10
print(x)
x //=2 # x= x//2
print(x)
# x>>=1
# print(x)
# x<<=1
# print(x)
# comparison operator
# ==,!=,>,<,>=,<=

if( 5>2 and 5>3):
    print("5 is big")
if(5>6 or 5>3):
    print("this is or")
if( not(5>6 or 5>3)):
    print("this is not")
else:
    print("This is outside")

# Identity operator
x = 100
y = 200

print(x is y)
print(x is not y)
print(x == y)

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Membership operator

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

# bitwise operator
# &(Sets each bit to 1 if both bits are 1),
# |(Sets each bit to 1 if one of two bits is 1), 
# ^(XOR)Sets each bit to 1 if only one of two bits is 1
# ~	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# input(para) - > promt will take the input from the users

name = input("Enter a value: ");
print(name)
name = str(input("Give me your name:"))


x= "kari"
str1 = int(x)# we cannot convert str to integer
print(str1)