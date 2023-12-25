# operator overloading + applying + - * / to objects
# normally arithmetic operators are meant for arithmetic operations over
# int,float data types. if we can extend the use of these operators to objects
# also, then the operators are said to be overloaded. and the phenomena is
# called operator overloading

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,self.marks)
    def __add__(self,s):
        temp=student(s.name,[])
        for i in range(len(self.marks)):
            temp.marks.append(self.marks[i]+s.marks[i])
        return temp

s1= student("nikhil",[87,90,85])
s2= student("nikhil",[83,86,66])
s1.display()
s2.display()
s3=student("",[])
s3=s1+s2 # + operator overloading
s3.display()

