try:
    print("raising exception ")
    raise (ValueError)
finally:
    print("clean up")
    
