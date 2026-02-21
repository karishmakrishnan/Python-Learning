# 🔥 Sliding Window Hard Variant
# Minimum Window Substring

# Example:

# s = "ADOBECODEBANC"
# t = "ABC"
# Output = "BANC"

s = "AAABBC"
t = "ABC"
min_len = float('inf')
left_min = 0
right_min = 0
frq_t = {}
frq_w = {}
act_match_count = 0
matcnt = 0
left = 0
right = 0

for char in t:
    if char not in frq_t:
        frq_t[char] = 1
        act_match_count += 1
    else:
        frq_t[char] += 1
def count_check(left, right, str1, freq):
    count = 0
    for left in range(right+1):
        if str1[left] in frq_t and freq[str1[left]] == frq_t[str1[left]]:
            count += 1
    return count
for right in range(len(s)):
    if s[right] not in frq_w:
        frq_w[s[right]] = 1
    else:
        frq_w[s[right]] += 1
    matcnt = count_check(left, right,s[:right+1], frq_w)
    if matcnt == act_match_count:
        if min_len > right - left +1:
            min_len = right - left + 1
            left_min = left
            right_min = right
        left = right+1 
print("Minimum length of str: ", min_len)
print("The minimum length str is ", s[left: right+1])

        
# Expand right
#     add char to window

#     if char frequency matches required:
#         formed += 1

#     while formed == required:
#         update min window

#         remove left char
#         if removing breaks requirement:
#             formed -= 1

#         move left