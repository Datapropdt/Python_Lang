try:
    print("raising exception ")
    raise (ValueError)
   
except:
    print("exception caught ... value error line : 6")
    #raise (ZeroDivisionError)
finally:
    print("clean up")


print("last line ")