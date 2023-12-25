# class is a collection of objects
# object is instance of a class
#__init__() method is to define the class constructor
# __del__() method is used to destroy objects will be activated when objects
# destroyed 

class ABC:
    class_var = 0
    def __init__(self,var):
        ABC.class_var+=1
        self.var=var
        print(" the object value is:", var)
        print(" the value of class variable is :  ",ABC.class_var)

    def __del__(self): # for deleting the objects created
        ABC.class_var -= 1
        print("object with value %d is going out of scope"%self.var)
    
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)

del obj1
del obj2
del obj3
    
       
       
