#setter and getter
from msilib.schema import Class

class Book:
    def __init__(self, price=40):
        self.price = price
    
    def setprice(self,price):
        self.price = price
    
    def getprice(self):
        return self.price


b1 = Book()
print(b1.getprice())
b1.setprice(45)
print(b1.getprice())

b2 = Book(20)
print(b2.getprice())
