from tkinter import *
root = Tk()
a = 1
b = 100
attempts = 0
number = 1
states = []
text1 = f'Choose a number from {a} to {b}...'
text2 = '''If I guess, write "=",
            if your number is less, then enter "<",
            if bigger, enter ">".
            and press "Enter".'''
text3 = 'Victory'
def equal():
    lbl1.destroy()
    lbl2.destroy()
    lbl5.destroy()
    btn2.destroy()
    btn3.destroy()
    btn4.destroy()
    lbl3.pack()
    lbl4 = Label(root, text=f'Attempts: {attempts}')
    lbl4.pack()
    btn5.pack()
def bigger():
    global a
    a = number + 1
    start()
def lower():
    global b
    b = number - 1
    start()
def start():
    global attempts
    global number
    global states
    global lbl5
    btn.destroy()
    lbl1.pack()
    lbl2.pack()
    if 1 in states:
        lbl5.destroy()
    states.append(1)
    attempts += 1
    number = (a + b) // 2
    text5 = f'Is it {number}? '
    lbl5 = Label(root, text=text5)
    btn2.pack()
    btn3.pack()
    btn4.pack()
    lbl5.pack()
lbl1 = Label(root, text=text1)
lbl2 = Label(root, text=text2)
lbl3 = Label(root, text=text3)
lbl5 = Label(root, text='')
btn = Button(root, text='Start', command=start)
btn2 = Button(root, text='Yes', command=equal)
btn3 = Button(root, text='>', command=bigger)
btn4 = Button(root, text='<', command=lower)
btn5 = Button(root, text='Exit', command=root.destroy)
btn.pack()
root.mainloop()