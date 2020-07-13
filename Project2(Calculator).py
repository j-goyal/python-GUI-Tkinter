from tkinter import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    text_input.set(expression)  # update the expression by using set method


def clear():
    global expression
    expression = ""
    text_input.set(expression)


def equal():
    try:
        global expression
        total = str(eval(expression))
        text_input.set(total)
        expression = ""

    except:
        text_input.set("Error")
        expression = ""


root = Tk()
root.title("SIMPLE CALCULATOR")
root.resizable(0, 0)

text_input = StringVar()  # means text input is of type string
entry = Entry(root, bg="#d98d8d", bd=19, font=("arial", 22, 'bold'), justify=RIGHT, textvariable=text_input)
entry.grid(columnspan=4)

btn7 = Button(root, text="7", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(7))
btn7.grid(row=1, column=0)

btn8 = Button(root, text="8", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(8))
btn8.grid(row=1, column=1)

btn9 = Button(root, text="9", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(9))
btn9.grid(row=1, column=2)

add = Button(root, text="+", padx=19, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
             command=lambda: press("+"))
add.grid(row=1, column=3)

# ***********************************************************************************************************

btn4 = Button(root, text="4", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(6))
btn6.grid(row=2, column=2)

sub = Button(root, text="-", padx=23, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
             command=lambda: press("-"))
sub.grid(row=2, column=3)

# **********************************************************************************************************

btn1 = Button(root, text="1", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(1))
btn1.grid(row=3, column=0)

btn2 = Button(root, text="2", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(2))
btn2.grid(row=3, column=1)

btn3 = Button(root, text="3", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(3))
btn3.grid(row=3, column=2)

mul = Button(root, text="*", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
             command=lambda: press("*"))
mul.grid(row=3, column=3)

# ***********************************************************************************************************

btn0 = Button(root, text="0", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
              command=lambda: press(0))
btn0.grid(row=4, column=0)

btnclear = Button(root, text="C", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
                  command=clear)
btnclear.grid(row=4, column=1)

btnequal = Button(root, text="=", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
                  command=equal)
btnequal.grid(row=4, column=2)

div = Button(root, text="/", padx=21, pady=15, bd=7, fg="black", bg="#d98d8d", font=("verdana", 16, 'bold'),
             command=lambda: press("/"))
div.grid(row=4, column=3)

root.mainloop()
