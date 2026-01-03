# A function is a block of code which only runs when it is called.

# A function can return data as a result.

# A function helps avoiding code repetition.

def greet():
  print("Hello from a function")
greet()

def my_function():
      print("Hello from a function")

my_function()
my_function()
my_function()
# When a function reaches a return statement, it stops executing and sends the result back:
def get_greeting():
      return "Hello from a function"

message = get_greeting()
print(message)

def my_function(fname, lname):
      print(fname + " " + lname)

my_function("Emil", "Refsnes")


# if nothing is passed name will be friend
def my_function(name = "friend"):
      print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

# assigning the value while passing
def my_function(animal, name):
      print("I have a", animal)
      print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

# You can combine both argument types in the same function.
# Arguments before / are positional-only, and arguments after * are keyword-only:
def my_function(a, b, /, *, c, d):
      return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))


# Using **kwargs to accept any number of keyword arguments:
def my_function(**kid):
      print("His last name is " + kid["lname"])
# You can use both *args and **kwargs in the same function.
# The order must be:
# regular parameters
# *args
# **kwargs
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

my_function(fname = "Tobias", lname = "Refsnes")

x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)

# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

def changecase(func):
    def myinner():
      return func().upper()
    return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())