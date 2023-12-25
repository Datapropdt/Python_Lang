# the problem of 82 is rectified here

class base1(object):
    def __init__(self):
        print("base1 class")
        super(base1,self).__init__() # not there in 82 because of this the init
                                     # method of base2 class is invoked

class base2(object):
    def __init__(self):
        print("base2 class")
        
class derived(base1,base2):
    pass

d = derived()
