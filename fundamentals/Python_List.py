# Python List

mylist  = [1,2,3,4,5]
print(mylist)
print(mylist[3])

mylist2 = ['as', 'like', 'mat']
print(mylist2)

mylist3 = ["karishma", 13, "begaluru", 23.78]
print(mylist3)

mylist3[3] = mylist2[2]
print(mylist3)

mylist3[0:2] = mylist2[0:2]
print(mylist3)

mylist4 = list((1,2,3,4,5,6,7,8,10))
print(mylist4)
print(len(mylist4))

# negative indexing
# [10, 20, 30]
# -3    -2  -1 -->negative index

print("Negative indexing")

mylist5 = [10, 20, 30]
print(mylist5[-3])
print(mylist5[-3:-1])
mylist5[-3:-1] = [100, 200]
print(mylist5)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
thislist.insert(2, "watermelon") # index, value
print(thislist)
thislist.append("orange")# add the item to the end
print(thislist)
# extend() used to append another list/tuple,set,dictionary to current list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #mentioning the index
print(thislist)
thislist.pop() #remove the last item from the list
print(thislist)
thislist = ["apple", "banana", "cherry"]
del thislist[0] # delete the specific value
print(thislist)
del thislist # delete the entire list

# loop through list
List = ["lion", "rabbit", "parrot"]

for x in List:
    print(x)
# loop through index
    
for x in range(len(List)):
    print(List[x])

# range() in python
    
for i in range(10):
    print(i)

for i in range(2,9):
    print(i)

for i in range(0,10,1):
    print(i)
# While loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "k" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
# newlist = [expression for item in iterable if condition == True]

newlist = [x for x in fruits]
print(newlist)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)
newlist = [x.upper() for x in fruits]
print(newlist)
newlist = ['hello' for x in fruits] #all the value will be hello in newlist
print(newlist)
# orange instead of banana
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

# List sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Cutomizing the sort function.
def myfunc(n):
      return abs(n - 50)

# sort the list like how close the number to 50
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)#case sensitive sort of the list
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# copying the list

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join 2 list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)