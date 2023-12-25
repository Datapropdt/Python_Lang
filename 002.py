# to get the input at runtime to the variables use input() method
# the content that will be taken using input method is always a string
# it should be converted to number using int()

a=input("enter a number ")
b=input("enter another number ")
print(" sum of ab in string format ",a+b)
print(a,b)
c=int(a)+int(b)  # after converting into integer
print(c)
d=45 # directly assigning the value hence conversion not required
e=56
print(d+e)
