# python performs automatic garbage collection. it deletes all the objects
# that are no longer needed and that gone out of scope to free the memory
# space
# class methods: methods defined in a class are called by instance of a class
# these will take self as the first argument.
# class methods are little different from these ordinary methods.
# first they are called by a class, second the first argument of the classmethod
# is cls but not self. class methods are marked with a classmethod decorator
# what are methods defined after classmethod all those considered as classmethods
class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    @classmethod
    def square(cls,side):
        return cls(side,side)

s=rectangle.square(10) # using classmethod
print("area = ",s.area())

t=rectangle(4.5,5.5)  # using init method
ar=t.area()
print(ar)
