# writting the contents on to disk file 
file=open("test2.txt","a")
lines=["greeshma1","harshita2","3gopika","priyanka4","5kumar"]
file.writelines(lines)
file.close()
