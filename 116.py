# program using @property and @setter

class sample:
    def __init__(self,var):
        self.var=var
    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self,var):
        self.__var = var

s = sample(20)
print(s.var)
s.var = 100
print(s.var)
