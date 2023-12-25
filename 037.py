# for loop : used to repeat set of statements desired no of times based on
# a condition.also known as determinate or definite loop
#  i j=1 to i
#  1 1
#  2 2 2
#  3 3 3 3
#  4 4 4 4 4
#  5 5 5 5 5 5

#  for <control variable> in sequence:
#      statement block


for i in range(1,6):
       for j in range(1,i):
              print(j,end =" ")
       print("\n")

