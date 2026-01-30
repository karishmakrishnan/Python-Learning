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

# improved version
s = "(())("
stack = []
is_valid = True

for char in s:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if stack:
            stack.pop()
        else:
            is_valid = False
            break

if is_valid and not stack:
    print("Valid")
else:
    print("Invalid")