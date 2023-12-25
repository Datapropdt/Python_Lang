# program using @property and @setter

class sample:
    def __init__(self,val):
        self.val=val
    @property
    def val(self):
        return self.__val
    @val.setter
    def val(self,val):
        self.__val = val

s = sample(20)
print(s.val)
s.val = 1000  # by using setter property we can set the values to members
print(s.val)
