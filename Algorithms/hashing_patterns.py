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