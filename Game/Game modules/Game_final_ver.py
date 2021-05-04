'''
Lines
-------------------------------------------
Guess Character : 230 - 800 
Easy Points : 803 - 1172
Guess by frame : 1175 - 1544
Opening : 1547 - 1964
Random : 1967 - 2409
Quotes : 2412 - 2854
Ending : 2857 - 3274
TV series : 3277 - 3718
Is it trap : 3721 - 4090
Game music : 4093 - 4510
'''
from tkinter import *
from pygame import mixer
from PIL import ImageTk, Image
import random 
from parameters import *
from images import *
newwin = Tk()
newwin.title('GCC Game')
newwin.geometry('700x700')
newwin.iconbitmap(iconbitmap)
newwin.configure(bg='black')#, cursor='@C:/Users/User/Documents/My Python/Game/cursor.cur')
mixer.init()
re1 = PhotoImage(file=hover_category1)
re2 = PhotoImage(file=hover_category2)
re3 = PhotoImage(file=hover_category3)      
re4 = PhotoImage(file=hover_category4)
re5 = PhotoImage(file=hover_category5)
re6 = PhotoImage(file=hover_category6)
re7 = PhotoImage(file=hover_category7)
re8 = PhotoImage(file=hover_category8)
re9 = PhotoImage(file=hover_category9)
re10 = PhotoImage(file=hover_category10)
re11 = PhotoImage(file=hover_exit)
re12 = PhotoImage(file='C:/Users/User/Documents/My Python/Game/1st page/random_re.png')
re13 = PhotoImage(file=hover_question1)
re14 = PhotoImage(file=hover_question2)
re15 = PhotoImage(file=hover_question3)
re16 = PhotoImage(file=hover_question4)
re17 = PhotoImage(file=hover_question5)
re18 = PhotoImage(file=hover_question6)
re19 = PhotoImage(file=hover_question7)
re20 = PhotoImage(file=hover_question8)
re21 = PhotoImage(file=hover_question9)
re22 = PhotoImage(file=hover_question10)
re23 = PhotoImage(file=hover_question11)
re24 = PhotoImage(file=hover_question12)
re25 = PhotoImage(file=hover_back)
re26 = PhotoImage(file=hover_start)
def hover_enter1(event):
	button1['image'] = re1
def hover_leave1(event):
	button1['image'] = d1
def hover_enter2(event):
	button2['image'] = re2
def hover_leave2(event):
	button2['image'] = d2
def hover_enter3(event):
	button3['image'] = re3
def hover_leave3(event):
	button3['image'] = d3
def hover_enter4(event):
	button4['image'] = re4
def hover_leave4(event):
	button4['image'] = d4
def hover_enter5(event):
	button5['image'] = re5
def hover_leave5(event):
	button5['image'] = d5
def hover_enter6(event):
	button6['image'] = re6
def hover_leave6(event):
	button6['image'] = d6
def hover_enter7(event):
	button7['image'] = re7
def hover_leave7(event):
	button7['image'] = d7
def hover_enter8(event):
	button8['image'] = re8
def hover_leave8(event):
	button8['image'] = d8
def hover_enter9(event):
	button9['image'] = re9
def hover_leave9(event):
	button9['image'] = d9
def hover_enter10(event):
	button10['image'] = re10
def hover_leave10(event):
	button10['image'] = d10
def hover_enter11(event):
	button11['image'] = re11
def hover_leave11(event):
	button11['image'] = x
# def hover_enter12(event):
# 	button12['image'] = re12
# def hover_leave12(event):
# 	button12['image'] = y
def hover_enter13(event):
	button1['image'] = re13
def hover_leave13(event):
	button1['image'] = key1
def hover_enter14(event):
	button2['image'] = re14
def hover_leave14(event):
	button2['image'] = key2
def hover_enter15(event):
	button3['image'] = re15
def hover_leave15(event):
	button3['image'] = key3
def hover_enter16(event):
	button4['image'] = re16
def hover_leave16(event):
	button4['image'] = key4
def hover_enter17(event):
	button5['image'] = re17
def hover_leave17(event):
	button5['image'] = key5
def hover_enter18(event):
	button6['image'] = re18
def hover_leave18(event):
	button6['image'] = key6
def hover_enter19(event):
	button7['image'] = re19
def hover_leave19(event):
	button7['image'] = key7
def hover_enter20(event):
	button8['image'] = re20
def hover_leave20(event):
	button8['image'] = key8
def hover_enter21(event):
	button9['image'] = re21
def hover_leave21(event):
	button9['image'] = key9
def hover_enter22(event):
	button10['image'] = re22
def hover_leave22(event):
	button10['image'] = key10
def hover_enter23(event):
	button11['image'] = re23
def hover_leave23(event):
	button11['image'] = key11
def hover_enter24(event):
	button12['image'] = re24
def hover_leave24(event):
	button12['image'] = key12
def hover_enter25(event):
	button13['image'] = re25
def hover_leave25(event):
	button13['image'] = s
def hover_enter26(event):
	btn['image'] = re26
def hover_leave26(event):
	btn['image'] = strt
def timer():
	global t 
	if t>0:
		lbl.config(text=t)
		t = t-1
		lbl.after(1000,timer)
	elif t==0:
		rt.destroy()
def timer_questions():
	global t_q 
	if t_q>0:
		lbl_q.config(text=t_q)
		t_q = t_q-1
		lbl_q.after(1000,timer_questions)
	elif t_q==0:
		rt.destroy()
	btn.destroy()
def timer_music():
	global t_music 
	if t_music>0:
		lbl_music.config(text=t_music)
		t_music = t_music-1
		lbl_music.after(1000,timer_music)
	elif t_music==0:
		rt.destroy()
def on_closing():
	mixer.music.set_volume(0)
	rt.destroy()
def choose(event):
	global r
	r['bg'] = 'black'
	r = random.choice(d)
	r['bg'] = 'light blue' 
newwin.bind('<f>', choose)
#----------------------------------------------------START---------------------------------------------------------------
#--------------------------------GUESS CHARACTER START-------------------------------------------------------------------
def delete1():
	frame1.destroy()
	frame2.destroy()
	frame3.destroy()
	frame4.destroy()
	frame5.destroy()
	frame6.destroy()
	frame7.destroy()
	frame8.destroy()
	frame9.destroy()
	frame10.destroy()
	button11.destroy()
	div3.destroy()
	label.destroy()
def delete2():
	button1.destroy()
	button2.destroy()
	button3.destroy()
	button4.destroy()
	button5.destroy()
	button6.destroy()
	button7.destroy()
	button8.destroy()
	button9.destroy()
	button10.destroy()
	button11.destroy()
	button12.destroy()
	button13.destroy()
	pic3.destroy()
def character_picture1():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question1
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state.append(1)
	button1.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture2():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(2)
	button2.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture3():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(3)
	button3.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture4():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(4)
	button4.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture5():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(5)
	button5.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture6():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(6)
	button6.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture7():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(7)
	button7.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture8():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(8)
	button8.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture9():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(9)
	button9.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture10():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(10)
	button10.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def character_picture11():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(11)
	button11.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack() 
	timer()
def character_picture12():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category1_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state.append(12)
	button12.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_character():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category1_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=298)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=character_picture1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=character_picture2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=character_picture3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=character_picture4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=character_picture5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=character_picture6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=character_picture7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=character_picture8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=character_picture9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=character_picture10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=character_picture11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=character_picture12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state:
		button1.destroy()
	if 2 in state:
		button2.destroy()
	if 3 in state:
		button3.destroy()
	if 4 in state:
		button4.destroy()
	if 5 in state:
		button5.destroy()
	if 6 in state:
		button6.destroy()
	if 7 in state:
		button7.destroy()
	if 8 in state:
		button8.destroy()
	if 9 in state:
		button9.destroy()
	if 10 in state:
		button10.destroy()
	if 11 in state:
		button11.destroy()
	if 12 in state:
		button12.destroy()
def build():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global frame1
	global frame2
	global frame3
	global frame4
	global frame5
	global frame6
	global frame7
	global frame8
	global frame9
	global frame10
	global x
	global div3
	global y
	global entry1
	global entry2
	global label1
	global label2
	global e
	global d1
	global d2
	global d3
	global d4
	global d5
	global d6
	global d7
	global d8
	global d9
	global d10
	global j
	global d
	global r
	global label
	r = Label(newwin, bg='white')
	if j==0:
		i_m_g = Image.open(logo)
		i_m_g = i_m_g.resize((150, 150), Image.ANTIALIAS)
		i_m_g = ImageTk.PhotoImage(i_m_g)	
		panel = Label(newwin, image=i_m_g)
		panel.image = i_m_g
		panel.pack()
		advertising1 = advertising_pic
		advertising2 = Image.open(advertising1)
		advertising2 = ImageTk.PhotoImage(advertising2)	
		advertising3 = Label(newwin, bg='black', image=advertising2)
		advertising3.image = advertising2
		advertising3.place(x=470,y=10)
	j += 1
	frame1 = LabelFrame(newwin, text='1', font='times 15', bg='black', fg='white', padx=70, pady=1) 
	frame2 = LabelFrame(newwin, text='2', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame3 = LabelFrame(newwin, text='3', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame4 = LabelFrame(newwin, text='4', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame5 = LabelFrame(newwin, text='5', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame6 = LabelFrame(newwin, text='6', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame7 = LabelFrame(newwin, text='7', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame8 = LabelFrame(newwin, text='8', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame9 = LabelFrame(newwin, text='9', font='times 15', bg='black', fg='white', padx=70, pady=1)
	frame10 = LabelFrame(newwin, text='10', font='times 15', bg='black', fg='white', padx=70, pady=1)
	label = Label(newwin, text='Press F to choose a section', bg='black', fg='white')
	d1 = PhotoImage(file=category_button1)
	button1 = Button(frame1, image=d1, bg='black', borderwidth=0, command=update_win1)	
	button1.bind('<Enter>',hover_enter1)
	button1.bind('<Leave>',hover_leave1)
	d2 = PhotoImage(file=category_button2)
	button2 = Button(frame2, image=d2, bg='black', borderwidth=0, command=update_win2)
	button2.bind('<Enter>',hover_enter2)
	button2.bind('<Leave>',hover_leave2)
	d3 = PhotoImage(file=category_button3)
	button3 = Button(frame3, image=d3, bg='black', borderwidth=0, command=update_win3)
	button3.bind('<Enter>',hover_enter3)
	button3.bind('<Leave>',hover_leave3)
	d4 = PhotoImage(file=category_button4)
	button4 = Button(frame4, image=d4, bg='black', borderwidth=0, command=update_win4)
	button4.bind('<Enter>',hover_enter4)
	button4.bind('<Leave>',hover_leave4)
	d5 = PhotoImage(file=category_button5)
	button5 = Button(frame5, image=d5, bg='black', borderwidth=0, command=update_win5)
	button5.bind('<Enter>',hover_enter5)
	button5.bind('<Leave>',hover_leave5)
	d6 = PhotoImage(file=category_button6)
	button6 = Button(frame6, image=d6, bg='black', borderwidth=0, command=update_win6)
	button6.bind('<Enter>',hover_enter6)
	button6.bind('<Leave>',hover_leave6)
	d7 = PhotoImage(file=category_button7)
	button7 = Button(frame7, image=d7, bg='black', borderwidth=0, command=update_win7)
	button7.bind('<Enter>',hover_enter7)
	button7.bind('<Leave>',hover_leave7)
	d8 = PhotoImage(file=category_button8)
	button8 = Button(frame8, image=d8, bg='black', borderwidth=0, command=update_win8)
	button8.bind('<Enter>',hover_enter8)
	button8.bind('<Leave>',hover_leave8)
	d9 = PhotoImage(file=category_button9)
	button9 = Button(frame9, image=d9, bg='black', borderwidth=0, command=update_win9)
	button9.bind('<Enter>',hover_enter9)
	button9.bind('<Leave>',hover_leave9)
	d10 = PhotoImage(file=category_button10) 
	button10 = Button(frame10, image=d10, bg='black', borderwidth=0, command=update_win10)
	button10.bind('<Enter>',hover_enter10)
	button10.bind('<Leave>',hover_leave10)
	x = PhotoImage(file=exit_pic)
	button11 = Button(newwin, bg='black', image=x, borderwidth=0, command=newwin.destroy)
	button11.bind('<Enter>',hover_enter11)
	button11.bind('<Leave>',hover_leave11)
	div1 = division
	div2 = Image.open(div1)
	div2 = div2.resize((5, 300), Image.ANTIALIAS)
	div2 = ImageTk.PhotoImage(div2)	
	div3 = Label(newwin, bg='black', image=div2)
	div3.image = div2
	div3.place(x=345,y=340)
	frame1.place(x=40,y=340)
	frame2.place(x=40,y=400)
	frame3.place(x=40,y=460)
	frame4.place(x=40,y=520)
	frame5.place(x=40,y=580)
	frame6.place(x=398,y=340)
	frame7.place(x=398,y=400)
	frame8.place(x=398,y=460)
	frame9.place(x=398,y=520)
	frame10.place(x=398,y=580)
	button1.pack()
	button2.pack()
	button3.pack()
	button4.pack()
	button5.pack()
	button6.pack()
	button7.pack()
	button8.pack()
	button9.pack()
	button10.pack()
	button11.place(x=260,y=650)
	label.place(x=275,y=250)
	d = [button1,button2,button3,button4,button5,button6,button7,button8,button9,button10]
def update_win1():
	delete1()
	guess_character()
def go_back1():
	delete2()
	build()
#--------------------------------GUESS CHARACTER END--------------------------------------------------------------------


#--------------------------------EASY POINTS START----------------------------------------------------------------------
def update_win2():
	delete1() 
	easy_points()
def easy_points1():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question1
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state2.append(1)
	button1.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points2():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(2)
	button2.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points3():
	global lbl
	global rt
	global t
	t = 20  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(3)
	button3.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points4():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(4)
	button4.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points5():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(5)
	button5.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points6():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(6)
	button6.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points7():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(7)
	button7.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points8():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(8)
	button8.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points9():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(9)
	button9.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points10():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(10)
	button10.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points11():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(11)
	button11.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack() 
	timer()
def easy_points12():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category2_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state2.append(12)
	button12.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def easy_points():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category2_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=easy_points1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=easy_points2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=easy_points3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=easy_points4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=easy_points5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=easy_points6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=easy_points7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=easy_points8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=easy_points9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=easy_points10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=easy_points11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=easy_points12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state2:
		button1.destroy()
	if 2 in state2:
		button2.destroy()
	if 3 in state2:
		button3.destroy()
	if 4 in state2:
		button4.destroy()
	if 5 in state2:
		button5.destroy()
	if 6 in state2:
		button6.destroy()
	if 7 in state2:
		button7.destroy()
	if 8 in state2:
		button8.destroy()
	if 9 in state2:
		button9.destroy()
	if 10 in state2:
		button10.destroy()
	if 11 in state2:
		button11.destroy()
	if 12 in state2:
		button12.destroy()
#--------------------------------EASY POINTS END------------------------------------------------------------------------


#--------------------------------GUESS BY FRAME START-------------------------------------------------------------------
def update_win3():
	delete1() 
	guess_by_frame()
def guess_by_frame1():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question1
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state3.append(1)
	button1.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame2():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(2)
	button2.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame3():
	global lbl
	global rt
	global t
	t = 20  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(3)
	button3.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame4():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(4)
	button4.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame5():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(5)
	button5.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame6():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(6)
	button6.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame7():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(7)
	button7.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame8():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(8)
	button8.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame9():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(9)
	button9.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame10():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(10)
	button10.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame11():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(11)
	button11.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack() 
	timer()
def guess_by_frame12():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category3_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state3.append(12)
	button12.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def guess_by_frame():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category3_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=guess_by_frame1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=guess_by_frame2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=guess_by_frame3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=guess_by_frame4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=guess_by_frame5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=guess_by_frame6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=guess_by_frame7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=guess_by_frame8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=guess_by_frame9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=guess_by_frame10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=guess_by_frame11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=guess_by_frame12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state3:
		button1.destroy()
	if 2 in state3:
		button2.destroy()
	if 3 in state3:
		button3.destroy()
	if 4 in state3:
		button4.destroy()
	if 5 in state3:
		button5.destroy()
	if 6 in state3:
		button6.destroy() 
	if 7 in state3:
		button7.destroy()
	if 8 in state3:
		button8.destroy()
	if 9 in state3:
		button9.destroy()
	if 10 in state3:
		button10.destroy()
	if 11 in state3:
		button11.destroy()
	if 12 in state3:
		button12.destroy()
#--------------------------------GUESS BT FRAME END---------------------------------------------------------------------


#--------------------------------OPENING START--------------------------------------------------------------------------
def update_win4():
	delete1()
	opening()
def opening1():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state4.append(1)
	button1.destroy()
	mixer.music.load(category4_question1)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening2():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(2)
	button2.destroy()
	mixer.music.load(category4_question2)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening3():
	global lbl_music
	global rt
	global t_music
	t_music = 22  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(3)
	button3.destroy()
	mixer.music.load(category4_question3)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening4():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(4)
	button4.destroy()
	mixer.music.load(category4_question4)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening5():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(5)
	button5.destroy()
	mixer.music.load(category4_question5)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening6():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(6)
	button6.destroy()
	mixer.music.load(category4_question6)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening7():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(7)
	button7.destroy()
	mixer.music.load(category4_question7)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening8():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(8)
	button8.destroy()
	mixer.music.load(category4_question8)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening9():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(9)
	button9.destroy()
	mixer.music.load(category4_question9)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening10():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(10)
	button10.destroy()
	mixer.music.load(category4_question10)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening11():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(11)
	button11.destroy()
	mixer.music.load(category4_question11)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack() 
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening12():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state4.append(12)
	button12.destroy()
	mixer.music.load(category4_question12)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def opening():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category4_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=opening1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=opening2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=opening3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=opening4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=opening5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=opening6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=opening7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=opening8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=opening9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=opening10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=opening11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=opening12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state4:
		button1.destroy()
	if 2 in state4:
		button2.destroy()
	if 3 in state4:
		button3.destroy()
	if 4 in state4:
		button4.destroy()
	if 5 in state4:
		button5.destroy()
	if 6 in state4:
		button6.destroy()
	if 7 in state4:
		button7.destroy()
	if 8 in state4:
		button8.destroy()
	if 9 in state4:
		button9.destroy()
	if 10 in state4:
		button10.destroy()
	if 11 in state4:
		button11.destroy()
	if 12 in state4:
		button12.destroy()
#--------------------------------OPENING END----------------------------------------------------------------------------


#--------------------------------RANDOM START---------------------------------------------------------------------------
def update_win5():
	delete1() 
	random_questions()
def random_questions1():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question1
	strt = PhotoImage(file=start)
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state5.append(1)
	button1.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions2():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(2)
	button2.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions3():
	global lbl_q
	global rt  
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(3)
	button3.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions4():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(4)
	button4.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions5():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(5)
	button5.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions6():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(6)
	button6.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions7():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(7)
	button7.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions8():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(8)
	button8.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions9():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(9)
	button9.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions10():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(10)
	button10.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions11():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(11)
	button11.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26) 
def random_questions12():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category5_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state5.append(12)
	button12.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def random_questions():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category5_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=random_questions1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=random_questions2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=random_questions3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=random_questions4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=random_questions5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=random_questions6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=random_questions7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=random_questions8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=random_questions9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=random_questions10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=random_questions11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=random_questions12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state5:
		button1.destroy()
	if 2 in state5:
		button2.destroy()
	if 3 in state5:
		button3.destroy()
	if 4 in state5:
		button4.destroy()
	if 5 in state5:
		button5.destroy()
	if 6 in state5:
		button6.destroy()
	if 7 in state5:
		button7.destroy()
	if 8 in state5:
		button8.destroy()
	if 9 in state5:
		button9.destroy()
	if 10 in state5:
		button10.destroy()
	if 11 in state5:
		button11.destroy()
	if 12 in state5:
		button12.destroy()
#--------------------------------RANDOM END-----------------------------------------------------------------------------


#--------------------------------QUOTES START---------------------------------------------------------------------------
def update_win6():
	delete1() 
	quotes()
def quotes1():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question1
	strt = PhotoImage(file=start)
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state6.append(1)
	button1.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes2():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(2)
	button2.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes3():
	global lbl_q
	global rt  
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(3)
	button3.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes4():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(4)
	button4.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes5():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(5)
	button5.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes6():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(6)
	button6.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes7():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(7)
	button7.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes8():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(8)
	button8.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes9():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(9)
	button9.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes10():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(10)
	button10.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def quotes11():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(11)
	button11.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26) 
def quotes12():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category6_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state6.append(12)
	button12.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)    
def quotes():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category6_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=quotes1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=quotes2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=quotes3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=quotes4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=quotes5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=quotes6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=quotes7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=quotes8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=quotes9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=quotes10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=quotes11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=quotes12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state6:
		button1.destroy()
	if 2 in state6:
		button2.destroy()
	if 3 in state6:
		button3.destroy()
	if 4 in state6:
		button4.destroy()
	if 5 in state6:
		button5.destroy()
	if 6 in state6:
		button6.destroy()
	if 7 in state6:
		button7.destroy()
	if 8 in state6:
		button8.destroy()
	if 9 in state6:
		button9.destroy()
	if 10 in state6:
		button10.destroy()
	if 11 in state6:
		button11.destroy()
	if 12 in state6:
		button12.destroy()
#--------------------------------QUOTES END-----------------------------------------------------------------------------


#--------------------------------ENDING START---------------------------------------------------------------------------
def update_win7():
	delete1()
	ending()
def ending1():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state7.append(1)
	button1.destroy()
	mixer.music.load(category7_question1)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending2():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(2)
	button2.destroy()
	mixer.music.load(category7_question2)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending3():
	global lbl_music
	global rt
	global t_music
	t_music = 22  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(3)
	button3.destroy()
	mixer.music.load(category7_question3)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending4():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(4)
	button4.destroy()
	mixer.music.load(category7_question4)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending5():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(5)
	button5.destroy()
	mixer.music.load(category7_question5)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending6():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(6)
	button6.destroy()
	mixer.music.load(category7_question6)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending7():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(7)
	button7.destroy()
	mixer.music.load(category7_question7)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending8():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(8)
	button8.destroy()
	mixer.music.load(category7_question8)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending9():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(9)
	button9.destroy()
	mixer.music.load(category7_question9)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending10():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(10)
	button10.destroy()
	mixer.music.load(category7_question10)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending11():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(11)
	button11.destroy()
	mixer.music.load(category7_question11)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack() 
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending12():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state7.append(12)
	button12.destroy()
	mixer.music.load(category7_question12)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def ending():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7  
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12   
	global pic3
	global s  
	pic1 = category7_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2  
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=ending1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=ending2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=ending3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=ending4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=ending5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=ending6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=ending7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=ending8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=ending9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=ending10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=ending11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=ending12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state7:
		button1.destroy()
	if 2 in state7:
		button2.destroy()
	if 3 in state7:
		button3.destroy()
	if 4 in state7:
		button4.destroy()
	if 5 in state7:
		button5.destroy()
	if 6 in state7:
		button6.destroy()
	if 7 in state7:
		button7.destroy()
	if 8 in state7:
		button8.destroy()
	if 9 in state7:
		button9.destroy()
	if 10 in state7:
		button10.destroy()
	if 11 in state7:
		button11.destroy()
	if 12 in state7:
		button12.destroy()
#--------------------------------ENDING END-----------------------------------------------------------------------------


#--------------------------------TV SERIES START------------------------------------------------------------------------
def update_win8():
	delete1() 
	TV_series()
def TV_series1():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question1
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state8.append(1)
	button1.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series2():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(2)
	button2.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series3():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(3)
	button3.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series4():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(4)
	button4.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series5():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(5)
	button5.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series6():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(6)
	button6.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series7():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(7)
	button7.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series8():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(8)
	button8.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series9():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(9)
	button9.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series10():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(10)
	button10.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series11():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(11)
	button11.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26) 
def TV_series12():
	global lbl_q
	global rt
	global btn
	global strt
	global t_q
	t_q = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category8_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state8.append(12)
	button12.destroy()
	lbl_q = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	strt = PhotoImage(file=start)
	btn = Button(rt, bg='black', image=strt, borderwidth=0, command=timer_questions)
	btn.pack()
	lbl_q.pack()
	btn.bind('<Enter>',hover_enter26)
	btn.bind('<Leave>',hover_leave26)
def TV_series():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category8_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=TV_series1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=TV_series2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=TV_series3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=TV_series4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=TV_series5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=TV_series6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=TV_series7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=TV_series8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=TV_series9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=TV_series10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=TV_series11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=TV_series12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state8:
		button1.destroy()
	if 2 in state8:
		button2.destroy()
	if 3 in state8:
		button3.destroy()
	if 4 in state8:
		button4.destroy()
	if 5 in state8:
		button5.destroy()
	if 6 in state8:
		button6.destroy()
	if 7 in state8:
		button7.destroy()
	if 8 in state8:
		button8.destroy()
	if 9 in state8:
		button9.destroy()
	if 10 in state8:
		button10.destroy()
	if 11 in state8:
		button11.destroy()
	if 12 in state8:
		button12.destroy()
#--------------------------------TV SERIES END--------------------------------------------------------------------------


#--------------------------------IS IT TRAP START-----------------------------------------------------------------------
def update_win9():
	delete1() 
	is_it_trap()
def trap_picture1():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question1
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state9.append(1)
	button1.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture2():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question2
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(2)
	button2.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture3():
	global lbl
	global rt
	global t
	t = 20  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question3
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(3)
	button3.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture4():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question4
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(4)
	button4.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture5():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question5
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(5)
	button5.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture6():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question6
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(6)
	button6.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture7():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question7
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(7)
	button7.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture8():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question8
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(8)
	button8.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture9():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question9
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(9)
	button9.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture10():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question10
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(10)
	button10.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def trap_picture11():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question11
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(11)
	button11.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack() 
	timer()
def trap_picture12():
	global lbl
	global rt
	global t
	t = 20
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = category9_question12
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state9.append(12)
	button12.destroy()
	lbl = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl.pack()
	timer()
def is_it_trap():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7 
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12
	global pic3
	global s
	pic1 = category9_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=trap_picture1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=trap_picture2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=trap_picture3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=trap_picture4)
	button4.bind('<Enter>',hover_enter16)
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=trap_picture5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=trap_picture6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=trap_picture7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=trap_picture8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=trap_picture9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=trap_picture10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=trap_picture11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=trap_picture12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state9:
		button1.destroy()
	if 2 in state9:
		button2.destroy()
	if 3 in state9:
		button3.destroy()
	if 4 in state9:
		button4.destroy()
	if 5 in state9:
		button5.destroy()
	if 6 in state9:
		button6.destroy()
	if 7 in state9:
		button7.destroy()
	if 8 in state9:
		button8.destroy()
	if 9 in state9:
		button9.destroy()
	if 10 in state9:
		button10.destroy()
	if 11 in state9:
		button11.destroy()
	if 12 in state9:
		button12.destroy()
#--------------------------------IS IT TRAP END-------------------------------------------------------------------------


#--------------------------------GAME MUSIC START-----------------------------------------------------------------------
def update_win10():
	delete1()
	game_music()
def game_music1():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack() 
	state10.append(1)
	button1.destroy()
	mixer.music.load(category10_question1)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music2():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(2)
	button2.destroy()
	mixer.music.load(category10_question2)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music3():
	global lbl_music
	global rt
	global t_music
	t_music = 22  
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(3)
	button3.destroy()
	mixer.music.load(category10_question3)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music4():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(4)
	button4.destroy()
	mixer.music.load(category10_question4)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music5():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(5)
	button5.destroy()
	mixer.music.load(category10_question5)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music6():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(6)
	button6.destroy()
	mixer.music.load(category10_question6)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music7():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(7)
	button7.destroy()
	mixer.music.load(category10_question7)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music8():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(8)
	button8.destroy()
	mixer.music.load(category10_question8)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music9():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(9)
	button9.destroy()
	mixer.music.load(category10_question9)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music10():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(10)
	button10.destroy()
	mixer.music.load(category10_question10)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music11():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(11)
	button11.destroy()
	mixer.music.load(category10_question11)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack() 
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music12():
	global lbl_music
	global rt
	global t_music
	t_music = 22
	rt = Toplevel(newwin)
	rt.configure(bg='black')
	rt.iconbitmap(iconbitmap)
	x = music_bg
	img = Image.open(x)
	img = img.resize((600, 400), Image.ANTIALIAS)
	img = ImageTk.PhotoImage(img)
	panel = Label(rt, image=img, bg='black')
	panel.image = img
	panel.pack()
	state10.append(12)
	button12.destroy()
	mixer.music.load(category10_question12)
	mixer.music.play()
	mixer.music.set_volume(1)
	lbl_music = Label(rt, bg='black', fg='deep sky blue', font='times 50')
	lbl_music.pack()
	rt.protocol("WM_DELETE_WINDOW", on_closing)
	timer_music()
def game_music():
	global button1 
	global button2 
	global button3 
	global button4 
	global button5 
	global button6 
	global button7  
	global button8 
	global button9 
	global button10
	global button11
	global button12
	global button13 
	global key1 
	global key2
	global key3
	global key4
	global key5
	global key6
	global key7
	global key8
	global key9
	global key10
	global key11
	global key12   
	global pic3
	global s  
	pic1 = category10_circle_pic
	pic2 = Image.open(pic1)
	pic2 = pic2.resize((200, 200), Image.ANTIALIAS)
	pic2 = ImageTk.PhotoImage(pic2)	
	pic3 = Label(newwin, bg='black', image=pic2)
	pic3.image = pic2  
	pic3.place(x=250,y=300)
	key1 = PhotoImage(file=question_button1)
	button1 = Button(newwin, bg='black', image=key1, borderwidth=0, command=game_music1)
	button1.bind('<Enter>',hover_enter13)
	button1.bind('<Leave>',hover_leave13)
	key2 = PhotoImage(file=question_button2)
	button2 = Button(newwin, bg='black', image=key2, borderwidth=0, command=game_music2)
	button2.bind('<Enter>',hover_enter14)
	button2.bind('<Leave>',hover_leave14)
	key3 = PhotoImage(file=question_button3)
	button3 = Button(newwin, bg='black', image=key3, borderwidth=0, command=game_music3)
	button3.bind('<Enter>',hover_enter15)
	button3.bind('<Leave>',hover_leave15)
	key4 = PhotoImage(file=question_button4)
	button4 = Button(newwin, bg='black', image=key4, borderwidth=0, command=game_music4)
	button4.bind('<Enter>',hover_enter16)  
	button4.bind('<Leave>',hover_leave16)
	key5 = PhotoImage(file=question_button5)
	button5 = Button(newwin, bg='black', image=key5, borderwidth=0, command=game_music5)
	button5.bind('<Enter>',hover_enter17)
	button5.bind('<Leave>',hover_leave17)
	key6 = PhotoImage(file=question_button6)
	button6 = Button(newwin, bg='black', image=key6, borderwidth=0, command=game_music6)
	button6.bind('<Enter>',hover_enter18)
	button6.bind('<Leave>',hover_leave18)
	key7 = PhotoImage(file=question_button7)
	button7 = Button(newwin, bg='black', image=key7, borderwidth=0, command=game_music7)
	button7.bind('<Enter>',hover_enter19)
	button7.bind('<Leave>',hover_leave19)
	key8 = PhotoImage(file=question_button8)
	button8 = Button(newwin, bg='black', image=key8, borderwidth=0, command=game_music8)
	button8.bind('<Enter>',hover_enter20)
	button8.bind('<Leave>',hover_leave20)
	key9 = PhotoImage(file=question_button9)
	button9 = Button(newwin, bg='black', image=key9, borderwidth=0, command=game_music9)
	button9.bind('<Enter>',hover_enter21)
	button9.bind('<Leave>',hover_leave21)
	key10 = PhotoImage(file=question_button10)
	button10 = Button(newwin, bg='black', image=key10, borderwidth=0, command=game_music10)
	button10.bind('<Enter>',hover_enter22)
	button10.bind('<Leave>',hover_leave22)
	key11 = PhotoImage(file=question_button11)
	button11 = Button(newwin, bg='black', image=key11, borderwidth=0, command=game_music11)
	button11.bind('<Enter>',hover_enter23)
	button11.bind('<Leave>',hover_leave23)
	key12 = PhotoImage(file=question_button12)
	button12 = Button(newwin, bg='black', image=key12, borderwidth=0, command=game_music12)
	button12.bind('<Enter>',hover_enter24)
	button12.bind('<Leave>',hover_leave24)
	s = PhotoImage(file=back_pic)
	button13 = Button(newwin, bg='black', image=s, borderwidth=0, command=go_back1)
	button13.bind('<Enter>',hover_enter25)
	button13.bind('<Leave>',hover_leave25)
	button1.place(x=320,y=180)
	button2.place(x=230,y=220)
	button3.place(x=160,y=280)
	button4.place(x=140,y=370)
	button5.place(x=160,y=460)
	button6.place(x=230,y=530)
	button7.place(x=320,y=560)
	button8.place(x=410,y=530)
	button9.place(x=480,y=460)
	button10.place(x=500,y=370)
	button11.place(x=480,y=280)
	button12.place(x=410,y=220)
	button13.place(x=260,y=650)
	if 1 in state10:
		button1.destroy()
	if 2 in state10:
		button2.destroy()
	if 3 in state10:
		button3.destroy()
	if 4 in state10:
		button4.destroy()
	if 5 in state10:
		button5.destroy()
	if 6 in state10:
		button6.destroy()
	if 7 in state10:
		button7.destroy()
	if 8 in state10:
		button8.destroy()
	if 9 in state10:
		button9.destroy()
	if 10 in state10:
		button10.destroy()
	if 11 in state10:
		button11.destroy()
	if 12 in state10:
		button12.destroy()
#--------------------------------GAME MUSIC END-------------------------------------------------------------------------


#----------------------------------------------------END----------------------------------------------------------------
build()
newwin.mainloop()	