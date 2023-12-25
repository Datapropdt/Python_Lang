#program to read the nos until -1 and count negatives, positives and zeros

nn=p=z=0
print("enter -1 to exit ")

while(1):
    n=int(input("enter a number, -1 to exit"))
    if (n==-1):
        break
    if (n==0):
        z=z+1
    elif (n>0):
        p=p+1
    else:
        nn=nn+1
        
print("no of zeros =",z)
print("no of postives =",p)
print("no of negatives =",nn)

