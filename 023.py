#program to print armstrong nos from 1 to 1000
# if the sum of the cubes of the digits is equal to original number then Arm

n=1
print("\n the armstrong numbers from 1-1000 are : ")

while(n<=1000):
    
    sum=0 
    number=n  # very important

    while(n>0):
        r=n%10  # % reminder division
        sum=sum+(r*r*r)
        n=n//10  # // quotient division

    if (sum==number):
        print(number)

    n=number+1   # it must not n=n+1

# 153%10 3      153/10  15
#  15%10 5      15/10    1
#   1%10 1      1/10     0

   
