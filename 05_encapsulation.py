#public Members
from turtle import st


class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute

obj1 = Student("haider",25)
print("name:",obj1.name)
print("age:",obj1.age)
obj1.age = 30 # since it is public data member so we can access it outside function also
print("new age is: ",obj1.age)

"""
********************************************************************************
"""
print("***********************************************")
#protected Members
class Student1:
    _schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self._name=name # protected instance attribute
        self._age=age #  protected instance attribute

std1 = Student1("lala",20)
print("name:",std1._name)
print("age",std1._age)

std1._age = 25 #it is protected data member but still we can access it outside function
print("new age is: ",std1._age)

"""
**************************************
"""
print("*****************************************")
#private members
class Student2:
    __schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.__name=name # private instance attribute
        self.__age=age # private instance attribute

    def __display(self):
        print("this is private function")


std2 = Student2("haider",11)
#print("Name: ",std2.__name) #IT WILL NOT WORK
#print("age: ",std2.__age) # IT WILL NOT WORK

#to access private data member we use follow pattern.
#object._className__dataMemberName
print("name",std2._Student2__name)

#You use getter and setter methods to access private attributes.

print(std2._Student2__display()) # accessing private function

#modify private data member
std2._Student2__name = "haider ali"
print("Name:",std2._Student2__name)
"""
Python provide name mangling for private data members
Thus, Python provides conceptual implementation of public, protected,
and private access modifiers,
but not like other languages like C#, Java, C++.
"""
