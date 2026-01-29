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


