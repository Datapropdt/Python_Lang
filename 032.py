# for loop : used to repeat set of statements desired no of times based on
# a condition.also known as determinate or definite loop

#  for <control variable> in sequence:
#      statement block 

#   line     i    j=1 to i+1
#     1      1    1
#     2      2    2 3
#     3      3    4 5 6
#     4      4    7 8 9 10
#     5      5    11 12 13 14 15

k=1
for i in range(1,6):
       for j in range(1,i+1):
              print(k,end=" ")
              k+=1 # short hand operator
       print(end="\n")
