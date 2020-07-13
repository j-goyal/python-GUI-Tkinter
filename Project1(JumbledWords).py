from tkinter import *
import random
from tkinter import messagebox

# pady or padxm is used for spacing between 2 widgets
# ipadx, ipady for internal padding(like in entry widget)

words = ["nptoyh", 'avja', 'twisf', 'diani', 'cdanaa', 'nehimac', 'phees', 'hopne',
         'yubr', 'anir', 'nhica', 'rhaic', 'dlhei', 'mircaea', 'eeslp', 'belitutgh',
         'buce', 'emony', 'pytma', 'koobeton', 'tolapp', 'ssraui',
         ]

answers = ['python', 'java', 'swift', 'india', 'canada', 'machine', 'sheep', 'phone',
          'ruby', 'iran', 'china', 'chair', 'delhi', 'america', 'sleep', 'tubelight',
           'cube', 'money', 'paytm', 'notebook', 'laptop', 'russia',
           ]

num = random.randrange(0, 22, 1)
score = 0
# wrong = 0

def default():
    global words, answers, num
    lbl.config(text=words[num])


def check():
    global words, score, wrong, answers, num
    var = entry.get()                     # get the word from entry widget

    if var == answers[num]:
        score = score + 1
        scorelbl.config(text="Current Score : " + str(score))
        messagebox.showinfo("Success", "Hurrrey ! Right answer")
        reset()

    elif len(var) == 0:
        messagebox.showwarning("NULL", "Please enter something")

    else:
        messagebox.showerror("Error", "Oooops ! Wrong answer")
        entry.delete(0, END)       # automatically delete the wrong word so that we can re enter


def reset():
    global words, answers, num
    num = random.randrange(0, 22, 1)
    lbl.config(text=words[num])
    entry.delete(0, END)


root = Tk()

root.title("Game")
root.geometry("400x400+250+150")
root.configure(background="black")
root.resizable(0,0)

scorelbl = Label(root, text="Current Score : 0", font=("comic sans ms", 17), fg="yellow", bg="black")
scorelbl.pack()

lbl = Label(root, text="Your here", font=("verdana", 18),  bg="black", fg="white")
lbl.pack(pady=20)

entry = Entry(root, font=("verdana", 16), bd=6, bg="powder blue",  justify=CENTER)
entry.pack(ipady=5, ipadx=5)

btncheck = Button(root, text="Check", font=("comic sans ms", 16), width=14,  bg="grey", relief=GROOVE, command=check)
btncheck.pack(pady=35)

btnreset = Button(root, text="Reset", font=("comic sans ms", 16), width=14, bg="grey", relief=GROOVE, command=reset)
btnreset.pack()

default()

root.mainloop()
