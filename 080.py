# program to convert lower case text to upper and upper to lower

Str1=input("Enter the string to be converted uppercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i]) # The ord () function returns the number representing
                  #the unicode code of a specified character.
   if x>=97 and x<=122:  # 97 is the ascii code for 'a', 65 is for 'A' diff 32
       x = x-32
   elif x>=65 and x<=91:  # 97 is the ascii code for 'a' , 65 is for 'A' diff 32
       x = x+32
       
   y=chr(x) # Convert given no back to character with the chr () function. 
   print(y,end="")
