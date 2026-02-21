min_len = float('inf')
left_min = 0
right_min = 0
frq_t = {}
frq_w = {}
act_match_count = 0
matcnt = 0
left = 0
right = 0
s = "AAABBC"
t = "ABC"
need = {}
window = {}
for char in t:
    if char not in need:
        need[char] = 1
    else:
        need[char] += 1
required = len(need)
formed = 0

left = 0


for right in range(len(s)):

    # expand window

    # if frequency matches, increase formed
    if s[right] not in window:
            window[s[right]] = 1
    else:
        window[s[right]] += 1
    if s[right] in need and window[s[right]] == need[s[right]]:
         formed += 1
    
    while formed == required:
        # update answer

        # shrink from left
        # if frequency falls below required, decrease formed
                # Update minimum window
        if right - left + 1 < min_len:
            min_len = right - left + 1
            start = left

        # Remove left character
        left_char = s[left]
        window[left_char] -= 1

        # If removing breaks requirement
        if left_char in need and window[left_char] < need[left_char]:
            formed -= 1

        left += 1
        # pass

if min_len == float("inf"):
    print("")
else:
    print(s[start:start + min_len])