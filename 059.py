#to use lambda function with an ordinary function

def increment(y):
   return( lambda x:x+1) (y)

a=100
print("a = ",a)
print(" a increment is = ")
b=increment(a)
print(b)
print(" a increment is = ",increment(b))
c=a+increment(b)
print(c)

print(increment(100)) 
