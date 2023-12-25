# return statement : returns a value to the place where we used it

def cube(x):
    print("hai")
    return (x*x*x)
    print("hai") # statements given after return will not be considered

num=10
result=cube(num)  # calling the function using variable
print("cube of ",num,"=",result)
print("cube of 3 = ",cube(3)) # calling the function using value

value=120+2*cube(4)# using the function in expression

print(value)
    
