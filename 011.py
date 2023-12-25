# nested if : if an if condition contains futher ifs either in true/false part

a = int(input("enter a  "))
b = int(input("enter b "))
c = int(input("enter c "))

if (a>b):
    if (a>c):
        big=a
    else:
         big=c
else:
    if (b>c):
        big=b
    else:
         big=c
print(" big = ",big)
