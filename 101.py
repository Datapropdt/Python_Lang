# other special methods
# __repr__(): return string representation of object
# __len__() : returns length of the object
# __cmp__(): used to compare two objects
class ABC():
    def __init__(self,name,var):
        self.name = name
        self.var = var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self, obj):
        return self.var - obj.var
obj = ABC("ABCDEF",10) # is possible because of constructor
print("the value stored in object is :   ",repr(obj))
print("the length of name stored in object is :   ",len(obj))
obj1=ABC("ABCDEF",10)
val=obj.__cmp__(obj1)
print(val)
if val == 0:
    print("both values are equal ")
elif val == -1:
    print("first value is less than second")
else:
    print("second is less than first")
