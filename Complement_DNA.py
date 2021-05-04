from tkinter import *
root = Tk()
root.geometry('700x150')
def DNA():
	a = e.get()
	x = 't'
	y = 'c'
	z = 'g'
	r = 'a'
	a = a.replace('A',x)
	a = a.replace('G',y)
	a = a.replace('C',z)
	a = a.replace('U',r)
	a = a.replace('T',r)
	d = a.upper()
	b = d[::-1]
	with open('Complement DNA.txt', 'w') as f:
		f.write(b)
	newwin = Toplevel(root)
	lbl = Label(newwin, text='Done')
	lbl.pack()
e = Entry(root, width=45, font='Times 20')
e.place(x=30,y=20)
btn = Button(root, text='Find', font='Times 20', command=DNA)
btn.place(x=330,y=80)
root.mainloop()