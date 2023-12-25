# writting the contents on to disk file 
file=open("test2.txt","w")
lines=["greeshma","\nharshita","\nbhargavi","\npriyanka"]
file.writelines(lines)
file.close()
