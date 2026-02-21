# longest substring with maximum distinct element is 2

s = "ccaabbb"
freq = {}
char_list = []
left = 0
right = 0
distinct = 0
max_len = 0
left_max = 0
right_max = 0

for right in range(len(s)):
    if s[right] not in freq:
        freq[s[right]] = 1
        distinct += 1
    else:
        freq[s[right]] += 1
    if distinct <= 2:
        char_list.append(s[right])
        if max_len < ((right - left) +1):
            max_len = (right - left) + 1
            left_max = left
            right_max = right
    else:
        while len(freq) > 2:
            popitem = char_list.pop(0)
            if popitem not in char_list:
                freq.pop(popitem)
                distinct -= 1
            left += 1
    
print("max substring with 2 elements:", max_len)
print("The substring is: ", s[left_max:right_max+1])