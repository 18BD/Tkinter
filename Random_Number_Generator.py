import random
from tkinter import *
root = Tk()
root.geometry('400x250')
root.resizable(width=True, height=True)
label = Label(root, text='')
newwin = Label(root, text='')
check = []
def add():
    check.append(1)
def generate_random_number():
    global label
    global newwin
    state = []  
    label.destroy()
    newwin.destroy()
    a = int(entry1.get())
    b  = int(entry2.get())
    c = int(entry3.get())
    for i in range(a,b):
        state.append(i+1)
    r = random.choices(state, k=c)
    newwin = Toplevel(root)
    label = Label(newwin, text=r, font='arial 20')
    label.pack()
    if 1 in check:
        with open('Numbers.txt', 'w') as f:
            f.write(str(r).strip('[]'))
label1 = Label(root, text='Range', font='arial 20')
label2 = Label(root, text='~', font='arial 20')
label3 = Label(root, text='Quantity', font='arial 20')
entry1 = Entry(root, width=15)
entry2 = Entry(root, width=15)
entry3 = Entry(root, width=11)
checkbutton = Checkbutton(root, text='Save in txt', font='arial 12', command=add)
btn = Button(root, text='Generate random number', font='arial 15', command=generate_random_number)
label1.place(x=20,y=30)
label2.place(x=230,y=30)
label3.place(x=20,y=100)
entry1.place(x=120,y=42)
entry2.place(x=270,y=42)
entry3.place(x=142,y=112)
checkbutton.place(x=250,y=108)
btn.place(x=83,y=175)
root.mainloop()