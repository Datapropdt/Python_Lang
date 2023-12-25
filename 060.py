#'''doc strings: documentation strings
#def functionname(parameters):
#    "documentation string" 
#    function stmts
#    return(expression)
# program to show multiline docstring
# '''

def func():
   # priyanka normal text will give an error
   # greeshma normal text will give an error
   
    """the program prints just  a message
    it will display hello world!!!"""

    print("hello world!!!")

def func1():
    '''the program prints just  a message of func1
    it will display hello world!!!'''

    print("hello world!!!")

print(func.__doc__) # to get the docstrings of the function
print(func1.__doc__)

func() # to run the function
func1()
