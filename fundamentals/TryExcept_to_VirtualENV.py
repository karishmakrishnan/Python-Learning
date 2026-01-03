# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
import math
try:
  print(x)
except:
  print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
# finally
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# example
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# raise an exception
x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

x = 23

if not type(x) is int:
  raise TypeError("Only integers are allowed")

# string formating
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# None is a special constant in Python that represents the absence of a value.
# Its data type is NoneType, and None is the only instance of a NoneType object.

x = None
print(type(x))
print(x)
print(bool(None))


# function without return statement return none
def myfunc():
      x = 5
x = myfunc()
print(x)

# print("Enter your name:")
# name = input()
# print(f"Hello {name}")

# name = input("Enter your name:")
# print(f"Hello {name}")

# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# x = input("Enter a number:")

# #find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}")

# validating the input
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")