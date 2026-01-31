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
        if not stack:
            is_valid = False
            break
        stack.pop()

print(stack)
if is_valid and not stack:
    print("Valid")
else:
    print("Invalid")

# for each element in array find the next greates element
arr = [4, 5, 2, 10]

# [5, 10, 10, -1]
next_max = []

for i in range(len(arr)):
    if i == len(arr) - 1:
        next_max.append(-1)
    j = i+1
    max_val = arr[i]
    while(j < len(arr)):
        if(arr[j]> max_val):
            next_max.append(arr[j])
            break
        elif max_val == arr[j]:
            next_max.append(-1)
            break
        j += 1
print(next_max)

# updated version 
arr = [4, 5, 2, 10]
result = [-1] * len(arr)
stack = []

for i in range(len(arr)):
    while stack and arr[i] > arr[stack[-1]]:
        idx = stack.pop()
        result[idx] = arr[i]
    stack.append(i)

print(result)
