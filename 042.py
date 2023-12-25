# prime number program
fc=0
n=int(input("enter a number  "))

for i in range(1,n+1):
    if (n%i==0): fc+=1
    
if (fc==2):
    print("n is prime ")
else:
    print("n is not prime ")
    
