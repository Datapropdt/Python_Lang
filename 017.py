#program to print the sum of nos from m to n
# vertical gap before each line is indentation
# horizontal gaps between lines is formatting

sum=0
m=int(input("enter start number  :  "))
n=int(input("enter end number  :  "))
while(m<=n):
    sum=sum+m   #55 = 45 + 10     
    m=m+1

print(sum)
