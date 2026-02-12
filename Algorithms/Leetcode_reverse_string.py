# Reverse stringclass Solution:
# def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
# reverse_list = []
# size = len(s) - 1
# while(size > 0):
# s.append(s[size])
# size -= 1
# return reverse_list
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

s = ["h","e","l","l","o"]
left = 0
right = len(s) - 1
temp = ""

while (left <= right):
    temp = s[left]
    s[left] = s[right]
    s[right] = temp
    left += 1
    right -= 1
print(s)



