# ### Tuple in Python

t = ("k", "a")
print(t)
print(t[1])
t2 = tuple(("jkj", "hkh", 898))
print(t2)
print(len(t2))
# -1 is for last column in tuple
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# tuples are immutable/unchngable
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Adding 2 tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

# removing item from tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# packing a tuple
# assigning a value to tuple is called packing
MyTuple = tuple()

MyTuple = ("Kari", "kris", "sulo")#packing

(tari, *kris,sulo) = MyTuple #unpacking

print(tari)
print(kris)
print(sulo)


# loop in tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop using range() and len()
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# While loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 # the tuple values will be twice

print(mytuple)

tp = (1,3,4,5)

tp2 = tp*2
print(tp2)
print(tp2.count(5)) # print the numbers of times the elements present in tuple
print(tp2.index(4)) # print the given value's index
