# program to demonstrate a method behaving like an attribute
class student:
    def __init__(self,first,last):
        self.__first__= first
        self.__last__ = last
    @property
    def name(self):
        return "%s %s "%(self.__first__,self.__last__)

s=student("sowmya","mohan")
print(s.name) # normally a method will called as name() here it was called
              # like an attribute

print(s.__first__)
#print(s.__last__)
