# Dictionary level 0 exercise
# A dictionary is a collection of key-value pairs.
# In this exercise, you will create a dictionary to store information about a person.
# In python dictionary key is string and value can be any data type.
# Dictionary is defined using curly braces {}.
# Create a dictionary named 'person' with the following key-value pairs:

person = {
    "name": "karishma",
    "age": 25,
    "height": 155
        }
# The vaule in dictionary can be accessed using the key.
print(person)
# Access and print the value associated with the key "name".
# the default value type in dictionary is integer but it can be string as well.
print(person["name"])

for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")
person["weight"] = 40
person["age"] = 26
print(person)

# Level 2 – Dictionary Methods
# the keys() in dictionary returns a view object that displays a list of all the keys in the dictionary.
print(person.keys())
# the values() in dictionary returns a view object that displays a list of all the values in the dictionary.
print(list(person.values()))
# the items() in dictionary returns a view object that displays a list of a dictionary's key-value tuple pairs.
print(person.items())

# pop() method removes the item with the specified key name.
person.pop("height")
print(person)
# popitem() method removes the last inserted key-value pair from the dictionary.
person.popitem()
print(person)
# clear() method removes all items from the dictionary.
person.clear()
print(person)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
vehicle = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
# merging 2 dict
car.update(vehicle)
print(car)

# merge 2 dict using | operator
merged_dict = {**car, **vehicle}
print(merged_dict)
# merge 
lst = ["banana", "apple", "orange","banana","kiwi","apple"]
fruit_count = {}
for fruit in lst:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1
print(fruit_count)

str1 = "hello world"
char_count = {}
for char in str1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

max_val  = 0
min_val = float('inf')
for key, value in fruit_count.items():
    if value > max_val:
        max_val = value
        max_key = key
    if value < min_val:
        min_val = value
        min_key = key
print(f"The most frequent/max fruit is {max_key} with a count of {max_val}")
print(f"The least frequent/min fruit is {min_key} with a count of {min_val}")

reverse_dict = {}
for key, val in char_count.items():
    reverse_dict[val] = key
print(reverse_dict) 

sorted_char_count = dict(sorted(char_count.items()))
print(sorted_char_count)

dict_1 = {'a': 1, 'b': 2, 'c': 3}
for key in dict_1:
    key = None
print(dict_1)

lst1 = [1, 2, 3, 4, 5]
lst2 = ["a", "b", "c", "d", "e"]
zipped_dict = dict(zip(lst2, lst1))
print(zipped_dict)
dic_list = {}

for x in range(len(lst2)):
    dic_list[lst2[x]] = lst1[x]
print(dic_list)

common_keys = [key for key in zipped_dict if key in dic_list]
print("Common keys:", common_keys)
