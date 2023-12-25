# __getitem__() : is used to indexing it can be declared as
# __getitem__(self,index)
# __setitem__(): is used to assign an item to indexed values.
#it can be declared
# as __setitem__(self,index,val)

# myList is built in one, we must use like that only

class numbers:
    def __init__(self,myList): # by using init we can initialize
        #the members
        self.myList = myList   # of class which nothing but
        #constructor
    def __getitem__(self,index):
        return self.myList[index]
    def __setitem__(self,index,val):
        self.myList[index]=val

numlist = numbers([1,2,3,4,5,6,7,8,9])
print(numlist[5]) # prints 5 index value of list
numlist[3]=10    # 10 will be assigned to 3 rd index element of list
print(numlist.myList)
