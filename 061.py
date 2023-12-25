# import is the keyword used to import the built in modules of python
# import can be used in two ways
# 1. import <module name>
# 2. from  <modulename> import <method1>,<method2> 

import time
import sys
from datetime import date

print("\n python path = \n",sys.path)

today = date.today()
print("Today's date:", today)

print(time.time())
System_time = time.localtime(time.time())
print("Local current time :", System_time)
sys.exit(0)

#\Users\rajsekhar>path
#PATH=D:\oracle\bin;C:\Program Files\Java\jdk1.8.0_202\bin;C:\Users\rajsekhar\
# AppData\Local\Programs\Python\Python36-32\Scripts\;
#C:\Users\rajsekhar\AppData\Local\Programs\Python\Python36-32\;
#C:\Users\rajsekhar\AppData\Local\Microsoft\WindowsApps;
