from tkinter import *

root = Tk()
root.title("Basic")

theLabel = Label(root, text="Hello there", bg="blue", fg="white")
theLabel.pack()         # without pack, data is not visible

theLabel2 = Label(root, text="Hi everybody", bg="red", fg="white")
theLabel2.pack(fill=X)  # fill the text in X direction on adjusting size of window

theLabel3 = Label(root, text="Whats Up!", bg="green", fg="white")
theLabel3.pack(side=LEFT, fill=Y)

root.mainloop()  # used for constantly displaying windows on screen
