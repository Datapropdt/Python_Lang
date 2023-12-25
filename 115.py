# program to use get and set functions to retrieve and set a value

class sample():
    def __init__(self,var):
        self.var = var
    def display(self):
        print(self.var)
    def get(self):
        return self.var
    def set(self,var):
         self.var = var
s = sample(20)
s.display()
s.set(10)
s.display()
print(s.get())
    
    
