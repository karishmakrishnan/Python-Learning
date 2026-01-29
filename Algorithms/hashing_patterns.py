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

