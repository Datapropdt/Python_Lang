#variable length arguments: will save the memory 

def func(name,*favsubs):
    print("\n",name,"likes 2 read")
    for sub in favsubs:
        print(sub)
        
func("raj","maths","math s engg")
func("ritche","c","ds","daa")
func("krish")
func("1","2","3","4","5","6")
