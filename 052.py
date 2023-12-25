# keyword arguments: the arguments mentioned along with function without any
# values are called keyword arguments, these should be completely given
# when called.

def display(str,intx,floaty): 
    print("string is ",str)
    print("intx is ",intx)
    print("floaty is ",floaty)

print(" the execution starts from here ")

display(floaty=345.55,intx=123,str="madhuri") # formal parameters
display("sowmya",342,5.66) # actual parameters
print(" the execution ends here ")

    
#display("sowmya",342) gives an error because of less no of arguments
