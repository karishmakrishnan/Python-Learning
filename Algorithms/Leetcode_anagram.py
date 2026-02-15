# Given two strings s and t, return true if t is an anagram of s, and false otherwise.s
# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_angram = False
        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))
        print(s1)
        print(t1)
        if s1 == t1:
           is_angram = True
        return is_angram 