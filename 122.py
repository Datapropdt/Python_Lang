#here there is no init methd in derived class, the init method of first base
# class is gets called. since there is no call to super() function in the
# init method of base1 class, no further init() method is invoked. it can
# be rectified in 83

class base1(object):
    def __init__(self):
        print("base1 class")

class base2(object):
    def __init__(self):
        print("base2 class")

class derived(base1,base2):
    pass

d = derived()

