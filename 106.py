# calling a class method from another class method

class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print(" Var is =", self.var)
    def add2(self):
        self.display()# in add2() we are calling display() method
        self.var += 2
        self.display()  # calling the class method display()

obj= ABC(10)
obj.display()
obj.add2()
        
