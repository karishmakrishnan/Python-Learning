# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 


import re
import string
s= "jkj"
print(s.isalpha())
print(s.isnumeric())
class Solution(object):
    def clean_string(self, s):
        lower_str = s.lower()
        chars = r"[a-z0-9]+"
        list_chars = re.findall(chars, lower_str)
        cleaned_str = "".join(list_chars)
        return cleaned_str
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_palindrom = True
        
        left = 0 
        if s == " " or s == "":
            is_palindrom = True
        else:
            cleaned = self.clean_string(s)
            right = len(cleaned) - 1
            if cleaned == "" or cleaned == " ":
                is_palindrom = True
            else:

                while(left <= right):
                    if left < right and cleaned[left] != cleaned[right]:
                        is_palindrom = False
                        break
                    else:
                        left += 1
                        right -= 1
          
        return is_palindrom
