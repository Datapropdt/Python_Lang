# default arguments: the values supplied to the arguments at the time of define

def display(str="hai",intx=10,floaty=5.5):
    #default values
    print("string is ",str)
    print("intx is ",intx)
    print("floaty is ",floaty)


display(floaty=345.55,intx=123,str="madhuri") #3 parameters passed
display("sowmya",342,234.44) #3 parameters passed
display() #no parameters passed
display("test") # only one parameter passed
display("test",400) # only 2 parameters passed


    
