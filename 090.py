# exception is an error if caught by compiler gives an error, not to be
# treated as an error it must be caught and handled which is called exception
# handling
# predefined exception
# user defined exception

import sys

list=[1,2,3,4,5,6,7,8,9,10]
it=iter(list)

while True:
   try:        # try to catch the exception if occured
       print(next(it),end=" ")
   except StopIteration:   # handling the exception
       print("\n all elements over, no more ")
       sys.exit()

