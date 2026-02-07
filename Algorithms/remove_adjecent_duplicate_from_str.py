# remove adjecent duplicate from the string
s = "abbaca"
stack = []

for char in s:
    if not stack or stack[-1] != char:
        stack.append(char)
    elif stack and stack[-1] == char:
        stack.pop()
print("The string without ajecent duplicate: ", "".join(stack))