# garbage collection or destroying objects:
# the process by which python periodically reclaims the unwanted memory is
# known as garbage collection
# ordinary methods are instanciated by a class.

# class methods: are called by a class(not by instance of class)
# the first argument of class method cls not the self
# class method will defined using @classmethod decorator
# class methods are widely used for factory methods, which instantiate an
# instance of class,using diff parameters from those usually passed to
# the class constructor
# program demostrates class method

class rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    @classmethod
    def square(cls,side):
        return cls(side,side)
    
s = rectangle.square(10) # a class method can be called by using classname followed by
                         # class method
print("AREA = ",s.area())

