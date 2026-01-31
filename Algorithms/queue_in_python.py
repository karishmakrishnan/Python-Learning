# /Queue in python
# queue in python is first in first out(FIFO)
# python collections have dequeue

from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue) #1,2,3


queue.popleft() #remove element from the front side
print(queue)

# pop element till the queue is empty
while queue:
    node = queue.popleft() # this return the pop value from the queue
    print(node)