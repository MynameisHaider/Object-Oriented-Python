"""
OOP IN PYTHON:
In OOP, class defines what are the attributes its object has, and how is its behaviour. 
Object, on the other hand is an instance of the class.
Objects are not only data and not only functions, but combination of both.
Objects (sometimes called instances) of User class do not have any attributes. 
Instance attributes are defined and initialized in Python class by a special 
method called constructor. 
An object a is declared. It automatically calls __init__() constructor to initialize it attributes.
Its contents are shown when display() method is called.

"""
from matplotlib.pyplot import cla


class User:
    "docstring of User Class"
    #making a constructor
    def __init__(self):
        self.name ="ali"
        self.email ="alihaider00760@gmail.com"
        self.role = "teacher"
    
    def display(self):
        print("Name",self.name)
        print("email",self.email)
        print("role",self.role)

a =User()
a.display()

class User1:
    "docstring of User1 class"
    def __init__(self,name='a',age='24',role='abc'):
        self.name = name
        self.age = age
        self.role = role
    
    def displayUser1(self):
        print("Name:",self.name)
        print("age:",self.age)
        print("role:",self.role)

obj1 = User1()
obj1.displayUser1()
obj2 = User1("lala","45","instructor")
obj2.displayUser1()