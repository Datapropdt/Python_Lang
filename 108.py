# like functions and modules class can also has docstring that can be accessed
# using classname.__doc__
# class ABC:
#      '''this is doc string '''

# program to add variables to a class at runtime

class ABC():
    def __init__(self, var):
        self.var = var
    def display(self):
        print(" var = ",self.var)

obj = ABC(10)
obj.display()
obj.new_var = 20 # variable added at runtime
print(" new var = ",obj.new_var)
obj.new_var = 30 # variable added at runtime
print(" new var after change = ",obj.new_var)

del obj.new_var
print(" new var after deletion = ",obj.new_var) # gives an error


