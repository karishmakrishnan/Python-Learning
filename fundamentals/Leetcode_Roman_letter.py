s = "MCMXCIV"
roman_letter = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
converted_sum = roman_letter[s[0]]
for i in range(len(s) - 1, 1, -1):
    if (i == len(s)-1):
        converted_sum += roman_letter[s[i]]
    elif(roman_letter[s[i]] < roman_letter[s[i-1]]):
        converted_sum -= roman_letter[s[i]]
    else:
        converted_sum += roman_letter[s[i]]
print(converted_sum)