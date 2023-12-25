# program to convert decimal number to binary number
# 5 --> 101 25 --->11001

dn=int(input("enter a decimal number "))
bn=0 # bn binary number
i=0
gn=dn # gn given number

while(dn!=0):
       r=dn%2
       bn=bn+r*(10**i) # ** indicates power
       dn=dn//2
       i = i+1
print("the binary equailvalent of ",gn,"= ",bn)
       
# n      q   r     bn
# 5 5/2  2   1     1
# 2  2/2 1   0     1
# 1  1/2 0   1    101



2^7 2^         2^1 2^0
128 64 32 16 8 4 2 1  = 65
 0   1  0 0  0 0 0 1  =  65



65
32 - 1
16 - 0 
8 - 0
4 - 0
2 - 0
1 - 0
