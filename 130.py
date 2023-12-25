# program to compare two date objects 

class Date:
    def __init__(self):
        d = m= y =0
    def get(self):
        self.d = int(input(" enter the day : "))
        self.m = int(input(" enter the month : "))
        self.y = int(input(" enter the year : "))
    def __eq__(self, D): # == overloading
        Flag = False
        if self.d == D.d:
            if self.m == D.m:
                if self.y == D.y:
                     Flag = True
        return Flag
    def __lt__(self, D):   # < overloading here it is lt not it 
        Flag = False
        if self.d < D.d:
            if self.m < D.m:
                if self.y < D.y:
                     Flag = True
        return Flag

D1 = Date()
D1.get()
D2 = Date()
D2.get()
print("D1 == D2", D1==D2)
print("D1 < D2", D1<D2)

                    
                     
