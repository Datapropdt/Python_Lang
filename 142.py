
#Assertions in python: is a basic check that can be turned on or off when
# program is being tested. uses assert keyword. when encountered  if the
# expression is false an AssertionError raised.
# assert expression[, arguments]
# assert <expression>, <message>

c = int(input("enter the temperature in celcius : "))
f = (c*9/5)+32
print(" f temp = ",f)

assert(f<=32),"its freezing"x
print("Temperature in Fahreinheit = ",f)
