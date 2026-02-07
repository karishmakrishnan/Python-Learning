s = "[{()}]"

stack = []
mapping = {')': '(', '}': '{', ']': '['}
is_valid = True

for char in s:
    if char in mapping.values():      # opening brackets
        stack.append(char)
    elif char in mapping:             # closing brackets
        if not stack or stack[-1] != mapping[char]:
            is_valid = False
            break
        stack.pop()

if is_valid and not stack:
    print("Valid parenthesis")
else:
    print("Invalid parenthesis")
