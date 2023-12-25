# adding two list and sort them and  print in reverse order

m=[6000,12345,8000,5000]
n=[13456,6000,9000,5000]
p=m+n

p = list(set(p)) # to remove duplicate elements

print(p)
p.sort() # to sort the list elements
print(p)
p.reverse() # to reverse a list
print(p)

z=[2,12,34,11,25]
z.sort()
print(z)

z.reverse()
print(z)
