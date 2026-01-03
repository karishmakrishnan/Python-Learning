# print("Hello World");

# import sys;
# print(sys.version);
# Indentation -----
if 3>9:
 print("3 is greater");
print("checking indentation");
# else:
#  print("9 is greater");

# Variables in python

x = 9.6
y = 10
sum = x+y;
s = "Hello World"
print(sum)
print(s)
# two statement in one line, ";" ends the line 
print(sum);print(s)

# "" or '' can be used to execute strings
print('Hello there')

# end parameter is used to add multiple word in same line
print("Hello there", end=' ')
print("My name is Karishma")

# numbers dont require to be in quotes
print(12221)
print(12.33)
print(5)

# Math inside the print function
print(8*9)
print(1234-354)
print(12/3)

# Printing both number and string
print("I am",25,"years old.")


# changing the type of variable

x = 3;
y = str(x)

z= '45'
w= float(z)

v= int(z)

print(x,y,z,w,v)

# print(type.x, type.y, type.z, type.w, type.v)
print(type(x), type(y), type(z), type(w), type(v))

# Assigning multiple values to variable.
ab, cb, db = 'first variable', 'second variable', 'third variable'

xx=xy=xz = 'Orange'

print(ab,cb,db)
print(xx,xy,xz)

# unpacking error
# t,u,o = "Hello World"
# print(t,u,o)

# '+' in numbers its mathematical operator with strings it is used for appending 

val1 = "My "
val2 = "Name "
val3 = "is karishma"

a1=10
a2=20
a3=30

print(val1+val2+val3)
print(a1+a2+a3)
print('Hello', 'World')

# gobal & local variable

# str1 is a global variabl and can access outside a function
str1 = "my name is "

def PrintName():
#  name 1 is local variable and can only used inside the function
    name1="Karishma K Krishnan"
    print(str1, name1)
PrintName()
# print(str1+name1)


# gobal keyword is used to make a local variable Gobal

str2 = "My place name is "

def PrintPlaceName():
   global place 
   place = "Wayanad"
   print(str2+place)

PrintPlaceName()
print(str2+place)