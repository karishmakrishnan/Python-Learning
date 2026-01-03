# A set is a collection which is unordered, unchangeable*, and unindexed.
# Set can store mulpiple values in a singles variable
# Set items are unordered, unchangeable, and do not allow duplicate values, but you can remove items and add new items.
thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}
myset = {"apple", "banana", "cherry"}
print(type(myset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# Accessing set
# You cannot access items in a set by referring to an index or a key.
# You can access using for loop
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("banana" not in thisset)

# Add&Remove item to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# adding the one set to another
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# Remove/discard
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset.remove("apple")
print(thisset)

# To remove random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# loop through set 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)# retyrns a new set | same as union()
print(set3)
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# common item from both the set you can & for intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# The difference()/ - method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)