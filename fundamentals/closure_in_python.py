# closure in python
# A closure is a nested function that captures and remembers variables from 
# its enclosing scope even after the outer function has finished execution.

# Every has inner function but all the nested functions are not closure

# This is a nested function, it is not using/remembering any variables of outer function
def outter():
    def inner():
        print("Hello, I'm inner function")
    print("Helllo, I'm outer function")
    inner()

# This perticular nested function is also not closure, the x defined in outer and inner has its own scope, 
# The variable x in outter is not used/remembered by inner
def myoutter():
    x=20
    def inner():
        x=30
        print("inner x: ",x)
    print("outer x: ", x)
    inner()

# Here using nonlocal we are making the outer x accessible to inner, inner is using the outer memory aand the scope is also in that
def myoutter2():
    x = 90
    def inner():
        nonlocal x
        x = 78
        print(x)
    print("Outter: ", x)
    inner()
    print("outer:", x)
# Another closure with example
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5)) 
outter()
myoutter()
myoutter2()