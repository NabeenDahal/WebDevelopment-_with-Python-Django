# Class and Objects
# Class is a user defined data type/structure 
# Class contains data members and member functions
# Data members are variables that are part of the class, also called as attributes
# Member functions are functions that are part of the class, also called as methods

# Objects are instances of a class
# Objects can access the data members and member functions of a class

# A Single Class can have multiple objects/instances
# All the objects of a class share the same data members and member functions
# But the objects have different states i.e different values of data members

# self is a reference variable that refers to the current instance of the class
# class methods must have self as the first argument


# """
# class syntax:
# class ClassName:
#     <statement-1> variables, functions
#     .variable  => data members / attributes
#     function() => member functions / methods
#     .
#     .
#     <statement-N>
# object creation:
# object_name = ClassName()
# """

        
class person:
    # data members/attributes:
    a = 'Nabin Dahal'
    b = 'Milan Rai'
    c = 'Pawan Thapa'
    # members functions/methods:
    def person1(self):    #self = obj1
       
        print(f'Hello, I am a {self.a}!')  #obj1.a
    def person2(self):
        print(f'Hello, I am a {self.b}!')
    def person3(self):
        print(f'Hello, I am a {self.c}!')
    def person4(self):
        print(f'Hello, I am a Bishal magar!')
        

obj1 = person()  #object creation or instance creation
obj1.person1()    
obj1.person2()
obj1.person3()
obj1.person4()