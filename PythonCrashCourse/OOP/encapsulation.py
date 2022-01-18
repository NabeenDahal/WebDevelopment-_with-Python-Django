# Encapsulation
# Public, private, protected access modifiers
#   - public: accessible from anywhere
#   - private: accessible only from inside the class 
#   - protected: accessible only from inside the class and from its subclasses but also can be accessed from outside the class but it a convention not to call protected methods from outside the class
#  -private: created using __ (two underscores) before the variable name
#  -protected: created using _ (one underscore) before the variable name

class Student:
    schoolName = 'st xaviers' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute



std = Student("nabin dahal", 23)
print(std.schoolName)
print(std.name)
print(std.age)
std.age = 25
print(std.age)




class Student:
    _schoolName = 'st xaviers' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute

std = Student("pawan", 18)
print(std._schoolName)
print(std._name)
std._age = 21
print(std._age)



# Python program to
# demonstrate private members
 
# Creating a Base class
 
 
class Base:
    def __init__(self):
        self.a = "NAbin Dahal"
        self.__c = "Nabin dahal"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
obj1 = Base()
print(obj1.a)
# print(obj1.__c)  Here uncommenting this line will show attributes error
 
# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as private member of base class is called inside derived class