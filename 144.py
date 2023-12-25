# recursion : when function calls itself is called recurstion
# generally a function will be used after complete definition
# program to find the factorial of a number using recurstion

def fon(n): # fon - factorial of a number 
    if n==1:
        return 1
    else:
        return n*fon(n-1) # in this function definition we are calling the
                        
n=int(input(" enter  a number "))

print("factorial of "+str(n)+"  =  ",fon(n))


  # function as a part of body of function which
                          # is recursion
                          # 5 *fon(4)
                          # 5 * 4 * fon(3)
                          # 5 * 4 * 3 * fon(2)
                          # 5 * 4 * 3 * 2 * fon(1)
                          # 5 * 4 * 3 * 2 * 1
