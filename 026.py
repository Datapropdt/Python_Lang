#  program to convert binary to decimal 
bn=int(input("enter a binary number "))
dn=0
i=0
gn=bn
while(bn!=0):
       r=bn%10   # r-remainder
       dn=dn+r*(2**i)
       bn=bn//10
       i = i+1
       
print("the decimal equailvalent of ",gn,"= ",dn)



# 101 bn    10            0        1
#           25)10    = 5*10  + 2* 10 = 5+20 = 25
#          0    1     2
# 101)2  1*2 +0*2 + 1*2  =5 

#              0     1
# 35 )10 = 5*10 + 3*10   = 35
