# program to demonstrate multiple inheritance
# super is the keyword used to get all the classes derived

class base1(object):  # first base class
    def __init__(self):
        super(base1,self).__init__()
        print("base1 class")

class base2(object):  # second base class
    def __init__(self):
        super(base2,self).__init__()
        print("base2 class")

class derived(base1,base2): # derived class derived from base1,base2
    def __init__(self):
        super(derived,self).__init__()
        print("DERIVED class")

d=derived()   