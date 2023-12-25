#data structures
#list is special data type in python which is sequence of elements separated
#by commas enclosed  in []. lists are mutable

l1=[1,2,3,4,5] #list

print(l1)
print(l1[0])
print(l1[2:3])
print(l1[:2])
print(l1[2:])
l1[2]=100 # updating list elements
print(l1[2])
l1[2]=100
print(l1)
del l1[1]  # deleting an element
print(l1)
l2=l1  #assigning
print(l2)
l3=[10,20,[30,40],50] #nested list
print(l3)
print(l3[2][0])
print(l3[2][1])
print(len(l1)) #length of list 
print(l1*3)
print(l1+l2) #concatenation
