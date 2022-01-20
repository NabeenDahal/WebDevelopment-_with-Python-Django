# Constructor, __init__, Class Variables, Instance Variables, __str__
# Construcor is a special method that is called when an object is created.
# It is used to initialize the state of the object.

# Class variable is a variable that is shared by all the objects of a class.
# Class variable is accessible by all the objects of the class.
# Class variable is not a part of the object.
# Class variable is also known as static variable.

# Instance variables are variables whose value is assigned inside a constructor or method with self
# Instance variables are accessible by all the objects of the class.
# Instance variable is a part of the object.
# Instance variable is not shared by all the objects of the class.

#__str__ is a special method that is called when an object is converted to a string.
# It is used to return a string representation of the object.

class laptop:
    # Class Variable
    os_type = 'windows'

    # The init method or constructor
    def __init__(self, company):   #self = Obj1 , company = "HP"
        # Instance Variable
        self.company = company   # Obj1.company = "HP"

    # Adds an instance variable
    def setColor(self, color):  # def setColor(obj1, "black"):
        self.color = color  # Obj1.color = "black"

    # Retrieves instance variable
    def getColor(self):	   # def getColor(Obj1):
        return self.color  # return Obj1.color

    def __str__(self):
        return f'{self.company} {self.os_type}'
Obj1 = laptop("HP")  #=> laptop.__init__(obj1, "HP")
Obj1.setColor("black")  #=> laptop.setColor(Obj1, "black")
print(Obj1.company)
# print(Obj1.getColor())  #=> laptop.getColor(Obj1)
print(Obj1.os_type)
# # accessing class variable using class name
# print(laptop.os_type)  #=> "windows"

r = Obj1.__str__()  
print(r)
print(type(r))