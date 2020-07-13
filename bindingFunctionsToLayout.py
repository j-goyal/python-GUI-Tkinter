from tkinter import *

root = Tk()
# 1st Method
"""
def printname():
    print("Hello my name is Jatin")

# DO NOT PUT BRACKETS AFTER FUNCTION NAME
button1 = Button(root, text="My name", command=printname) 
button1.pack()
"""

# 2nd Method
"""
def printname(event):
    print("Hello my name is Jatin")


button1 = Button(root, text="My name")
button1.bind("<Button-1>", printname)    # <Button-1> symbolizes left click 
button1.pack()
"""

root.mainloop()
