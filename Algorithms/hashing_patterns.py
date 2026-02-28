# use dic/set to store informations so lookup takesO(1)
# Patterns: Frequency counting

# Count occurance

s = "aabbbcdd"
frequency = {}

for char in s:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

print("The CHAR with frequency:", frequency)

# find duplicate & non-repeating elements in string

for char,counter in frequency.items():
    if counter > 1:
        print(f"The charector has duplicate {char}: {counter}")
    else:
        print(f"The non-repeating elements are: {char}")

# anagram using python

frequency2 = {}
s2 = "aaddbbbc"
for char in s:
    if char not in frequency2:
        frequency2[char] = 1
    else:
        frequency2[char] += 1

if frequency == frequency2:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")

# set based hashing problems
arr = [1, 2, 3, 4, 2]
seen = set()
duplicate = False

for x in arr:
    if x in seen:
        duplicate = True
        break
    seen.add(x)
print(duplicate)

# check uniqueness in an array
arr = [1,2,3,4,2]
unique = set()
is_unique = True

for x in arr:
    if x not in unique:
        unique.add(x)
    else:
        is_unique = False
        break
print("The array has only unique elements: ", is_unique)
print(unique)

# Find two number sum to target
arr = [2, 7, 11, 15]
target = 9

seen = set()
found = False

for num in arr:
    if target - num in seen:
        found = True
        break
    seen.add(num)
if(found):
    print(f"The target {target} is sum of {seen}")
else:
    print("Cound not find the values in array gives target: ", target)

print("hello" == "Hello")