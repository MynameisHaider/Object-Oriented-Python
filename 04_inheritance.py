from pyparsing import col

class superClass:
    def __init__(self, height ,color ,width):
        self.height = height
        self.color = color
        self.width = width

    def does_stuff(self):
        print("this function does some stuff")
    
# simple inheritance
class subClass(superClass):
    pass


obj1 = subClass('5 feet','red', 12)
print("height:" ,obj1.height)
print("color:" ,obj1.color)
print("width:", obj1.width)
obj1.does_stuff()
obj1.height = 24 # we can access class attribute directly. not a good option
print(obj1.height)

