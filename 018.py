# program to read key press and reply letter,number or space

char = input("press anykey ")

if(char.isalpha()):
    print("u entered a character")

if(char.isdigit()):
    print("u entered a digit")

if(char.isspace()):
    print("u entered a space")

