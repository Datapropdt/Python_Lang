# dictionary contains key value pairs

d1={"item":"choco","price":100,"qty":5,"mdate":"5 mar 22"}
print(d1)
d={}
print(d)
print(d1["item"]) # print the vlaue of item key
print(d1["qty"])
d1["edate"]="5 mar 24" # adding new key value pair
print(d1)
del d1["qty"] # deleting the qty pair
print(d1)
d1.pop("price") # deleting the last key value pair
print(d1)

print(sorted(d1.keys())) # sorting the key value pair
for val in d1.values(): # printing all values
    print(val,end=" ")

for key,val in d1.items(): # printing all key values pairs
    print(key,val,end=" ")
    
#d1.clear  clears all elements of d1
# del d1 deletes entire d1 from memory
