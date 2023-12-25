# list operations. list are mutable. items enclosed in []
# we can add or remove elements in a list
l1 = ['a','bc',78,1.23]
l2 = ['d',78]

print(l1)   
print(l2)  
print(l1[0]) #prints first element of list
print(l1[1:3])# prints elements starting from 2 till 3
print(l1[2:])#prints elements from 2 to last
print(l1[-1]) #prints list element
print(l1*2)#prints l1 2 times
print(l1+l2)#combines 1l,l2
l1[0]='z' #o th element of l1 is assigned Z
l2[0]='y'
print(l1) 

l1[1]= "Datapro"
l1.append(" sastry")
l1.append("sandya")

print(l1) 
#l2.remove('y')

print(l1)   #prints l1 contents
print(l2) # prints l2 contents







