from tkinter import *


def register():
    root2 = Toplevel(root)
    root2.config(bg="black")
    root2.title("Register")
    root2.geometry("350x330")

    # Set text variables
    username = StringVar()
    password = StringVar()

    # Set label for user's instruction
    lbl = Label(root2, text="Please enter details below", font=("verdana", 18), bg="black", fg="blue")
    lbl.pack(pady=16)


    # Set username label
    username_lable = Label(root2, text="Username * ", font=("verdana", 16), fg="white", bg="black")
    username_lable.pack()

    # Set username entry

    username_entry = Entry(root2, textvariable=username, font=("verdana", 13))
    username_entry.pack(pady=13)

    # Set password label
    password_lable = Label(root2, text="Password * ", font=("verdana", 16), fg="white", bg="black")
    password_lable.pack(pady=8)

    # Set password entry
    password_entry = Entry(root2, textvariable=password, show='*', font=("verdana", 13))
    password_entry.pack(pady=8)

    # Set register button
    btn = Button(root2, text="Register", width=10, font=("verdana", 14), bg="grey", fg="yellow")
    btn.pack(pady=34)


root = Tk()

root.title("LOGIN PAGE")
root.geometry("350x370")
root.config(bg="black")

label = Label(root, text="Select your choice", fg="blue", bg="black", font=("verdana", 21)).pack(pady=20)
btn1 = Button(root, text="Login", fg="yellow", bg="grey", width=15, font=("verdana", 16)).pack(pady=36)
btn2 = Button(root, text="Register", fg="yellow", bg="grey", width=15, font=("verdana", 16), command=register).pack(pady=25)

root.mainloop()
