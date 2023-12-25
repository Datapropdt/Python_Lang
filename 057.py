#lambda or anonymous functions: will not use def keyword, will be created
#using lambda keyword, these are throw away functions.
#contain only a single line. syntax
#lambda arguments:expression
#program to add 2 numbers

sum = lambda x,y:x+y
pro = lambda x,y:x*y

print(" sum = ",sum(13,15))
print(" product = ",pro(3,5))
