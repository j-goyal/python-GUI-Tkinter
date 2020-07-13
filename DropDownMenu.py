from tkinter import *
from tkinter import messagebox


def doNothing():
    messagebox.showinfo("Sorry", "Not yet functional")


root = Tk()

menubar = Menu(root)         # create a Menu
root.config(menu=menubar)    # without this menu is not displayed on window(like pack command)

fileMenu = Menu(menubar)                               # First element in menu
menubar.add_cascade(label="File", menu=fileMenu)       # add_cascade used for drop down menus

# adding sub names in our drop down menu for File
fileMenu.add_command(label="New Project...", command=doNothing)
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_command(label="open...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)


editMenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=editMenu)

# adding sub names in our drop down menu for Edit
editMenu.add_command(label="undo", command=doNothing)
editMenu.add_command(label="redo", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="cut", command=doNothing)
editMenu.add_command(label="copy", command=doNothing)
editMenu.add_command(label="paste", command=doNothing)

root.mainloop()
