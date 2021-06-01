from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from Parameters import *
from PIL import ImageTk, Image
import os
path = str(os.path.dirname(os.path.abspath(__file__)))
main = Tk()
main.geometry('1080x700')
main.iconbitmap(path+'\\logo.ico')
main.configure(bg='#05081a')
main.title('Veyron Sky')

def progress():
	pass
#-------------------------------------------------------------HOVER-----------------------------------------------------------------
def hover_admin(event):
	global adm_pic
	adm_pic = PhotoImage(file=path+'\\admin_hover.png')
	admin_button['image'] = adm_pic

def hoverl_admin(event):
	global adm_pic
	adm_pic = PhotoImage(file=path+'\\admin.png')
	admin_button['image'] = adm_pic 

def hover_guest(event):
	global gst_pic
	gst_pic = PhotoImage(file=path+'\\guest_hover.png')
	guest_button['image'] = gst_pic

def hoverl_guest(event):
	global gst_pic
	gst_pic = PhotoImage(file=path+'\\guest.png')
	guest_button['image'] = gst_pic

def hover_about(event):
	global ab_pic
	ab_pic = PhotoImage(file=path+'\\about_hover.png')
	ab_button['image'] = ab_pic

def hoverl_about(event):
	global ab_pic
	ab_pic = PhotoImage(file=path+'\\about.png')
	ab_button['image'] = ab_pic

def hover_contacts(event):
	global con_pic
	con_pic = PhotoImage(file=path+'\\contacts_hover.png')
	contacts['image'] = con_pic

def hoverl_contacts(event):
	global con_pic
	con_pic = PhotoImage(file=path+'\\contacts.png')
	contacts['image'] = con_pic

def hover_enter_button(event):
	global ent_pic
	ent_pic = PhotoImage(file=path+'\\enter_hover.png')
	enter_button['image'] = ent_pic

def hoverl_enter_button(event):
	global ent_pic
	ent_pic = PhotoImage(file=path+'\\enter.png')
	enter_button['image'] = ent_pic

def hover_back(event):
	global bk_pic
	bk_pic = PhotoImage(file=path+'\\back_hover.png')
	back['image'] = bk_pic

def hoverl_back(event):
	global bk_pic
	bk_pic = PhotoImage(file=path+'\\back.png')
	back['image'] = bk_pic

def hover_send_button(event):
	global send_pic
	send_pic = PhotoImage(file=path+'\\send_hover.png')
	send_button['image'] = send_pic

def hoverl_send_button(event):
	global send_pic
	send_pic = PhotoImage(file=path+'\\send.png')
	send_button['image'] = send_pic

def hover_fb_button(event):
	global fb_pic
	fb_pic = PhotoImage(file=path+'\\feedbacks_hover.png')
	fb_button['image'] = fb_pic

def hoverl_fb_button(event):
	global fb_pic
	fb_pic = PhotoImage(file=path+'\\feedbacks.png')
	fb_button['image'] = fb_pic

def hover_rinf_button(event):
	global rinf_pic
	rinf_pic = PhotoImage(file=path+'\\room_info_hover.png')
	rinf_button['image'] = rinf_pic

def hoverl_rinf_button(event):
	global rinf_pic
	rinf_pic = PhotoImage(file=path+'\\room_info.png')
	rinf_button['image'] = rinf_pic

def hover_hotst_button(event):
	global hotst_pic
	hotst_pic = PhotoImage(file=path+'\\hotel_staff_hover.png')
	hotst_button['image'] = hotst_pic

def hoverl_hotst_button(event):
	global hotst_pic
	hotst_pic = PhotoImage(file=path+'\\hotel_staff.png')
	hotst_button['image'] = hotst_pic

def hover_inv_button(event):
	global inv_pic
	inv_pic = PhotoImage(file=path+'\\invoices_hover.png')
	inv_button['image'] = inv_pic

def hoverl_inv_button(event):
	global inv_pic
	inv_pic = PhotoImage(file=path+'\\invoices.png')
	inv_button['image'] = inv_pic

def hover_guests_button(event):
	global guests_pic
	guests_pic = PhotoImage(file=path+'\\guests_hover.png')
	guests_button['image'] = guests_pic

def hoverl_guests_button(event):
	global guests_pic
	guests_pic = PhotoImage(file=path+'\\guests.png')
	guests_button['image'] = guests_pic

def hover_reg_button(event):
	global reg_pic
	reg_pic = PhotoImage(file=path+'\\registrations_hover.png')
	reg_button['image'] = reg_pic

def hoverl_reg_button(event):
	global reg_pic
	reg_pic = PhotoImage(file=path+'\\registrations.png')
	reg_button['image'] = reg_pic

def hover_newreg_button(event):
	global newreg_pic
	newreg_pic = PhotoImage(file=path+'\\new_registration_hover.png')
	newreg_button['image'] = newreg_pic

def hoverl_newreg_button(event):
	global newreg_pic
	newreg_pic = PhotoImage(file=path+'\\new_registration.png')
	newreg_button['image'] = newreg_pic
#-------------------------------------------------------------HOVER-----------------------------------------------------------------
def go_back():
	if cnt==0:
		id_label.place_forget()
		r_id_label.place_forget()
		enter_button.place_forget()
		back.place_forget()
		login.place_forget()
		password.place_forget()
		build()
	if cnt==1:
		share_label.place_forget()
		id_label.place_forget()
		r_id_label.place_forget()
		enter_button.place_forget()
		back.place_forget()
		login.place_forget()
		password.place_forget()
		build()
	if cnt==2:
		send_button.place_forget()
		r1_button.place_forget()
		r2_button.place_forget()
		r3_button.place_forget()
		r4_button.place_forget()
		r5_button.place_forget()
		variants.place_forget()
		guest()
	if cnt==3:
		fb_button.place_forget()
		newreg_button.place_forget()
		reg_button.place_forget()
		guests_button.place_forget()
		inv_button.place_forget()
		hotst_button.place_forget()
		rinf_button.place_forget()
		title.place(x=350,y=20)
		h_name.place(x=440,y=70)
		h_name2.place(x=343,y=295)
		admin()

def timer():
	global t
	if t>0:
		lbl.config(text=t)
		t = t-1
		lbl.after(1000,timer)
	elif t==0:
		thx_label.place_forget()
		lbl.place_forget()
		build()
		t = 3

def information():
	global text
	admin_button.place_forget()
	guest_button.place_forget()
	ab_button.place_forget()

#------------------------------------------------------GUEST-----------------------------------------------------------------------
def selected(event, k=[]):
	pass


def redirect():
	global thx_pic,thx_label,lbl,t
	sending_label.place_forget()
	progress.place_forget()
	lbl = Label(main, bg='#05081a', fg='yellow', font=('Arial black', 30))
	thx_pic = PhotoImage(file=path+'\\thx.png')
	thx_label = Label(main, bg='#05081a', image=thx_pic)
	thx_label.place(x=200,y=500)
	lbl.place(x=550,y=600)
	timer()

def bar():
    import time
    progress['value'] = 20
    main.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 40
    main.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 50
    main.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 60
    main.update_idletasks()
    time.sleep(0.5)
  
    progress['value'] = 80
    main.update_idletasks()
    time.sleep(0.5)
    progress['value'] = 100

    if progress['value']==100:
        redirect()

def send_rate():
	global sending_pic,sending_label,progress
	send_button.place_forget()
	r1_button.place_forget()
	r2_button.place_forget()
	r3_button.place_forget()
	r4_button.place_forget()
	r5_button.place_forget()
	back.place_forget()
	variants.place_forget()
	progress = Progressbar(main, orient = HORIZONTAL, length = 500, mode = 'determinate')
	sending_pic = PhotoImage(file=path+'\\sending.png')
	sending_label = Label(main, bg='#05081a', image=sending_pic)
	sending_label.place(x=380,y=610)
	progress.place(x=290,y=500)
	bar()

def enter_gst():
	global send_button,send_pic,r1,r2,r3,r4,r5,r1_button,r2_button,r3_button,r4_button,r5_button,cnt,variants
	cnt = 2
	share_label.place_forget()
	id_label.place_forget()
	r_id_label.place_forget()
	enter_button.place_forget()
	login.place_forget()
	password.place_forget()	
	send_pic = PhotoImage(file=path+'\\send.png')
	send_button = Button(main, bg='#05081a', image=send_pic, borderwidth=0, command=send_rate)	
	r1 = PhotoImage(file=path+'\\rate_1.png')
	r1_button = Button(main, bg='#05081a', image=r1, borderwidth=0)
	r2 = PhotoImage(file=path+'\\rate_2.png')
	r2_button = Button(main, bg='#05081a', image=r2, borderwidth=0)
	r3 = PhotoImage(file=path+'\\rate_3.png')
	r3_button = Button(main, bg='#05081a', image=r3, borderwidth=0)
	r4 = PhotoImage(file=path+'\\rate_4.png')
	r4_button = Button(main, bg='#05081a', image=r4, borderwidth=0)
	r5 = PhotoImage(file=path+'\\rate_5.png')
	r5_button = Button(main, bg='#05081a', image=r5, borderwidth=0)
	variants = ttk.Combobox(main, value=options, width=40)
	variants.current(0)
	# variants.bind('<<ComboboxSelected>>', selected)
	send_button.place(x=400,y=610)
	r1_button.place(x=100,y=450)
	r2_button.place(x=300,y=450)
	r3_button.place(x=500,y=450)
	r4_button.place(x=700,y=450)
	r5_button.place(x=900,y=450)
	variants.place(x=800,y=350)
	send_button.bind('<Enter>', hover_send_button)
	back.bind('<Enter>', hover_back)
	send_button.bind('<Leave>', hoverl_send_button)
	back.bind('<Leave>', hoverl_back)


def guest():
	global login,password,enter_button,sh_f,id_,r_id,ent_pic,bk_pic,share_label,id_label,r_id_label,enter_button,back,cnt
	cnt = 1
	admin_button.place_forget()
	guest_button.place_forget()
	ab_button.place_forget()
	sh_f = PhotoImage(file=path+'\\share.png')
	share_label = Label(main, bg='#05081a', image=sh_f)
	id_ = PhotoImage(file=path+'\\id.png')
	id_label = Label(main, bg='#05081a', image=id_)
	r_id = PhotoImage(file=path+'\\res_id.png')
	r_id_label = Label(main, bg='#05081a', image=r_id)
	ent_pic = PhotoImage(file=path+'\\enter.png')
	enter_button = Button(main, bg='#05081a', image=ent_pic, borderwidth=0, command=enter_gst)
	bk_pic = PhotoImage(file=path+'\\back.png')
	back = Button(main, bg='#05081a', image=bk_pic, borderwidth=0, command=go_back)	
	login = Entry(main, width=20, font=('Arial black',23), bg='#05081a', fg='#e1d95b')	
	login.focus()
	password = Entry(main, width=20, font=('Arial black',23), bg='#05081a', fg='#e1d95b')
	share_label.place(x=800,y=350)
	id_label.place(x=240,y=420)
	r_id_label.place(x=220,y=490)
	enter_button.place(x=400,y=600)
	back.place(x=5,y=620)
	login.place(x=340,y=420)
	password.place(x=340,y=490)
	enter_button.bind('<Enter>', hover_enter_button)
	back.bind('<Enter>', hover_back)
	enter_button.bind('<Leave>', hoverl_enter_button)
	back.bind('<Leave>', hoverl_back)
#------------------------------------------------------GUEST------------------------------------------------------------------------
#-------------------------------------------------------------ADMIN-----------------------------------------------------------------
def enter_adm():
	global newreg_pic,newreg_button,reg_pic,reg_button,guests_pic,guests_button,inv_pic,inv_button,hotst_pic,hotst_button,rinf_pic,rinf_button,fb_pic,fb_button,cnt
	cnt = 3
	id_label.place_forget()
	r_id_label.place_forget()
	enter_button.place_forget()
	login.place_forget()
	password.place_forget()
	newreg_pic = PhotoImage(file=path+'\\new_registration.png')
	newreg_button = Button(main, bg='#05081a', image=newreg_pic, borderwidth=0)	
	reg_pic = PhotoImage(file=path+'\\registrations.png')
	reg_button = Button(main, bg='#05081a', image=reg_pic, borderwidth=0)	
	guests_pic = PhotoImage(file=path+'\\guests.png')
	guests_button = Button(main, bg='#05081a', image=guests_pic, borderwidth=0)	
	inv_pic = PhotoImage(file=path+'\\invoices.png')
	inv_button = Button(main, bg='#05081a', image=inv_pic, borderwidth=0)	
	hotst_pic = PhotoImage(file=path+'\\hotel_staff.png')
	hotst_button = Button(main, bg='#05081a', image=hotst_pic, borderwidth=0)	
	rinf_pic = PhotoImage(file=path+'\\room_info.png')
	rinf_button = Button(main, bg='#05081a', image=rinf_pic, borderwidth=0)	
	fb_pic = PhotoImage(file=path+'\\feedbacks.png')
	fb_button = Button(main, bg='#05081a', image=fb_pic, borderwidth=0)	
	fb_button.place(x=430,y=400)
	newreg_button.place(x=10,y=350)
	reg_button.place(x=190,y=465)
	guests_button.place(x=300,y=645)
	inv_button.place(x=580,y=645)
	hotst_button.place(x=700,y=465)
	rinf_button.place(x=880,y=350)
	back.bind('<Enter>', hover_back)
	back.bind('<Leave>', hoverl_back)
	fb_button.bind('<Enter>', hover_fb_button)
	fb_button.bind('<Leave>', hoverl_fb_button)
	newreg_button.bind('<Enter>', hover_newreg_button)
	newreg_button.bind('<Leave>', hoverl_newreg_button)
	reg_button.bind('<Enter>', hover_reg_button)
	reg_button.bind('<Leave>', hoverl_reg_button)
	guests_button.bind('<Enter>', hover_guests_button)
	guests_button.bind('<Leave>', hoverl_guests_button)
	inv_button.bind('<Enter>', hover_inv_button)
	inv_button.bind('<Leave>', hoverl_inv_button)
	hotst_button.bind('<Enter>', hover_hotst_button)
	hotst_button.bind('<Leave>', hoverl_hotst_button)
	rinf_button.bind('<Enter>', hover_rinf_button)
	rinf_button.bind('<Leave>', hoverl_rinf_button)

def admin():
	global login,password,enter_button,id_,r_id,ent_pic,bk_pic,id_label,r_id_label,enter_button,back,cnt
	cnt = 0
	admin_button.place_forget()
	guest_button.place_forget()
	ab_button.place_forget()
	id_ = PhotoImage(file=path+'\\login.png')
	id_label = Label(main, bg='#05081a', image=id_)
	r_id = PhotoImage(file=path+'\\password.png')
	r_id_label = Label(main, bg='#05081a', image=r_id)
	ent_pic = PhotoImage(file=path+'\\enter.png')
	enter_button = Button(main, bg='#05081a', image=ent_pic, borderwidth=0, command=enter_adm)
	bk_pic = PhotoImage(file=path+'\\back.png')
	back = Button(main, bg='#05081a', image=bk_pic, borderwidth=0, command=go_back)	
	login = Entry(main, width=20, font=('Arial black',23), bg='#05081a', fg='#e1d95b')	
	login.focus()
	password = Entry(main, width=20, font=('Arial black',23), bg='#05081a', fg='#e1d95b')
	id_label.place(x=220,y=420)
	r_id_label.place(x=205,y=490)
	enter_button.place(x=400,y=600)
	back.place(x=5,y=620)
	login.place(x=340,y=420)
	password.place(x=340,y=490)
	enter_button.bind('<Enter>', hover_enter_button)
	back.bind('<Enter>', hover_back)
	enter_button.bind('<Leave>', hoverl_enter_button)
	back.bind('<Leave>', hoverl_back)
#-------------------------------------------------------------ADMIN-----------------------------------------------------------------
#---------------------------------------------------------------MAIN----------------------------------------------------------------
def build():
	global title,h_name,h_name2,admin_button,guest_button,ab_button,contacts,adm_pic,gst_pic,ab_pic,con_pic,img,img2,img3,x,z,v
	x = path+'\\welcome.png'
	img = Image.open(x)
	img = ImageTk.PhotoImage(img)
	title = Label(main, image=img, bg='#05081a')
	title.image = img
	title.place(x=350,y=20)
	z = path+'\\logo.png'
	img2 = Image.open(z)
	img2 = ImageTk.PhotoImage(img2)
	h_name = Label(main, image=img2, bg='#05081a')
	h_name.image = img2
	h_name.place(x=440,y=70)
	v = path+'\\title.png'
	img3 = Image.open(v)
	img3 = ImageTk.PhotoImage(img3)
	h_name2 = Label(main, image=img3, bg='#05081a')
	h_name2.image = img3
	h_name2.place(x=343,y=295)
	adm_pic = PhotoImage(file=path+'\\admin.png')
	admin_button = Button(main, bg='#05081a', image=adm_pic, borderwidth=0, command=admin)
	gst_pic = PhotoImage(file=path+'\\guest.png')
	guest_button = Button(main, bg='#05081a', image=gst_pic, borderwidth=0, command=guest)
	ab_pic = PhotoImage(file=path+'\\about.png')
	ab_button = Button(main, bg='#05081a', image=ab_pic, borderwidth=0, command=information)
	con_pic = PhotoImage(file=path+'\\contacts.png')
	contacts = Button(main, bg='#05081a', image=con_pic, borderwidth=0)
	admin_button.bind('<Enter>',hover_admin)
	guest_button.bind('<Enter>',hover_guest)
	ab_button.bind('<Enter>',hover_about)
	contacts.bind('<Enter>',hover_contacts)
	admin_button.bind('<Leave>',hoverl_admin)
	guest_button.bind('<Leave>',hoverl_guest)
	ab_button.bind('<Leave>',hoverl_about)
	contacts.bind('<Leave>',hoverl_contacts)
	admin_button.place(x=80,y=420)
	guest_button.place(x=700,y=420)
	ab_button.place(x=400,y=570)
	contacts.place(x=30,y=85)
#---------------------------------------------------------------MAIN----------------------------------------------------------------
build()
main.mainloop()