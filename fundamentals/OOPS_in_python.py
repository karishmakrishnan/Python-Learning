# OOOPS in python
# Properties are variables that belong to a class. They store data for each object created from the class.

class MyClass:
    x = 10

Object_1 = MyClass()
print(Object_1.x)

del Object_1 # to delete object

#You can create multiple object from the class

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
# print(p2.x)
# print(p3.x)

# pass can be used to make the class empty

# _init_ method is used to initialise the values for object
#  which is always executed when the class is being initiated.

class Person1:
    def __init__(self, name, age):# The first method executed in a class by default
     self.name = name
     self.age = age

p1 = Person1("Emil", 36) #Initiating the class (_init() will be executed here), setting the initial value when creating the object

print(p1.name)
print(p1.age)

# Without _init_() setting the properties manually
class Person:
      pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)

# Setting the default values
class Person:
#   If age is not passed or not seeting it manually, it will be 18
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p1.age = 26
p2 = Person("Tobias", 25)

print("Person 1 : ",p1.name, p1.age)
print("Person 1 : ",p2.name, p2.age)

# passing multiple parameter

class Person:
 def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print("Name: ",p1.name)
print("Age: ",p1.age)
print("City: ",p1.city)
print("Country: ",p1.country)

# self parameter in class
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# Without self, Python would not know which object's properties you want to access:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()

class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()

# Self can be of any name but it has to be first parameter
class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def greet(abc):
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()

# Deleting the property of an object
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
# print(p1.age) # This would cause an error

# class vs object properties
class Person:
  species = "Human" # Class property
  lastname = ""
  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

Person.lastname = "Krishna"

print(p1.lastname)
print(p2.lastname)
print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

# class with methods
# methods are function defined inside the class
# methods define the behaviour of an objected created from the class
# methods can access the properties using self

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


# methods can change the property
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)
print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

# multiple methods in a class
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

# inheritance
class Student(Person):
  pass
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)