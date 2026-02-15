# You are given a string s consisting of lowercase English letters, spaces, and digits.

# Let v be the number of vowels in s and c be the number of consonants in s.

# A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u', while any other letter in the English alphabet is considered a consonant.

# The score of the string s is defined as follows:

# If c > 0, the score = floor(v / c) where floor denotes rounding down to the nearest integer.
# Otherwise, the score = 0.
# Return an integer denoting the score of the string.

 

# Example 1:

# Input: s = "cooear"

# Output: 2

# Explanation:

# The string s = "cooear" contains v = 4 vowels ('o', 'o', 'e', 'a') and c = 2 consonants ('c', 'r').

# The score is floor(v / c) = floor(4 / 2) = 2.


class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        counter = {
            "vovels" : 0,
            "cons" : 0
            }
        v = ['a', 'e', 'i', 'o', 'u']
        c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

        for char in s:
            if char in v:
                counter["vovels"] += 1
            if char in c:
                counter["cons"] +=1
        result = 0
        if counter["cons"] == 0 or counter["vovels"] == 0:
            result = 0
        else:
            result = counter["vovels"] // counter["cons"]
        return result