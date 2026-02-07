# Daily tempreature 
temps = [73, 74, 75, 71, 69, 72, 76, 73]

result = [0] * len(temps)
stack = []   # store indices

for i in range(len(temps)):
    # while stack not empty AND current temp > temp at stack top
        # pop index
        # result[popped_index] = i - popped_index

    # push current index
    while stack and  temps[i] > temps[stack[-1]]:
            popped_index = stack.pop()
            result[popped_index] = i - popped_index
    stack.append(i)

print(result)