s = "{[()]}"

stack = []
mapping = {')': '(',
           ']': '[',
           '}': '{'
           }
is_valid = True

for ch in s:
    if ch in mapping.values():
        stack.append(ch)
    elif ch in mapping:
    #     if not stack or stack[-1] != mapping[ch]:
    #         is_valid = False
    #         break
        stack.pop()

print(stack)
if is_valid and not stack:
    print("Valid")
else:
    print("Invalid")

