# Numeric type in python
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
# datatype:int nothing but a whole number
x = 5
y = 10
print(type(x), type(y))

# datatype:float is used for storing decimal number
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
f = 12.89896
d = 23.90
print(type(f), type(d))

# datatype:complex to store complex values
# Complex numbers are written with a "j" as the imaginary part:
c = complex(3, 5)
c=6j
print(c)
print(type(c))

# datatype:range give 0-range_value-1
print(range(6))

# Random
import random
print(random.randrange(1,10))

# datatype:str
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# 3 double quote/single quote for multiple values
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

str1 = "Hello world"
str2 = str1[1]
print(str2)

for x in str1:
    print(x, end='')
    # print(x)
print("\n")
print(len(str1))

# you can use "in" or "not in" to check string

print("door" in a)
print("dolor" in a)

if "elit" in a:
    print ("Given strin is present")
else:
    print ("Given string is not present")

print ("Lorem" not in a)
if "Lorem" not in a:
    print("Lorem is not present instring")
else:
    print("Lorem is present")

a = "hello world"
x=a[2:5]
print(x)
print(a[2:5])
print(a[1:5])
print(a[:8])
print(a[3:])
print(a[-7:])
print(a[-11: -7])
print(a[-7:-11])

# string methods
str_1 = "Hello My World"

print(str_1.upper())
print(str_1.lower())
print(str_1.replace("H", "M"))
print(str_1.strip())
print(str_1.split(" "))

# '+' is used for string concatination
# format() method is used for combining string and numbers

age = 20
txt = F"My age is {age}"
print(txt)

price = 1000
txt = F"The bag price is {price}"
print(txt)
txt = F"The bag price is {price:.5f}" #add five floating value
print(txt)
txt = F"The bag ptice is {100*price:.3f}"
print(txt)

txt = 'The varriors were called "Vikkings"'
txt1 = "The varriors were called \"Vikking\""
print(txt1)
print(txt)
print(5//10)