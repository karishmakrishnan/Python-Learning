# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.




class Solution:
    def get_common_str(self,str1, str2):
            stack = []
            rev_str = list(reversed(str2))
            # i = 0
            for i in range(len(str2)):
                # stack.append(str1[i])
                # # print(stack)
                # if(stack and rev_str and stack[-1] != rev_str[-1]):
                #     stack.pop()
                # elif(rev_str and stack and stack[-1] == rev_str[-1]):
                #     rev_str.pop()
                if str1[i] == str2[i]:
                    stack.append(str1[i])
                else:
                    # stack = ""
                    return ''.join(stack)
                    break
            print(stack)
            return ''.join(stack)
    def longestCommonPrefix(self, strs) -> str:
        small_str = ""
        min_len = float("inf")
        common = min(strs, key=len)
        print(common)
        if len(strs) == 1:
            return strs[0]
        for s in strs:
            print(s)
            common = self.get_common_str(s, common)
            # if common == "":
            #     return ""
            #     break
        return common