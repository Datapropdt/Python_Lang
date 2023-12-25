d1={"item":"choco","price":100,"qty":5,"mdate":"5 mar 22"}
print(d1)
print(len(d1)) # gives length of d1
print(str(d1)) # prints string formats of d1
d2=d1.copy()  # d1 will be copied to d2
print(d2)
print(d1.items()) # d1 items will be printed
print(d1.keys()) # d1 keys will be printed
d1.update(d2) #d1 will be updated with d2
print(d1)
print("item" in d1) # returns true if d1 contains item 
print("item" not in d1) # returns false if d1 contains item
