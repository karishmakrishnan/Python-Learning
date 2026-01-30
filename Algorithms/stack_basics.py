s = "(())("
stack = []

for char in s:
    if char == '(':
        stack.append(char)
    elif len(stack) != 0 and char  == ')':
        stack.pop()
    else:
        print("Invalid parenthesis")
if len(stack) == 0:
    print("valid")
else:
    print("Invalid")
