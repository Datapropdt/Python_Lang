# exception is an error if it is findout by computer gives error
# but it can be handled which is exception handling

 #exception handling

try:
    #import ramesh
    n = int(input("enter numerator "))
    d = int(input("enter denominator "))
    q = n/d
    print(" quotient = ",q)

except (ValueError):
    print("it must be a number ")
except ZeroDivisionError:
    print(" denominator cant be zero ")
except ImportError:
    print("cant import")
else:
    print("unknown exeption")
    

