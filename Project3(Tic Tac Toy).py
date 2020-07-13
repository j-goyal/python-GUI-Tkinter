import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Player 1')
root.resizable(0,0)
activeplayer=1
p1=[]
p2=[]

def btnclick(id):
    global activeplayer
    global p1,p2
    if activeplayer==1:
        root.title('Player 2')
        changelayout(id,'X','#00ff0d')
        p1.append(id)
        activeplayer=2
        #print("p1",p1)
    elif activeplayer==2:
        root.title('Player 1')
        changelayout(id,'O','red')
        p2.append(id)
        activeplayer=1
        #print("p2",p2)   
    checkwinner()



def changelayout(id, symbol,color):
    if id==1:
        btn1.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==2:
        btn2.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==3:
        btn3.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==4:
        btn4.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==5:
        btn5.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==6:
        btn6.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==7:
        btn7.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==8:
        btn8.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
    if id==9:
        btn9.config(text=symbol, padx=31, pady=29, state=DISABLED, disabledforeground=color)
        


def checkwinner():
    winner = -1
    if (1 in p1 and 2 in p1 and 3 in p1) or (4 in p1 and 5 in p1 and 6 in p1) or (7 in p1 and 8 in p1 and 9 in p1):
        winner = 1
    if (1 in p1 and 4 in p1 and 7 in p1) or (2 in p1 and 5 in p1 and 8 in p1) or (3 in p1 and 6 in p1 and 9 in p1):
        winner = 1
    if (1 in p1 and 5 in p1 and 9 in p1) or (3 in p1 and 5 in p1 and 7 in p1):
        winner = 1
    if (1 in p2 and 2 in p2 and 3 in p2) or (4 in p2 and 5 in p2 and 6 in p2) or (7 in p2 and 8 in p2 and 9 in p2):
        winner = 2
    if (1 in p2 and 4 in p2 and 7 in p2) or (2 in p2 and 5 in p2 and 8 in p2) or (3 in p2 and 6 in p2 and 9 in p2):
        winner = 2
    if (1 in p2 and 5 in p2 and 9 in p2) or (3 in p2 and 5 in p2 and 7 in p2):
        winner = 2
        
    i=0
    j=0
    if winner == 1:
        #i=i+1
        #string = str(i)+":"+str(j)
        #lbl.config(text=string)
        messagebox.showinfo(title='Hurreeey!', message='Player 1 Win')
    elif winner == 2:
        #j=j+1
        #string = str(i)+":"+str(j)
        #lbl.config(text=string)
        messagebox.showinfo(title='Hurreeey!', message='Player 2 Win')
    if len(p1) + len(p2) == 9:
        messagebox.showinfo(title='DRAW', message='Game Draw')
        


    
#lbl = Label(root, text='0:0', font=('verdana',12))
#lbl.grid(columnspan=3)
        
btn1 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(1))
btn1.grid(row=1, column=0)

btn2 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(2))
btn2.grid(row=1, column=1)

btn3 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(3))
btn3.grid(row=1, column=2)

btn4 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(6))
btn6.grid(row=2, column=2)

btn7 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(7))
btn7.grid(row=3, column=0)

btn8 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(8))
btn8.grid(row=3, column=1)

btn9 = Button(root, bd=3, padx=35, pady=30, bg='black', command= lambda: btnclick(9))
btn9.grid(row=3, column=2)


root.mainloop()
