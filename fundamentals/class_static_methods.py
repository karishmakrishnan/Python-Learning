# class methods and static method

# A class method is a method that is bound to the class and not the instance of the class. It
# can access and modify the class state that applies across all instances of the class. Class
# methods are defined using the @classmethod decorator and take cls as the first
# parameter, which refers to the class itself.

# Static methos are regular function which is in scope of class namespace
# It is not bound to the class or it instance
# It doesn't take self,cls as argument


class MyClass:
    Myclass_variable = 0

    @classmethod
    def MyClassMethods(cls):
        cls.Myclass_variable +=1
        return cls.Myclass_variable
    @staticmethod
    def add(a: int, b: int):
        return a+b
# you dont need to create an instance to access the classmethods
# The changes made to the variable using classmethod is in scope of the class
# The first parameter is always cls and refere to the class.
# the modification applies to all the instance of the class.
MyClass.MyClassMethods()
MyClass.MyClassMethods()
print(MyClass.MyClassMethods())
print(MyClass.Myclass_variable)

print("From static method: ", MyClass.add(23,78))