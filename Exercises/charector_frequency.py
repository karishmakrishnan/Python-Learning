# Count charector frequency in a string using dictionary
str1 = "Hello Everyone"
char_count = {}

for char in str1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)