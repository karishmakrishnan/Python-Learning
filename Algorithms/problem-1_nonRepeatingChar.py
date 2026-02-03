# non repeating charecter

s = "aabbcdde"

frequency = {}

for char in s:
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

for char, count in frequency.items():
    if count == 1:
        print("The non repeating char:", char)
