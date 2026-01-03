dictionary  = {
    "Name": "Karishma",
    "Place": "Karnataka",
    "Age": 26
}
print(dictionary)
print(len(dictionary))

dictionary_2 = {
    "Name" : ("kari", "Madhu", "Sulo"),
    "Place": ["Karnataka", "Kerala"],
    "Electric": False,
    "Numbers": 10
}

print(dictionary_2["Name"])

x = dictionary_2["Name"]
y = dictionary_2.get("Place")

print(x)
print(y)

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# the list of all the keys in dictionary
l = dictionary_2.keys()
print(l)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

val = dictionary_2.values()
print(val)

# The items() method will return each item in a dictionary, as tuples in a list.

itm = dictionary_2.items()
print(itm)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change the value of dictioanry
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["year"] = 2018
print(thisdict)

# update() 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

thisdict["color"] = "red"

# Removing item from list
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")# removing the item with key
print(thisdict)

# removing the last inserted item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

# del key with dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.
# empty the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict.clear()
print(thisdict)

for x in thisdict:#print the key in dictioanry
      print(x)
for x in thisdict:#print the value of a dictionary
  print(thisdict[x])

# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)

# copy dictionary
# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)