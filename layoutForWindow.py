from tkinter import *

root = Tk()
root.geometry("300x300")

topframe = Frame(root)     # create an invisible frame on top and bottom
topframe.pack()            # no need to mention side for TOP frame

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

button1 = Button(topframe, text="BUTTON 1", bg="yellow", fg="red")
button2 = Button(topframe, text="BUTTON 2", bg="yellow", fg="green")
button5 = Button(topframe, text="BUTTON 5", bg="yellow", fg="blue")
button3 = Button(bottomframe, text="BUTTON 3", bg="white", fg="purple")
button4 = Button(bottomframe, text="BUTTON 4", bg="white", fg="yellow")
button6 = Button(bottomframe, text="BUTTON 6", bg="white", fg="black")

button1.pack()     # order of packing is important and have effect on layout
button2.pack(side=LEFT)
button3.pack()
button4.pack(side=RIGHT)
button5.pack()
button6.pack()

root.mainloop()
