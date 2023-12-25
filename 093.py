#generator: is a function that produces or yields a sequence of values using
#yield

def square():
    number=2
    while True:
        yield number
        number*=number  
sq=square()
#print(next(sq))
#print(next(sq))
#print(next(sq))
#print(next(sq))
#print(next(sq))
#print(next(sq))

for i in range(1,5):
    print(next(sq),end=" ")

