from tkinter import *

class JatinButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.print_button = Button(frame, text="Button", command=self.printmessage)
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="quit", command=frame.quit)
        self.quit_button.pack()

    def printmessage(self):
        print("This is nice!")


root = Tk()

obj = JatinButtons(root)

root.mainloop()
