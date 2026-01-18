# python decorator
# decorator is the way to pass function as an argument to another function 

def my_decorator(function):
    print("Starting of the decorator")
    function()
    print("end of the decorator")

@my_decorator
def normalFunction():
    print("This is my decorator normal function")

normalFunction