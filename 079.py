# program to convert lower case text to upper case
# ascii(american standard code for information interchange
# code of A is 65 small a is 97 diff is 32

Str1=input("Enter the string to be converted uppercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")
