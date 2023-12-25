# operator overloading + applying + - * / to objects
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

s1= student("rakhil",[87,90,85])
s2= student("akhil",[83,86,66])
s1.display()
s2.display()
s3=student("",[])
s3=s1+s2 # + operator overloading
s3.display()

