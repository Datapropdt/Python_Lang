#program to find the big, small of of any given nos 
sum=0
i=1
m=int(input("how many nos  :  "))

n=int(input("enter  number  :  "))

sum =sum+n
big=small=n

i=2

while(i<=m):
    n=int(input("enter  number  :  "))
    if (big<n):
        big=n
    if (small>n):
        small=n

    sum=sum+n    
    i=i+1

print("sum = ",sum)
print("big =  ",big)
print("small = ",small)
