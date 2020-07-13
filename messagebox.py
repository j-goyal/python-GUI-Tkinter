from tkinter import *
from tkinter import messagebox


def error():
    messagebox.showerror("error", "Error on this button")


def info():
    messagebox.showinfo("info", "You are very smart")


root = Tk()

root.config(bg="black")

button1 = Button(root, text="Error", command=error)
button1.pack(fill=X, padx=10, pady=5)
button1 = Button(root, text="Info", command=info)
button1.pack(fill=X, padx=10, pady=10)

root.mainloop()
