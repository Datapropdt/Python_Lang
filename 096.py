#program to create a genenrator that reverses a string

def rev(mes):
    l=len(mes)
    for i in range(l - 1,-1,-1):
        yield mes[i]

mes = "hello"
for char in rev(mes):
    print(char, end=" ")      
