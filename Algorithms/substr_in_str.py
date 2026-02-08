# find the substring in given string 

str1 = "flight"
target = "flow"

stack = []
rev_target = list(reversed(target))

print(rev_target)

for s in str1:
    stack.append(s)
    if(stack and stack[-1] != rev_target[-1]):
        stack.pop()
    elif(rev_target and stack[-1] == rev_target[-1]):
        rev_target.pop()
print(stack)