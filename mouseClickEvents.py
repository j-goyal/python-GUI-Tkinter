from tkinter import *


def leftclick(event):
    print("Left")


def rightclick(event):
    print("Right")


root = Tk()

frame = Frame(root, width=320, height=150)
frame.bind("<Button-1>", leftclick)      # <Button-1> for left click of mouse
frame.bind("<Button-3>", rightclick)     # <Button-2> for middle click of mouse
frame.pack()                             # <Button-3> for right click of mouse

root.mainloop()
