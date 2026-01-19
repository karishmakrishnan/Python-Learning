# Count charector frequency in a string using dictionary
str1 = "Hello Everyone"
char_count = {}

for char in str1:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

# Print non-repeating characters
for key,value in char_count.items():
    if value == 1:
        print(f"The character {key} is non-repeating")

# Count charector frequency in a string using collections module
from collections import Counter
str1 = "Hello Everyone"
char_count = Counter(str1)
print(char_count)

# Count charector frequency in a string using defaultdict
from collections import defaultdict 
str1 = "Hello Everyone"
char_count = defaultdict(int)
for char in str1:
    char_count[char] += 1
print(dict(char_count))

# Count charector frequency in a string using pandas
import pandas as pd
str1 = "Hello Everyone"
char_series = pd.Series(list(str1))
char_count = char_series.value_counts() 
print(char_count)
# print(char_series)

