#program to read a number and find armstrong or not
# if the sum of the cubes of the digits is equal to original number then Arm

n=int(input("enter a number "))
sum=0
number=n  # very important
while(n>0):
    r=n%10  # % reminder division
    sum=sum+(r*r*r)
    n=n//10  # // quotient division
if (sum==number):
    print("the number ",number," is armstrong")
else:
    print("the number ",number," is not armstrong")

# 153%10 3      153/10  15      10)1(0
#  15%10 5      15/10    1         0
#   1%10 1      1/10     0          1

   
