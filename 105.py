#public and private data members
#public variables are defined in the class and can be accessed from anywhere in
# the program using . (dot) operator. from with in the class as well as from
# outside the class.
# private variables defined with in the class with __. can be accessed with
# in the class but not outside of the class.

class ABC():
    def __init__(self, var):
        self.__var = var
    def __display(self): # it is a private method , preceeded by __
        print("from class method , var = ",self.__var)

    
obj = ABC(10)
obj._ABC__display()
# the private method can be accessed outside the class using an object
