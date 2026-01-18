# threads in python
# thread is a smallest unit of execution
# share same memory and run concurrently

# simple thread example
import threading

def greetings():
    print("Hello Everyone")

thread = threading.Thread(target=greetings())
thread.start() #begin the execution
thread.join() #main thread wait for it execution

# thread helps in I/O operation mainly
# n/w and db queries

# Thread with arguments

def greetMe(name):
    print(f"Hello {name}, Have a great day")

thread2 = threading.Thread(target=greetMe, args=["Karishma"])
thread2.start()

# race condition in threads
# thread share memory, when multiple threads run at a time it can corrupt the data which is used by all the treads
# we can use lock to ensure only one thread critical section execute at a time

count = 0
count2 = 0
lock = threading.Lock()
def incrementer():
    global count
    for _ in range(100_000): # the loop is running for 100000 times, 
        count +=1
    return count
def increment_with_lock():
    global count2
    for _ in range(100_000):
        with lock:
            count2 +=1
    return count2

thds = []
for _ in range(6): # 6*100,000 times we are running the loop
    thread3 = threading.Thread(target=incrementer)
    thread3.start()
for _ in range(6):
    thread = threading.Thread(target=increment_with_lock)
    thread.start()
print(count)
print(count2)

print(threading.current_thread().name)