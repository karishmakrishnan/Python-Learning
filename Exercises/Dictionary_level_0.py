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
# Level 3 – Practical Coding Questions
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

sum_val = 0;

for val in dic_list.values():
    sum_val += val
print("Sum of values in dic_list:", sum_val)
# Level 5 – Dictionary Comprehension
# What is dictionary comprehension?
# Dictionary comprehension is a concise way to create dictionaries using a single line of code.
# It consists of an expression pair (key: value) followed by a for statement inside curly braces {}.
# Example: Create a dictionary that maps numbers to their squares for numbers from 1 to 5.
squares = {x: x**2 for x in range(1, 6)}
print(squares)
# it is equivalent to the ternary operator in list comprehension.
# Example: Create a dictionary that maps numbers to their squares for even numbers from 1 to 10.
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares) 
# Create a dictionary that maps characters to their ASCII values for characters in the string "hello".
ascii_values = {char: ord(char) for char in "hello"}
lst = ["apple", "banana", "cherry"]
lst_dict = {fruit: fruit for fruit in lst}
print(lst_dict)

multiple_squares = {x: x**2 for x in range(1, 25) if x%5 == 0}
print(multiple_squares)

swap_dict = {value: key for key, value in multiple_squares.items()}
print(swap_dict)

nested_dict = {x: {y: y**2 for y in range(1, 4)} for x in range(1, 4)}
print(nested_dict)
# Are dictionaries mutable?
# Yes, dictionaries are mutable, meaning you can change their content without changing their identity.
# Why must dictionary keys be immutable?
# Dictionary keys must be immutable because they need to have a fixed hash value that does not change during their lifetime.
# This allows for efficient lookups and ensures the integrity of the dictionary structure.
# How hashing works in dictionaries?
# Hashing is a process that converts an object (like a key) into a fixed-size integer (hash value) using a hash function.
# This hash value is used to determine the index where the key-value pair will be stored in the dictionary.
# When you look up a key, the hash value is computed again to find the correct index quickly.   
# This allows for fast access to values based on their keys.
# What is a hash collision?
# A hash collision occurs when two different keys produce the same hash value.
# In such cases, the dictionary must handle the collision to ensure that both key-value pairs can be stored and retrieved correctly.
# Python dictionaries handle collisions using a technique called "open addressing" or "chaining," depending on the implementation.
# What happens internally when a dictionary grows?
# When a dictionary grows (i.e., when more key-value pairs are added), 
# Python may need to resize the underlying data structure to maintain efficient access times.
# This involves creating a new, larger array and rehashing all existing key-value pairs to their new positions in the array.
# This process is known as "rehashing" and helps to keep the average time complexity for lookups, insertions, and deletions close to O(1).
# Can you use a tuple as a dictionary key? Why?
# Yes, you can use a tuple as a dictionary key because tuples are immutable.
# Since dictionary keys must be immutable and hashable, tuples meet these criteria, allowing them to be used as keys in dictionaries.
# However, the elements within the tuple must also be immutable for the tuple to be hashable.
# For example, a tuple containing only strings and numbers can be used as a dictionary key, but a tuple containing a list cannot.
tuple_key_dict = {(1, 2): "point A", (3, 4): "point B"}
print(tuple_key_dict)