# for loop : used to repeat set of statements desired no of times based on
# a condition.also known as determinate or definite loop

#  for <control variable> in sequence:
#      statement block


n = int(input("enter a number "))
s = 0.0

for i in range(1,n+1):
       a = 1.0/i
       s = s+a

print("the sum of 1 + 1/2+1/3+....1/"+str(n)+" is "+str(s))
