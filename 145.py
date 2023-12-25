# generally a function will be used after complete definition
# program to find the factorial of a number without recurstion

def fon(n):
    fact=1
    for i in range(1,n+1):
        fact*=i # fact = fact * i
    return fact

n=int(input(" enter  a number "))

print("factorial of "+str(n)+"  =  ",fon(n))
