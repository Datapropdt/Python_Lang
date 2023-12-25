try:
    print("dividing strings ")
    try:
        quo ="abc"/"def"
    finally:
       print("in finally block ")
        
except TypeError:
    print("in except block .... handling type error...")
 
