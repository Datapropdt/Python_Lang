#program to create a generator to print fibonacci numbers
# 0 1 1 2 3 5 8 13 if we add 1,2 numbers we will get third one
# 0+1  =1 1 +1 =2 1+2 =3 

def fb():
    a,b=0,1 # a=0 b=1
    while a<20:
        yield b
        a, b = b, a + b  # a = b, b= a+b

iter = fb()

for i in iter:
    print(i, end=" ")
