#INHERITANCE AND POLYMORPHISM
#Polymorphism refers to a subclass's ability to adapt
# a method that already exists in its superclass to meet its needs.
#i.e here __rep__() class is used by both subclass according to its requirnment

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()},pages: {self.pages}"


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    #POLYMORPHISM: subclass use function defined in main class already
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()},branch:{self.branch}"


#object creation
novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 200, 'IT')

print(novel1)
print(academic1)