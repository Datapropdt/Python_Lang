 # built in class attributes  : can be accessed using .operator
# __dict__ : gives a dictionary containg the class objects
# __doc__ : gives class documentation string
# __name__ :returns the name of the class
# __module__ : returns the name of module in which class defined
# __bases__ : returns the base classes 

class ABC():
    """ this is class doc string"""
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def display(self):
        print(" var1 = ",self.var1)
        print(" var2 = ",self.var2)

obj = ABC(10,12.34)
obj.display()

print(" object.__dict__ :  ", obj.__dict__)
print(" object.__doc__  :  ", obj.__doc__)
print(" class.__name__  :  ", ABC.__name__)
print(" object.__module__ : ", obj.__module__)
print(" class.__bases__ - ", ABC.__bases__)

