# global keyword: can be used to make a local variable of a function as global

z=100 # global must not be used here

def show():
    global var1 # var1 is local but because of global keyword it became global
    a=10 # is local only
    var1="morning"
    print("in function - var is = ",var)
    print("in function - z is = ",z)
    
var ="good"
show()
print("var is ",var)
print("outside function - var1 is = ",var1) #var1 is local variable
print("in main - z is = ",z)

#print("a is",a) a can't be accessed as it is declared without global
      

    
