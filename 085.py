#   0123456789 1011 12 13 
# s=ramesh cha n  d  r a
#

s="ramesh chandra"
print(s)
print(s[:2]) # upto 1 only
print(s[2:]) # 2 to end
print(s[2:10]) # start from 2 till 9
print(s[2:10:2])# starts from 2 and skips every alternate letter upt 9
print(s[::3]) #start from first one and index%3==0 th characters
print(s[:-1]) # all but no last letter
print(s[::-1])# reverse string word by word
print(s[::-2])# alternate letters in reverse of string
      
