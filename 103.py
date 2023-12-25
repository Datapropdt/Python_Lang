#public and private data members
#public variables are defined in the class and can be
#accessed from anywhere in
# the program using . (dot) operator. from with in the
#class as well as from
# outside the class.
# private variables defined with in the class with __.
#can be accessed with
# in the class but not outside of the class.

class ABC():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def display(self):
        print("from class method , var1 = ",self.var1)
        print("from class method , var2 = ",self.var2)


obj = ABC(10,20)

obj.display()

print("from main module , var1 = ",obj.var1)
print("from class method , var2 = ",obj.var2)
# var2 is a private variable cant access outside the class
