# for loop : used to repeat set of statements desired no of times based on
# a condition.also known as determinate or definite loop
#  i 1 to i
#  1 1
#  2 1 2
#  3 1 2 3
#  4 1 2 3 4
#  5 1 2 3 4 5

#  for <control variable> in sequence:
#      statement block

k=1
for i in range(1,6):
	for j in range(1,i+1):
	  print(k,end =" ")
	  k=k+1
	  if (k==10):
	   break
	print("\n")
 	