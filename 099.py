# class is a collection of objects
# object is instance of a class
# constructor is used to initialize the memebers of a class

#__init__() method (the class constructor will be called automatically without
# an object and dot operactor

class ABC:
    class_var = 0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var
        print(" the object value is:", var)
        print(" the value of class variable is :  ",ABC.class_var)

    def show(self):
        print("harshita")


obj1=ABC(10) # here the constructor will be called along with object
obj2=ABC(20)
obj3=ABC(30)

obj1.show()