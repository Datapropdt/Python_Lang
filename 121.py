# inheritance: derived class inherits all the capabilites of the base class
# and adds refines and extensions of its own.
# syntax class derivedclass(baseclass):
#              body of derived class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def disp(self):
        print(" NAME : ",self.name)
        print(" age  : ",self.age)

class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def disp(self):
        person.disp(self)
        print(" experience : ",self.exp)
        print(" research area : ",self.rarea)

class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def disp(self):
        person.disp(self)
        print(" course : ",self.course)
        print(" marks : ",self.marks)

print("************** Teacher **********")

t=teacher("sastry",55,26," programming ")
t.disp()
print("********** student ***********")
s=student("madhuri ",19,"mca",98)
s.disp()     