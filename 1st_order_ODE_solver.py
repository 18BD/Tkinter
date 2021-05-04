from tkinter import *
from sympy import *
from math import *
import matplotlib.pyplot as plt
root = Tk()
root.title('1st order ODE Solver')
root.geometry('500x363')
root.configure(bg='#c5eff7')
state = []
state2 = []
x = 1
y = 1
a = 1
def check1():
	state.append(1)
def check2():
	state.append(2)
def check3():
	state.append(3)
def check4():
	state.append(4)
def check5():
	state.append(5)
def check6():
	state2.append(6)
def Euler():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		y1 = y + h*f(x,y)
		x0 = x + h
		y0 = y1
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(1)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='green', marker='o', label='Numerical')
	ax.grid()
	ax.legend()
	ax.set_title('Euler')
def Euler_Analytic():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		y1 = y + h*f(x,y)
		x0 = round(x + h,2)
		y0 = round(y1,2)
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(1)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='red', marker='x', label='Analytical')
	ax.legend()
def Improved_Euler():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		y1 = y + h/2*(f(x,y)+f(x+h,y+h*f(x,y)))
		x0 = x + h
		y0 = y1
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(2)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='red', marker='o', linestyle='dotted', label='Numerical')
	ax.grid()
	ax.legend()
	ax.set_title('Improved Euler')
def Improved_Euler_Analytical():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		y1 = y + h/2*(f(x,y)+f(x+h,y+h*f(x,y)))
		x0 = round(x + h,2)
		y0 = round(y1,2)
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(2)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='black', marker='x', linestyle='dotted', label='Analytical')
	ax.legend()
def Runge_Kutta2():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + h,y + k1*h)
		y1 = y + (k1/2+k2/2)*h
		x0 = x + h
		y0 = y1
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(3)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='orange', marker='o', linestyle=':', label='Numerical')
	ax.grid()
	ax.legend()
	ax.set_title('Runge Kutta II')
def Runge_Kutta2_Analytical():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + h,y + k1*h)
		y1 = y + (k1/2+k2/2)*h
		x0 = round(x + h,2)
		y0 = round(y1,2)
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(3)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='red', marker='x', linestyle=':', label='Analytical')
	ax.legend()
def Runge_Kutta3():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + (h/2),y + k1*h/2)
		k4 = f(x + h,y + k1*h) 
		k3 = f(x + h,y + k4*h)
		y1 = y + (h/6)*(k1 + 4*k2 + k3)
		x0 = x + h
		y0 = y1
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(4)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='blue', marker='o', linestyle='dashed', label='Numerical')
	ax.grid()	
	ax.legend()
	ax.set_title('Runge Kutta III')
def Runge_Kutta3_Analytical():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + (h/2),y + k1*h/2)
		k4 = f(x + h,y + k1*h) 
		k3 = f(x + h,y + k4*h)
		y1 = y + (h/6)*(k1 + 4*k2 + k3)
		x0 = round(x + h,2)
		y0 = round(y1,2)
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(4)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='red', marker='x', linestyle='dashed', label='Analytical')	
	ax.legend()
def Runge_Kutta4():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + (h/2),y + k1*h/2)
		k3 = f(x + (h/2),y + k2*h/2)
		k4 = f(x + h,y + k3*h) 
		y1 = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
		x0 = x0 + h
		y0 = y1
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(5)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='purple', marker='o', linestyle='dashdot', label='Numerical')
	ax.grid()
	ax.legend()
	ax.set_title('Runge Kutta IV')
def Runge_Kutta4_Analytical():
	global x
	global y
	def f(x,y):
		equation = Differential_Equation()
		return equation
	list_x = []
	list_y = []
	x0 = x_initial()
	y0 = y_initial()
	h = sequence()
	w = iteration()
	for i in range(w):
		y = y0
		x = x0
		k1 = f(x,y)
		k2 = f(x + (h/2),y + k1*h/2)
		k3 = f(x + (h/2),y + k2*h/2)
		k4 = f(x + h,y + k3*h) 
		y1 = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
		x0 = round(x0 + h,2)
		y0 = round(y1,2)
		list_x.append(x0)
		list_y.append(y0)
	b = len(state)
	c = state.index(5)+1
	ax = figure.add_subplot(a,b,c)
	ax.plot(list_x,list_y, color='red', marker='x', linestyle='dashdot', label='Analytical')
	ax.legend()
def graphs():
	if 1 in state:
		Euler()
		Euler_Analytic()
	if 2 in state:
		Improved_Euler()
		Improved_Euler_Analytical()
	if 3 in state:
		Runge_Kutta2()
		Runge_Kutta2_Analytical()
	if 4 in state:
		Runge_Kutta3()
		Runge_Kutta3_Analytical()
	if 5 in state:
		Runge_Kutta4()
		Runge_Kutta4_Analytical()
	if 6 in state2:
		x=Symbol('x')
		y=Symbol('y')
		r=entry1.get()
		p=plotting.plot3d(r)
	plt.show()
def Differential_Equation():
	eq=eval(entry1.get())
	Button7.destroy()
	return eq
def y_initial():
	yz=eval(entry2.get())
	if type(yz)==int:
		Button8.destroy()
		return yz
	else:
		show_error_window()
def x_initial():
	xz=eval(entry3.get())
	if type(xz)==int:
		Button9.destroy()
		return xz
	else:
		show_error_window()
def sequence(): 
	st=eval(entry4.get())
	Button10.destroy()
	return st
def iteration():
	nb=eval(entry5.get())
	if type(nb)==int:
		Button15.destroy()
		return nb
	else:
		show_error_window()
def show_error_window():
	new = Toplevel(root)
	new.title('!')
	new.configure(bg='#c5eff7')
	Label(new, text='Value Error (not integer)', bg='#c5eff7', fg='gray15').pack()
	Button(new, text='Ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=new.destroy).pack()
def reset():
	global state
	global state2
	state = []
	state2 = []
	delete()
	build()
def calculator_window():
    global button_list
    window = Tk()
    window.configure(bg='#c5eff7')
    def click(key):
        ln = log
        e = exp(1)
        global memory
        if key == '<-':
            label['text'] = label['text'][:-1]
        elif key == '±':
            try:
                result = -eval(label["text"])
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == 'x^2':
            try: 
                result = eval(label["text"])**2
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == '1/x':
            try:
                result = 1/eval(label["text"])
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == 'x!':
            try:
                result = factorial(eval(label["text"]))
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == '%':
            try:
                result = eval(label["text"])/100
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == 'MC':
            memory = ''
        elif key == 'MS':
            try:
                result = eval(label["text"])
                memory = str(result)
            except SyntaxError:
                show_error_window()
        elif key == 'Quit':
            window.destroy()
        elif key == 'MR':
            label['text'] += memory
        elif key == 'C':
            label['text'] = ''
        elif key == '√':
            try:
                result = eval(label["text"])
                label['text'] = str(sqrt(result))
            except SyntaxError:
                show_error_window()
        elif key == '=':
            try:
                cnt = 0
                for i in label['text']:
                    if i == '(':
                        cnt+=1
                    elif i == ')':
                        cnt -= 1
                if cnt > 0:
                    label['text'] += ')' * cnt
                result = eval(label["text"])
                result = round(result, 7)
                label['text'] = str(result)
            except SyntaxError:
                show_error_window()
        elif key == 'Ω':
            text = label['text']
            clear()
            place_buttons(text=text)
        else:
            label['text'] += key
    def show_error_window():
        new = Toplevel(window)
        Label(new, text='Invalid syntax').pack()
        Button(new, text='Ok', command=new.destroy).pack()
    def clear():
        elements = window.winfo_children()
        for l in elements:
            l.destroy()
    button_list1 = [
    'MC','MR','MS','(',')',
    '<-','C','±','√','Quit',
    '7','8','9','/','%',
    '4','5','6','*','1/x',
    '1','2','3','-','=',
    '0','.','+',
    'Ω'
    ]
    button_list2 = [
    'MC','MR','MS','(',')',
    '<-','C','±','√','Quit',
    'sin(','cos(','tan(','1/tan(','=',
    'ln(','x!','x^2','e','pi',
    'Ω'
    ]
    memory = ''
    endings = ['%', '1/x', '=', 'ctg', 'Quit', '+', 'pi', ')' ]
    button_list = button_list2
    def place_buttons(text=''):
        global label
        global buttons
        global button_list
        if button_list == button_list2:
            button_list = button_list1
        else:
            button_list = button_list2
        buttons = []
        label = Label(window, width = 39, bg='#89c4f4')
        label.place(x=10, y=6)
        label['text'] = text
        m = 45
        n = 30
        row = label['text'].count('\n') + 1
        column = 1
        for b in button_list:
            def command(x=b):
                click(x)
            btn = Button(window, text = b, width = 5, relief = 'ridge', bg = '#89c4f4', fg  = 'black', command = command)
            btn.place(y = row*n, x = column*m)
            buttons += [btn]
            if b in endings:
                row += 1
                column = 1
            else:
                column += 1
    place_buttons()
    window.geometry('300x250')
    window.mainloop()
def delete():
	label1.destroy()
	entry1.destroy()
	label2.destroy()
	entry2.destroy()
	label3.destroy()
	entry3.destroy()
	label4.destroy()
	entry4.destroy()
	Button1.destroy()
	Button2.destroy()
	Button3.destroy()
	Button4.destroy()
	Button5.destroy()
	Button6.destroy()
	Button7.destroy()
	Button8.destroy()
	Button9.destroy()
	Button10.destroy()
	Button11.destroy()
	Button12.destroy()
	Button13.destroy()
	Button14.destroy()
def build():
	global label1
	global label2
	global label3
	global label4
	global label5
	global entry1
	global entry2
	global entry3
	global entry4
	global entry5
	global Button1
	global Button2
	global Button3
	global Button4
	global Button5
	global Button6
	global Button7
	global Button8
	global Button9
	global Button10
	global Button11
	global Button12
	global Button13
	global Button14
	global Button15
	global figure
	figure = plt.figure('Graphs', figsize=(3,3))
	label1 = Label(root, text='dy/dx = ', bg='#c5eff7', fg='gray15')
	label2 = Label(root, text='y0 = ', bg='#c5eff7', fg='gray15')
	label3 = Label(root, text='x0 = ', bg='#c5eff7', fg='gray15')
	label4 = Label(root, text='h = ', bg='#c5eff7', fg='gray15')
	label5 = Label(root, text='n = ', bg='#c5eff7', fg='gray15')
	entry1 = Entry(root, width=40, bg='#89c4f4', fg='black', border=0)
	entry2 = Entry(root, width=3, bg='#89c4f4', fg='black', border=0)
	entry3 = Entry(root, width=3, bg='#89c4f4', fg='black', border=0)
	entry4 = Entry(root, width=3, bg='#89c4f4', fg='black', border=0)
	entry5 = Entry(root, width=3, bg='#89c4f4', fg='black', border=0)
	Button1 = Checkbutton(root, state=ACTIVE, text='Euler', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check1)
	Button2 = Checkbutton(root, state=ACTIVE, text='Improved Euler', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check2)
	Button3 = Checkbutton(root, state=ACTIVE, text='Runge-Kutta II', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check3)
	Button4 = Checkbutton(root, state=ACTIVE, text='Runge-Kutta III', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check4)
	Button5 = Checkbutton(root, state=ACTIVE, text='Runge-Kutta IV', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check5)
	Button13 = Checkbutton(root, state=ACTIVE, text='3D graph', activebackground='#c5eff7', activeforeground='gray15', bg='#c5eff7', fg='gray15', relief='ridge', selectcolor='#c5eff7', command=check6)
	Button6 = Button(root, text='Calculate', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=graphs)
	Button7 = Button(root, text='ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=Differential_Equation)
	Button8 = Button(root, text='ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=y_initial)
	Button9 = Button(root, text='ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=x_initial)
	Button10 = Button(root, text='ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=sequence)
	Button15 = Button(root, text='ok', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=iteration)
	Button11 = Button(root, text='Reset', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=reset)
	Button12 = Button(root, text='Quit', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=root.destroy)
	Button14 = Button(root, text='Calculator', bg='#c5eff7', fg='gray15', relief='ridge', border=0, command=calculator_window)
	label1.place(y=6, x=100)
	entry1.place(y=10, x=150)    
	label2.place(y=36, x=118)
	entry2.place(y=40, x=150)
	label3.place(y=66, x=118)
	entry3.place(y=70, x=150)
	label4.place(y=96, x=123)
	entry4.place(y=100, x=150)
	label5.place(y=126, x=123)
	entry5.place(y=130, x=150)
	Button1.place(y=170, x=50)
	Button2.place(y=210, x=50)
	Button3.place(y=250, x=50)
	Button4.place(y=290, x=50)
	Button5.place(y=330, x=50)
	Button6.place(y=330, x=230)
	Button7.place(y=8, x=400)
	Button8.place(y=38, x=178)
	Button9.place(y=68, x=178)
	Button10.place(y=98, x=178)
	Button11.place(y=300,x=240)
	Button12.place(y=270,x=242)
	Button13.place(y=170,x=250)
	Button14.place(y=210,x=250)
	Button15.place(y=128, x=178)
build()
root.mainloop()