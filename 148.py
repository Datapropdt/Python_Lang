# gui programming with tkinter package
#import tkinter
#print(tkinter.TkVersion)
# program to print text in window 

from tkinter import Tk, Message
root=Tk()
msg=Message(root, text='hai Kumar')
msg.config(font=('callibri',24,'bold'))
#root.attributes('-fullscreen', True)
msg.pack()
root.title("this is my first gui ")

root.mainloop()
