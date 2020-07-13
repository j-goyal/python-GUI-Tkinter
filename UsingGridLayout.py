# Grid is like excel worksheet with rows and columns

from tkinter import *

root = Tk()

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)
# entry3 = Entry(root)

label1.grid(row=0, sticky=E)          # column is 0 by default
label2.grid(row=1, sticky=E)          # sticky aligns the text W,N,E,S directions

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
# entry3.grid(row=1, column=2)

c = Checkbutton(root, text="keep me logged in")
c.grid(columnspan=2)               # columnspan merges n cells and place it in CENTER

root.mainloop()
