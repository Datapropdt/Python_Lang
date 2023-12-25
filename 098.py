# class is a collection of objects
# object is instance of a class
class A:
    v1=10
    v2="somya"
    def show(self):
        print(" calling show ")

a=A()  # a is object of class A
b=A()   # b is another object of class A
print(a.v1,a.v2) # the members of a class can be accessed with the help of
print(b.v1,b.v2) # an object and a dot(.) operator
   
a.show()  # a method can be called using object.methodname(), . dot operator
b.show()
