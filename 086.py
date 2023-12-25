# iterators and generators 
# iterator is an object which allows a programmer to traverse through all the
# elements of a sequence. iterator implements 2 methods 1.iter(),2.__next__()
# by using iter() and next() we can move along a list

#program that uses iter() to traverse thru the elements of list

list=[1,2,3,4]
l1="sastry"

it =iter(list)
it1=iter(l1)

print(it.__next__()) # 1
print(it.__next__()) # 2
print(it.__next__()) # 3
print(it.__next__()) # 4


print(it1.__next__())
print(it1.__next__())
print(it1.__next__())
print(it1.__next__())
print(it1.__next__())
print(it1.__next__())
