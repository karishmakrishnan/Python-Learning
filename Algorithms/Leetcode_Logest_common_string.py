List = ["flower","flow","flight"]
small_str = ""
min_len = float("inf")
for s in List:
    if min_len < len(s):
            min_len = len(s)
            small_str = s

def get_common_str(str1, str2):
    stack = []
    rev_str = list(reversed(str2))
    for char in str1:
        stack.append(char)
        if(stack and rev_str and stack[-1] != rev_str[-1]):
            stack.pop()
        elif(rev_str and stack[-1] == rev_str[-1]):
            rev_str.pop()
    return ''.join(stack)
if len(List) == 1:
    print(List[0])
else:
    common = small_str
    for s in List:
        common = get_common_str(s, common)
    print(common)