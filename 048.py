# prime numbers using function

def prime(n):
    fc=0 # factor count 
    for i in range(1,n+1):
        if (n%i==0):
            fc+=1
    
    if (fc==2):
        print(n,end=" ")
    

for j in range(1,70):
    prime(j)
