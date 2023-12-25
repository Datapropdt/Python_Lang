# dictionary : key:value pair elements enclosed in curly braces is dictionary
# the items can be mutable(can be modified)

d1={"item":"choco","price":100}

print("item name : ",d1["item"])
print("item cost : ",d1["price"])

print(d1)

d1["item"]="rice"
print(d1.keys())
print(d1.values())
