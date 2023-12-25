# multi threading
import _thread
import time
# define a function for the thread
def display_time(threadName, delay):
    count = 1
    while count < 5:
        time.sleep(2)
        count +=1
        print(threadName, time.ctime(time.time()))
        print("%s: %s" %(threadName, time.ctime(time.time())))
# create two threads as follows
try:
    _thread.start_new_thread(display_time,("one",1))
    _thread.start_new_thread(display_time,("two",2))
except:
    print("error: unable to start thread")
