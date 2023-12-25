# for loop : used to repeat set of statements desired no of times based on
# a condition.also known as determinate or definite loop

#  for <control variable> in sequence:
#      statement block 

#   line     i    j=1 to i+1
#     1      1    1
#     2      2    1 2
#     3      3    1 2 3
#     4      4    1 2 3 4
#     5      5    1 2 3 4 5

for i in range(1,6):
       for j in range(1,i+1):   
              print(j,end=" ")
       print(end="\n")
