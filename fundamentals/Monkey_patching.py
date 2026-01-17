# Monkey patching
# monkey patching is dynamically modifying the methods in python

class Person:
    def __init__(self, name):
        self.name = name
    
    def greetings(self):
        return f"hello Everyone, I'm {self.name}"


person = Person("Karishma")

def new_greet(self):
    return f"Hi, I am {self.name}!"
def say_goodby(self):
    return f"Good bye {self.name}"

Person.greetings = new_greet
Person.say_goodby = say_goodby

print(person.greetings())
print(person.say_goodby())

# Monkey patching in Python allows you to modify or extend the behavior of classes and
# modules at runtime. While this can be useful for applying temporary fixes, adding
# functionality, or during testing, it should be used sparingly and with caution due to potential
# risks such as maintainability issues and conflicts with future updates. Understanding the
# implications and limitations of monkey patching is essential to use it e