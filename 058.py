#lambda or anonymous functions: will not use def keyword, will be created
#using lambda keyword, these are throw away functions.
#contain only a single line. syntax
#lambda arguments:expression
#program to add 2 numbers

print("test ")

def small(a,b):
    if (a<b):
        return a
    else:
        return b

sum = lambda x,y:x+y
diff = lambda x,y:x-y

print(sum(-3,-2))
print(diff(-1,5))

print(" smaller of 2 nos  = ",small(sum(-3,-2),diff(-1,5)))

print(sum ( sum(4,5), sum(5,6) ) ) #nested sum


