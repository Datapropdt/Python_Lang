# global variables : variables declared in the main program and can be accessed
# any where in the program either in main or in any function, scope and life throguht
# the main as well as function
# local variables : variables declared with in a function and can be accessed
# with in the function but not outside the function, scope and life upto function

num1=10
print("global variable num1 = ",num1)

def func(num2):
    print("in function - local varibale num2 = ",num2)
    num3=30
    print("in function - local varibale num3 = ",num3)
    print("in function - global varibale num1 = ",num1)

    
func(20)
print("num1 again  = ",num1)


#print("num3 out of function  = ",num3) # cannot be accessible outside the function
#print("num2 out of function  = ",num2)   
