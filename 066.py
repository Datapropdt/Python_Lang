# command line arguments
# for this the input is to be given at the commandline as follows
# at the time of file save as copy the path
# goto cmd , then cd\ , then cd pastepath using ctrl v then press enter
# c:\...............\saspyprgs>python 44.py 5 9 3 2
#C:\Users\rajsekhar\AppData\Local\Programs\Python\Python36-32\saspypprgs

import sys

a=int(sys.argv[1])# the value must be given at the prompt in the command line 
b=int(sys.argv[2])# the value must be given at the prompt in the command line
c=int(sys.argv[3])# the value must be given at the prompt in the command line
d=float(sys.argv[4])# the value must be given at the prompt in the command line
print("You have entered values")
sum=a+b+c+d

print("sum = ",sum)
sys.exit(0)
print("hai")

# output

# C:\Users\rajsekhar\AppData\Local\Programs\Python\Python36-32\saspypprgs>python 44.py 1 2 3 4
# sum =  10.0
