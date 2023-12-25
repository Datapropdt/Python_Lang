#generator: is a function that produces or yields a sequence of values using
#yield

def square():
    number=2
    while True:
        yield number
        number*=number # a*=5 -> a = a*5 short hand operator
sq=square()
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))



