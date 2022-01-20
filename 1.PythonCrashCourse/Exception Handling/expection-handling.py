#Exceptional handling

# The try statement lets you test a block of code for errors.
# The except statement lets you handle the error.
# Different types of errors are
# Errors:
# SyntaxError: Raised when there is a syntax error in Python code
# NameError: Raised when a variable is not found
# TypeError: Raised when a variable is used incorrectly
# ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero
# IndexError: Raised when an index of a sequence is out of range
# KeyError: Raised when a key is not found in a dictionary
# AttributeError: Raised when an attribute that doesn't exist is accessed
# ImportError: Raised when an import statement fails
# ModuleNotFoundError: Raised when a module is not found
# FileNotFoundError: Raised when a file is not found
# ValueError: Raised when a variable is assigned a value that has an inappropriate type
# AssertionError: Raised when an assert statement fails
# EOFError: Raised when the input() function hits an EOF
# KeyboardInterrupt: Raised when the user hits the interrupt key (normally Ctrl+C or Ctrl+D) during input()
# IndentationError: Raised when the Python code is not properly indented
# TabError: Raised when the wrong number of tabs or spaces are used for indentation
# SystemError: Raised when the interpreter finds an internal problem, but cannot be specifically identified
# SystemExit: Raised when Python interpreter is quit by calling the sys.exit() function
# Warning: Raised when the interpreter encounters a possible problem
# DeprecationWarning: Raised when the interpreter encounters a deprecated feature

# try :
#     #statements in try block
# except :
#     #executed when error in try block

# try - except 
try:
    a=5
    b='0'
    print(a/b)
except:
    print('Some error occurred.')
print("Out of try except blocks.")




## Program to handle multiple errors with one
# except statement
# Python 3
 
def fun(a):
    if a < 4:
 
        # throws ZeroDivisionError for a = 3
        b = a/(a-3)
 
    # throws NameError if a >= 4
    print("Value of b = ", b)
     
try:
    fun(3)
    fun(5)
 
# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")



    # Python program to demonstrate finally
 
# No exception Exception raised in try block
try:
    k = 5//0  # raises divide by zero exception.
    print(k)
 
# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")
 
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')







    # Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not