# Python has several functions for creating, reading, updating, and deleting files.
# Modes of file
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# open() function is used to open a file and it accept file name and mode

file = open("MyDoc.txt", "+rt") #file object is created
print(file.read())
print("===============================")
file2 = open("..\Level-2-Excercise\Document.txt","r")
print(file2.read())

print("===============================")
with open("MyDoc.txt") as f:#close the file automatically
  print(f.read())

#   always close the file once you done with it
f = open("MyDoc.txt")
print(f.readline())
f.close()

with open("MyDoc.txt") as f: #read first 5 char of file
  print(f.read(5))
f = open("MyDoc.txt","r")
print(f.readline()) #return first line of the file 

# Looping through file
with open("MyDoc.txt") as f:
  for x in f:
    print(x,end="")
print("\n")
print("===============================")
with open("MyDoc.txt") as f:
  print(f.readline())
  print(f.readline())