# # Create&Write in a file
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

with open("NewDoc.txt", "a") as f:
  f.write("Now the file has more content!")

# #open and read the file after the appending:
# with open("NewDoc.txt") as f:
#   print(f.read())

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())

# Create a new file
# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists
  
# file1 = open("FileX.txt","x") #create filex because it doesn't exit with the same name or error
file2 = open("FileA.txt","a") #create a file if it dosen't exist or no error
file3 = open("FileW.txt","w") #create a file if it doesn't exist or no error

# Delete a file
import os
# os.remove("..\myproject")
 

# os.remove("FileX.txt")

if os.path.exists("demofile.txt"):
      os.remove("demofile.txt")
else:
  print("The file does not exist")

# Detele a folder
import os
os.rmdir("..\myproject")