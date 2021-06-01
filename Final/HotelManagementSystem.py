from tkinter import *
from tkinter.ttk import Progressbar
from Parameters import *
from PIL import ImageTk, Image
import os
from datetime import *
from tkinter.ttk import Combobox
import pyodbc
from tkinter import messagebox
from datetime import datetime
from threading import Timer
from tkinter.ttk import Radiobutton  
from tkinter.ttk import Checkbutton
path = str(os.path.dirname(os.path.abspath(__file__)))
main = Tk()
main.geometry('1080x700')
main.iconbitmap(path+'\\logo.ico')
main.configure(bg='#05081a')
main.title('Veyron Sky')

subWindowOpened = False

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=LEGION;"
    "Database=hotel;"
    "Trusted_Connection=yes")
cursor = conn.cursor()
cursorTwo = conn.cursor()
cursorThree = conn.cursor()
cursor1 = conn.cursor()
cursor2 = conn.cursor()
cursor3 = conn.cursor()
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

def hover_r1_button(event):
	global r1
	r1 = PhotoImage(file=path+'\\rate_1_hover.png')
	r1_button['image'] = r1

def hoverl_r1_button(event):
	global r1
	r1 = PhotoImage(file=path+'\\rate_1.png')
	r1_button['image'] = r1

def hover_r2_button(event):
	global r2
	r2 = PhotoImage(file=path+'\\rate_2_hover.png')
	r2_button['image'] = r2

def hoverl_r2_button(event):
	global r2
	r2 = PhotoImage(file=path+'\\rate_2.png')
	r2_button['image'] = r2

def hover_r3_button(event):
	global r3
	r3 = PhotoImage(file=path+'\\rate_3_hover.png')
	r3_button['image'] = r3

def hoverl_r3_button(event):
	global r3
	r3 = PhotoImage(file=path+'\\rate_3.png')
	r3_button['image'] = r3

def hover_r4_button(event):
	global r4
	r4 = PhotoImage(file=path+'\\rate_4_hover.png')
	r4_button['image'] = r4

def hoverl_r4_button(event):
	global r4
	r4 = PhotoImage(file=path+'\\rate_4.png')
	r4_button['image'] = r4

def hover_r5_button(event):
	global r5
	r5 = PhotoImage(file=path+'\\rate_5_hover.png')
	r5_button['image'] = r5

def hoverl_r5_button(event):
	global r5
	r5 = PhotoImage(file=path+'\\rate_5.png')
	r5_button['image'] = r5

def hover_int_lbl(event):
	global int_pic
	int_pic = PhotoImage(file=path+'\\interface_hover.png')
	int_lbl['image'] = int_pic

def hoverl_int_lbl(event):
	global int_pic
	int_pic = PhotoImage(file=path+'\\interface.png')
	int_lbl['image'] = int_pic

def hover_proc_lbl(event):
	global proc_pic
	proc_pic = PhotoImage(file=path+'\\pft_hover.png')
	proc_lbl['image'] = proc_pic

def hoverl_proc_lbl(event):
	global proc_pic
	proc_pic = PhotoImage(file=path+'\\pft.png')
	proc_lbl['image'] = proc_pic

def hover_erd_lbl(event):
	global erd_pic
	erd_pic = PhotoImage(file=path+'\\erd_norm_hover.png')
	erd_lbl['image'] = erd_pic

def hoverl_erd_lbl(event):
	global erd_pic
	erd_pic = PhotoImage(file=path+'\\erd_norm.png')
	erd_lbl['image'] = erd_pic
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
		enter_button.place_forget()
		back.place_forget()
		login.place_forget()
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
		pass
	if cnt==4:
		int_lbl.place_forget()
		proc_lbl.place_forget()
		erd_lbl.place_forget()
		back.place_forget()
		build()

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
#-----------------------------------------------------ABOUT------------------------------------------------------------------------
def information():
	global cnt,int_pic,int_lbl,proc_pic,proc_lbl,erd_pic,erd_lbl,bk_pic,back
	cnt = 4
	admin_button.place_forget()
	guest_button.place_forget()
	ab_button.place_forget()
	int_pic = PhotoImage(file=path+'\\interface.png')
	int_lbl = Label(main, bg='#05081a', image=int_pic)
	proc_pic = PhotoImage(file=path+'\\pft.png')
	proc_lbl = Label(main, bg='#05081a', image=proc_pic)
	erd_pic = PhotoImage(file=path+'\\erd_norm.png')
	erd_lbl = Label(main, bg='#05081a', image=erd_pic)
	bk_pic = PhotoImage(file=path+'\\back.png')
	back = Button(main, bg='#05081a', image=bk_pic, borderwidth=0, command=go_back)
	int_lbl.place(x=10,y=370)
	proc_lbl.place(x=380,y=400)
	erd_lbl.place(x=750,y=400)
	back.place(x=5,y=620)
	back.bind('<Enter>', hover_back)
	back.bind('<Leave>', hoverl_back)
	int_lbl.bind('<Enter>', hover_int_lbl)
	int_lbl.bind('<Leave>', hoverl_int_lbl)
	proc_lbl.bind('<Enter>', hover_proc_lbl)
	proc_lbl.bind('<Leave>', hoverl_proc_lbl)
	erd_lbl.bind('<Enter>', hover_erd_lbl)
	erd_lbl.bind('<Leave>', hoverl_erd_lbl)
#-----------------------------------------------------ABOUT------------------------------------------------------------------------
#------------------------------------------------------GUEST-----------------------------------------------------------------------


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
	back.place_forget()
	variants.place_forget()
	progress = Progressbar(main, orient = HORIZONTAL, length = 500, mode = 'determinate')
	sending_pic = PhotoImage(file=path+'\\sending.png')
	sending_label = Label(main, bg='#05081a', image=sending_pic)
	sending_label.place(x=380,y=610)
	progress.place(x=290,y=500)
	bar()

def r1p():
	feedback = 1
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()
	cursor.execute('insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values(getdate());')

def r1p():
	feedback = 1
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()
	cursor.execute(f'insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values({feedback},{feedback},{feedback},{feedback},{feedback},{feedback});')

def r2p():
	feedback = 2
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()
	cursor.execute(f'insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values({feedback},{feedback},{feedback},{feedback},{feedback},{feedback});')

def r3p():
	feedback = 3
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()	
	cursor.execute(f'insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values({feedback},{feedback},{feedback},{feedback},{feedback},{feedback});')

def r4p():
	feedback = 4
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()		
	cursor.execute(f'insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values({feedback},{feedback},{feedback},{feedback},{feedback},{feedback});')

def r5p():
	feedback = 5
	r1_button.destroy()
	r2_button.destroy()
	r3_button.destroy()
	r4_button.destroy()
	r5_button.destroy()
	cursor.execute(f'insert into Rating(rating_id, rating_guest_id, rating_reservation_id, rating_room, rating_spa, rating_date) values({feedback},{feedback},{feedback},{feedback},{feedback},{feedback});')

def again():
	r1 = PhotoImage(file=path+'\\rate_1.png')
	r1_button = Button(main, bg='#05081a', image=r1, borderwidth=0, command=r1p)
	r2 = PhotoImage(file=path+'\\rate_2.png')
	r2_button = Button(main, bg='#05081a', image=r2, borderwidth=0, command=r2p)
	r3 = PhotoImage(file=path+'\\rate_3.png')
	r3_button = Button(main, bg='#05081a', image=r3, borderwidth=0, command=r3p)
	r4 = PhotoImage(file=path+'\\rate_4.png')
	r4_button = Button(main, bg='#05081a', image=r4, borderwidth=0, command=r4p)
	r5 = PhotoImage(file=path+'\\rate_5.png')
	r5_button = Button(main, bg='#05081a', image=r5, borderwidth=0, command=r5p)
	r1_button.place(x=100,y=450)
	r2_button.place(x=300,y=450)
	r3_button.place(x=500,y=450)
	r4_button.place(x=700,y=450)
	r5_button.place(x=900,y=450)
	r1_button.bind('<Enter>',hover_r1_button)
	r2_button.bind('<Enter>',hover_r2_button)
	r3_button.bind('<Enter>',hover_r3_button)
	r4_button.bind('<Enter>',hover_r4_button)
	r5_button.bind('<Enter>',hover_r5_button)
	r1_button.bind('<Leave>',hoverl_r1_button)
	r2_button.bind('<Leave>',hoverl_r2_button)
	r3_button.bind('<Leave>',hoverl_r3_button)
	r4_button.bind('<Leave>',hoverl_r4_button)
	r5_button.bind('<Leave>',hoverl_r5_button)

def enter_gst():
	global send_button,send_pic,r1,r2,r3,r4,r5,r1_button,r2_button,r3_button,r4_button,r5_button,cnt,variants,login
	if login.get() in g_ids:
		cnt = 2
		share_label.place_forget()
		id_label.place_forget()
		enter_button.place_forget()
		login.place_forget()	
		send_pic = PhotoImage(file=path+'\\send.png')
		send_button = Button(main, bg='#05081a', image=send_pic, borderwidth=0, command=send_rate)	
		r1 = PhotoImage(file=path+'\\rate_1.png')
		r1_button = Button(main, bg='#05081a', image=r1, borderwidth=0, command=r1p)
		r2 = PhotoImage(file=path+'\\rate_2.png')
		r2_button = Button(main, bg='#05081a', image=r2, borderwidth=0, command=r2p)
		r3 = PhotoImage(file=path+'\\rate_3.png')
		r3_button = Button(main, bg='#05081a', image=r3, borderwidth=0, command=r3p)
		r4 = PhotoImage(file=path+'\\rate_4.png')
		r4_button = Button(main, bg='#05081a', image=r4, borderwidth=0, command=r4p)
		r5 = PhotoImage(file=path+'\\rate_5.png')
		r5_button = Button(main, bg='#05081a', image=r5, borderwidth=0, command=r5p)
		variants = Combobox(main, value=options, width=40)
		variants.current(0)
		send_button.place(x=400,y=610)
		r1_button.place(x=100,y=450)
		r2_button.place(x=300,y=450)
		r3_button.place(x=500,y=450)
		r4_button.place(x=700,y=450)
		r5_button.place(x=900,y=450)
		variants.place(x=800,y=350)
		send_button.bind('<Enter>', hover_send_button)
		back.bind('<Enter>', hover_back)
		r1_button.bind('<Enter>',hover_r1_button)
		r2_button.bind('<Enter>',hover_r2_button)
		r3_button.bind('<Enter>',hover_r3_button)
		r4_button.bind('<Enter>',hover_r4_button)
		r5_button.bind('<Enter>',hover_r5_button)
		send_button.bind('<Leave>', hoverl_send_button)
		back.bind('<Leave>', hoverl_back)
		r1_button.bind('<Leave>',hoverl_r1_button)
		r2_button.bind('<Leave>',hoverl_r2_button)
		r3_button.bind('<Leave>',hoverl_r3_button)
		r4_button.bind('<Leave>',hoverl_r4_button)
		r5_button.bind('<Leave>',hoverl_r5_button)
	else:
		messagebox.showerror('Error','Incorrect guest id')

def guest():
	global login,enter_button,sh_f,id_,ent_pic,bk_pic,share_label,id_label,enter_button,back,cnt
	cnt = 1
	admin_button.place_forget()
	guest_button.place_forget()
	ab_button.place_forget()
	sh_f = PhotoImage(file=path+'\\share.png')
	share_label = Label(main, bg='#05081a', image=sh_f)
	id_ = PhotoImage(file=path+'\\id.png')
	id_label = Label(main, bg='#05081a', image=id_)
	ent_pic = PhotoImage(file=path+'\\enter.png')
	enter_button = Button(main, bg='#05081a', image=ent_pic, borderwidth=0, command=enter_gst)
	bk_pic = PhotoImage(file=path+'\\back.png')
	back = Button(main, bg='#05081a', image=bk_pic, borderwidth=0, command=go_back)	
	login = Entry(main, width=20, font=('Arial black',23), bg='#05081a', fg='#e1d95b')	
	login.focus()
	share_label.place(x=800,y=350)
	id_label.place(x=240,y=450)
	enter_button.place(x=400,y=600)
	back.place(x=5,y=620)
	login.place(x=340,y=450)
	enter_button.bind('<Enter>', hover_enter_button)
	back.bind('<Enter>', hover_back)
	enter_button.bind('<Leave>', hoverl_enter_button)
	back.bind('<Leave>', hoverl_back)
#------------------------------------------------------GUEST------------------------------------------------------------------------
#-------------------------------------------------------------ADMIN-----------------------------------------------------------------
def spa_invoice():
    global chk_state1, chk_state2, spin1, spin2, res_id_input, guest_id_input, staff_id_input, payment_type_input, window, firm_id, firm_title
    window = Tk()
    window.title("Veyron Sky: SPA")
    window.configure(bg=bg_color)
    window.geometry(f'{w}x{h}')
    firm_title = "Spa Services"
    firm_id = 'SPA1'
    vs_txt = Label(window, bg=bg_color, fg='black', text = f"Veyron Sky", font=font_head) 
    table_txt = Label(window, bg=bg_color, fg='black', text = f"{firm_title}", font=font_txt) 
    show_table_btn = Button(window, text=f"Show {firm_title}", command=view_firm_services_table)
    show_invoice_btn = Button(window, text="Show invoices", command=show_invoices_btn)
    show_f_staff_btn = Button(window, text="Show firm staff", command=show_firm_staff_btn)
    chk_state1 = IntVar()
    chk_state2 = IntVar()
    chk_state1.set(0)
    chk_state2.set(0)
    spin1 = IntVar()
    spin2 = IntVar()
    serv1 = Checkbutton(window, text='facial', variable=chk_state1) 
    spin1 = Spinbox(window, from_=1, to=100, width=5)
    serv2 = Checkbutton(window, text='massage', variable=chk_state2) 
    spin2 = Spinbox(window, from_=1, to=100, width=5)
    res_id_txt = Label(window, bg=bg_color, fg='black', text = f"Reservation ID:", font=font_txt)
    res_id_input = Entry(window) 
    guest_id_txt = Label(window, bg=bg_color, fg='black', text = f"Guest ID:", font=font_txt)
    guest_id_input = Entry(window) 
    staff_id_txt = Label(window, bg=bg_color, fg='black', text = f"Staff ID:", font=font_txt)
    staff_id_input = Entry(window) 
    payment_type_txt = Label(window, bg=bg_color, fg='black', text = f"Payment type:", font=font_txt)
    payment_type_input = Entry(window) 
    invoice_btn = Button(window, text="Create invoice", command=new_invoice_btn)
    table_txt.pack()
    show_table_btn.pack()
    show_invoice_btn.pack()
    show_f_staff_btn.pack()
    serv1.pack()
    spin1.pack()
    serv2.pack()
    spin2.pack()
    res_id_txt.pack()
    res_id_input.pack()
    guest_id_txt.pack()
    guest_id_input.pack()
    staff_id_txt.pack()
    staff_id_input.pack()
    payment_type_txt.pack()
    payment_type_input.pack()
    invoice_btn.pack()
    window.mainloop()
    
def gym_invoice():
    global chk_state1, chk_state2, chk_state3, spin1, spin2, spin3, res_id_input, guest_id_input, staff_id_input, payment_type_input, window, firm_id, firm_title
    window = Tk()
    window.title("Veyron Sky: Gym")
    window.configure(bg=bg_color)
    h = 540
    w = 1080
    window.geometry(f'{w}x{h}')
    firm_title = "Hotel Services"
    firm_id = 'G1'
    vs_txt = Label(window, bg=bg_color, fg='black', text = f"Veyron Sky", font=font_head)
    table_txt = Label(window, bg=bg_color, fg='black', text = f"{firm_title}", font=font_txt)
    show_table_btn = Button(window, text=f"Show {firm_title}", command=view_firm_services_table)
    show_invoice_btn = Button(window, text="Show invoices", command=show_invoices_btn)
    show_f_staff_btn = Button(window, text="Show firm staff", command=show_firm_staff_btn)
    chk_state1 = IntVar()
    chk_state2 = IntVar()
    chk_state3 = IntVar()
    chk_state1.set(0)
    chk_state2.set(0)
    chk_state3.set(0)
    spin1 = IntVar()
    spin2 = IntVar()
    spin3 = IntVar()
    serv1 = Checkbutton(window, text='standard', variable=chk_state1) 
    spin1 = Spinbox(window, from_=1, to=100, width=5)
    serv2 = Checkbutton(window, text='silver', variable=chk_state2) 
    spin2 = Spinbox(window, from_=1, to=100, width=5)
    serv3 = Checkbutton(window, text='gold', variable=chk_state3) 
    spin3 = Spinbox(window, from_=1, to=100, width=5)
    res_id_txt = Label(window, bg=bg_color, fg='black', text = f"Reservation ID:", font=font_txt)
    res_id_input = Entry(window) 
    guest_id_txt = Label(window, bg=bg_color, fg='black', text = f"Guest ID:", font=font_txt)
    guest_id_input = Entry(window) 
    staff_id_txt = Label(window, bg=bg_color, fg='black', text = f"Staff ID:", font=font_txt)
    staff_id_input = Entry(window) 
    payment_type_txt = Label(window, bg=bg_color, fg='black', text = f"Payment type:", font=font_txt)
    payment_type_input = Entry(window) 
    invoice_btn = Button(window, text="Create invoice", command=new_invoice_btn)
    table_txt.pack()
    show_table_btn.pack()
    show_invoice_btn.pack()
    show_f_staff_btn.pack()
    serv1.pack()
    spin1.pack()
    serv2.pack()
    spin2.pack()
    serv3.pack()
    spin3.pack()
    res_id_txt.pack()
    res_id_input.pack()
    guest_id_txt.pack()
    guest_id_input.pack()
    staff_id_txt.pack()
    staff_id_input.pack()
    payment_type_txt.pack()
    payment_type_input.pack()
    invoice_btn.pack()
    window.mainloop()
    
def hotel_invoice():
    global spin, res_id_input, guest_id_input, staff_id_input, serv_input, window, firm_id, firm_title
    window = Tk()
    window.title("New Invoice")
    window.configure(bg=bg_color)
    window.geometry(f'{w}x{h}')
    firm_title = "Hotel Services"
    firm_id = 'H'
    #vs_txt = Label(window, bg=bg_color, fg='black', text = f"Veyron Sky", font=font_head) 
    #table_txt = Label(window, bg=bg_color, fg='black', text = f"{firm_title}", font=font_txt) 
    show_table_btn = Button(window, text=f"Show {firm_title}", command=view_firm_services_table)
    show_invoice_btn = Button(window, text="Show invoices", command=show_h_invoices_btn)
    show_f_staff_btn = Button(window, text="Show hoel staff", command=show_hotel_staff_btn)
    spin = IntVar()
    serv_input = Combobox(window)  
    serv_input['values'] = ('minibar', 'laundry')  
    serv_input.current(0)
    spin = Spinbox(window, from_=1, to=100, width=5)
    res_id_txt = Label(window, bg=bg_color, fg='black', text = f"Reservation ID:", font=font_txt)
    res_id_input = Entry(window) 
    guest_id_txt = Label(window, bg=bg_color, fg='black', text = f"Guest ID:", font=font_txt)
    guest_id_input = Entry(window) 
    staff_id_txt = Label(window, bg=bg_color, fg='black', text = f"Staff ID:", font=font_txt)
    staff_id_input = Entry(window)
    invoice_btn = Button(window, text="Create invoice", command=new_invoice_btn)
    #table_txt.pack()
    show_table_btn.pack()
    show_invoice_btn.pack()
    show_f_staff_btn.pack()
    serv_input.pack()
    spin.pack()
    res_id_txt.pack()
    res_id_input.pack()
    guest_id_txt.pack()
    guest_id_input.pack()
    staff_id_txt.pack()
    staff_id_input.pack()
    invoice_btn.pack()
    button3 = Button(window, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=window.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    window.mainloop()
    
def room_info():
    global room_info_win, room_type_input, day_cost_input
    room_info_win = Tk()
    room_info_win.title("Veyron Sky: Room Info")
    room_info_win.configure(bg=bg_color)
    room_info_win.geometry(f'{w}x{h}')
    vs_txt = Label(room_info_win, bg=bg_color, fg='black', text = f"Veyron Sky", font=font_head) 
    table_txt = Label(room_info_win, bg=bg_color, fg='black', text = f"Room type information", font=font_txt)
    room_type_btn = Button(room_info_win, text="Show room type", command=show_room_type)
    room_type_txt = Label(room_info_win, bg=bg_color, fg='black', text = f"Room type:", font=font_txt)
    room_type_input = Combobox(room_info_win)  
    room_type_input['values'] = ('single', 'double', 'family', 'president')  
    room_type_input.current(0)
    day_cost_txt = Label(room_info_win, bg=bg_color, fg='black', text = f"Day cost:", font=font_txt)
    day_cost_input = Entry(room_info_win)
    change_btn = Button(room_info_win, text="Change cost", command=change_cost_btn)
    table_txt.pack()
    room_type_btn.pack()
    room_type_txt.pack()
    room_type_input.pack()
    day_cost_txt.pack()
    day_cost_input.pack()
    change_btn.pack()
    button3 = Button(room_info_win, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=room_info_win.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    room_info_win.mainloop()
    
def show_room_type():
    global room_type_win
    room_type_win = Tk()
    room_type_win.title(f"Room Type")
    room_type_win.configure(bg=bg_color)
    count = 0
    cursor.execute("select count(*) from room_type");
    for row in cursor:
        count = row[0]
    list = cursor.execute("select * from room_type");
    e=Label(room_type_win,width=20,text='Room type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(room_type_win,width=20,text='Bed number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(room_type_win,width=20,text='Max capacity',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(room_type_win,width=20,text='Balcony number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(room_type_win,width=20,text='Inventory quality',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(room_type_win,width=20,text='Day cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    i=1
    for room in list:
        for j in range(6):
            e = Entry(room_type_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
    room_type_win.mainloop()

def change_cost_btn():
    if day_cost_input.get() == '':
        messagebox.showerror('Error', '''You didn't set a price''')
        return
    cursor.execute(f'''
        exec ChangeRoomTypeDayCost @room_type = '{room_type_input.get()}', @cost = {day_cost_input.get()};
    ''')
    messagebox.showinfo('ChangeDayCost', f'The cost for {room_type_input.get()} room was successfully changed!')
    if (room_type_win.winfo_exists() == 1):
        exit(room_type_win)
        show_room_type()

def new_invoice_btn():
    r = defineInput(res_id_input.get())
    g = defineInput(guest_id_input.get())
    st = defineInput(staff_id_input.get())
    if firm_id == 'H':
        ser = defineInput(serv_input.get())
        if (ser == 'minibar'):
            s1 = 6
        if (ser == 'laundry'):
            s1 = 7  
        sp = defineInput(spin.get())
        cursor.execute(f'''
            exec Calculate_hotel_invoice @reservation_id = {r}, @guest_id = {g}, @hotel_staff_id = {st},  @hotel_id = 'H', @service_id = '{s1}', @quantity = '{sp}';
        ''')
    if firm_id == 'SPA1':
        p = defineInput(payment_type_input.get())
        sp1 = defineInput(spin1.get())
        sp2 = defineInput(spin2.get())
        if (chk_state1.get() == 1):
            s1 = 1
        else:
            s1 = ''
            sp1 = ''
        if (chk_state2.get() == 1):
            s2 = 2
        else:
            s2 = ''
            sp2 = ''
        cursor.execute(f'''
            exec Calculate_firm_invoice @reservation_id = {r}, @guest_id = {g}, @firm_staff_id = {st}, @payment_type = '{p}', @firm_id = '{firm_id}', @service_ids = '{s1} {s2} {s3}', @quantitys = '{sp1} {sp2} {sp3}';
        ''')
    elif firm_id == 'G1':
        p = defineInput(payment_type_input.get())
        sp1 = defineInput(spin1.get())
        sp2 = defineInput(spin2.get())
        sp3 = defineInput(spin2.get())
        if (chk_state1.get() == 1):
            s1 = 3
        else:
            s1 = ''
            sp1 = ''
        if (chk_state2.get() == 1):
            s2 = 4
        else:
            s2 = ''
            sp2 = ''
        if (chk_state3.get() == 1):
            s3 = 5
        else:
            s3 = ''
            sp3 = ''
        cursor.execute(f'''
            exec Calculate_firm_invoice @reservation_id = {r}, @guest_id = {g}, @firm_staff_id = {st}, @payment_type = '{p}', @firm_id = '{firm_id}', @service_ids = '{s1} {s2} {s3}', @quantitys = '{sp1} {sp2} {sp3}';
        ''')
        
    isOkay = True
    for l in cursor:
        l = list(l)
        result = str(l[0])
        if('Sorry' in result):
            messagebox.showerror('Error',result)
            isOkay = False
            return
        
    
    if isOkay == True and (firm_id == 'G1' or firm_id == 'SPA1'):
        cursor.execute(f'''
            select * from totalinvoice;
        ''')
        text = ''
        for l in cursor:
            l = list(l)
            result = str(l[0])
        result = result.replace('@', '\n')
    
    if (invoice_win.winfo_exists() == 1):
        exit(invoice_win)
        if (firm_id == 'H'):
            show_h_invoices_btn()
        else:
            show_invoices_btn()
    
def total_hotel_invoice_info():
    cursor.execute(f'''
            select * from total_h_invoice;
    ''')
    text = ''
    for l in cursor:
        l = list(l)
        result = str(l[0])
    result = result.replace('@', '\n')
    print(result)
    window = Tk()
    window.title("Total Hotel Invoice")
    window.configure(bg=bg_color)
    view_txt = Label(window, bg=bg_color, fg='black', text=result, font=font_txt) 
    view_txt.pack()
    window.mainloop()

def defineInput(variable):
    if(variable == '' or variable == ' '):
        return 'NULL'
    else:
        return variable

def show_invoices_btn():
    global invoice_win
    invoice_win = Tk()
    invoice_win.title(f"{firm_title} Invoices")
    invoice_win.configure(bg=bg_color)
    count = 0
    cursor.execute(f"select count(*) from Firm_Invoice where firm_id = '{firm_id}'")
    for row in cursor:
        count = row[0]
    list = cursor.execute(f"select * from Firm_Invoice where firm_id = '{firm_id}'");
    e=Label(invoice_win,width=20,text='firm_invoice_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(invoice_win,width=20,text='reservation_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(invoice_win,width=20,text='guest_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(invoice_win,width=20,text='staff_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(invoice_win,width=20,text='total_cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(invoice_win,width=20,text='invoice_date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(invoice_win,width=20,text='payment_type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(invoice_win,width=20,text='firm_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    i=1
    for room in list:
        for j in range(8):
            e = Entry(invoice_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
        
    print(count) 
    i = count + 1
    count = 0
    cursor.execute(f"select count(*) from service_detail where firm_id = '{firm_id}'");
    for row in cursor:
        count = row[0]
    list = cursor.execute(f"select * from service_firm_invoice where f_invoice_id in (select firm_invoice_id from Firm_Invoice where firm_id = '{firm_id}');");
    e=Label(invoice_win,width=20,text='firm_invoice_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=0)
    e=Label(invoice_win,width=20,text='service_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=1)
    e=Label(invoice_win,width=20,text='quantity',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=2)
    i = i + 1
    for room in list:
        for j in range(3):
            e = Entry(invoice_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1   
    invoice_win.mainloop()
    
def show_h_invoices_btn():
    global invoice_win 
    invoice_win = Tk()
    invoice_win.title(f"{firm_title} Invoices")
    invoice_win.configure(bg=bg_color)
    count = 0
    cursor.execute("select count(*) from hotel_Invoice")
    for row in cursor:
        count = row[0]
    list = cursor.execute("select * from hotel_Invoice");
    e=Label(invoice_win,width=20,text='hotel_invoice_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(invoice_win,width=20,text='reservation_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(invoice_win,width=20,text='guest_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(invoice_win,width=20,text='staff_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(invoice_win,width=20,text='total_cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(invoice_win,width=20,text='invoice_date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(invoice_win,width=20,text='invoice_status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(invoice_win,width=20,text='hotel_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    i=1
    for room in list:
        for j in range(8):
            e = Entry(invoice_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
        
    print(count) 
    i = count + 1
    count = 0
    cursor.execute(f"select count(*) from service_detail where firm_id = '{firm_id}'")
    for row in cursor:
        count = row[0]
    list = cursor.execute(f"select * from service_hotel_invoice where h_invoice_id in (select hotel_invoice_id from hotel_Invoice where hotel_id = '{firm_id}');")
    e=Label(invoice_win,width=20,text='hotel_invoice_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=0)
    e=Label(invoice_win,width=20,text='service_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=1)
    e=Label(invoice_win,width=20,text='quantity',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i,column=2)
    i = i + 1
    for room in list:
        for j in range(3):
            e = Entry(invoice_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1   
    invoice_win.mainloop()
    
def view_firm_services_table():
    firm_serv_win = Tk()
    firm_serv_win.title(firm_title)
    firm_serv_win.configure(bg=bg_color)
    count = 0
    if (firm_id == 'H'):
        cursor.execute(f"select count(*) from service_detail where firm_id = '{firm_id}' and service_title != 'accommodation'")
    else:
        cursor.execute(f"select count(*) from service_detail where firm_id = '{firm_id}'")
    for row in cursor:
        count = row[0]
    if (firm_id == 'H'):
        list = cursor.execute(f"select service_id, service_title, cost from service_detail where firm_id = '{firm_id}' and service_title != 'accommodation'");
    else:
        list = cursor.execute(f"select service_id, service_title, cost from service_detail where firm_id = '{firm_id}'");
    e=Label(firm_serv_win,width=20,text='Service ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(firm_serv_win,width=20,text='Service title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(firm_serv_win,width=20,text='Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    i=1
    for room in list:
        for j in range(3):
            e = Entry(firm_serv_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
    firm_serv_win.mainloop()
    
def show_firm_staff_btn():
    firm_staff_win = Tk()
    firm_staff_win.title(firm_title)
    firm_staff_win.configure(bg=bg_color)
    count = 0
    cursor.execute(f"select count(*) from firm_staff where firm_id = '{firm_id}'");
    for row in cursor:
        count = row[0]
    list = cursor.execute(f"select firm_staff_id, firm_staff_name, firm_staff_surname, firm_staff_job_title, firm_id from firm_staff where firm_id = '{firm_id}'");
    e=Label(firm_staff_win,width=20,text='firm_staff_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(firm_staff_win,width=20,text='name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(firm_staff_win,width=20,text='surname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(firm_staff_win,width=20,text='job_title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(firm_staff_win,width=20,text='firm_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    i=1
    for room in list:
        for j in range(5):
            e = Entry(firm_staff_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
    firm_staff_win.mainloop()
    
def show_hotel_staff_btn():
    hotel_staff_win = Tk()
    hotel_staff_win.title(firm_title)
    hotel_staff_win.configure(bg=bg_color)
    count = 0
    cursor.execute(f"select count(*) from hotel_staff where hotel_staff_department_id = 222");
    for row in cursor:
        count = row[0]
    list = cursor.execute(f"select hotel_staff_id, hotel_staff_name, hotel_staff_surname, hotel_staff_job_title from hotel_staff where hotel_staff_department_id = 222");
    e=Label(hotel_staff_win,width=20,text='hotel_staff_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(hotel_staff_win,width=20,text='name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(hotel_staff_win,width=20,text='surname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(hotel_staff_win,width=20,text='job_title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    i=1
    for room in list:
        for j in range(4):
            e = Entry(hotel_staff_win, width=23, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
    hotel_staff_win.mainloop()


# In[61]:


def exit():
    main.quit()

def hotelManagerWin():
    hotelManager = Tk()
    hotelManager.title('Veyron Sky: Hotel Manager')
    hotelManager.geometry(f'{w}x{h}')
    hotelManager.configure(bg=bg_color)
    label0 = Label(hotelManager, text='Welcome Hotel Manager', height=10, width=150, bg=bg_color, fg='black', font=("Noto Sans JP", 13, 'bold'))
    label0.place(x = 20, y = 30, width=300, height=20)
    button1 = Button(hotelManager, text='Registrations', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=reservationWin)
    button1.place(x = 20, y = 100, width=120, height=50)
    button3 = Button(hotelManager, text='Guests', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=showGuests)
    button3.place(x = 20, y = 150, width=120, height=50)
    button4 = Button(hotelManager, text='Invoices', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=showHotelInvoices)
    button4.place(x = 20, y = 2000, width=120, height=50)
    button5 = Button(hotelManager, text='Hotel Staff', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=showHotelStaff)
    button5.place(x = 200, y = 100, width=120, height=50)
    button6 = Button(hotelManager, text='Room Info', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=room_info)
    button6.place(x = 200, y = 150, width=120, height=50)
    button7 = Button(hotelManager, text='Feedbacks', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command =showRating)
    button7.place(x = 200, y = 200, width=120, height=50)
    hotelManager.mainloop()
    
def showGuests():
    guestTable = Tk()
    guestTable.title('Veyron Sky: Hotel Manager')
    guestTable.geometry('1500x700')
    guestTable.configure(bg=bg_color)
    list = cursor.execute("select * from Guest");
    e=Label(guestTable,width=20,text='ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(guestTable,width=20,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(guestTable,width=20,text='Surname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(guestTable,width=20,text='Address',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(guestTable,width=20,text='Birthday',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(guestTable,width=20,text='Family Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(guestTable,width=20,text='Phone Number',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(guestTable,width=20,text='Email',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    e=Label(guestTable,width=20,text='Gender',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=8)
    i=1
    for guest in list:
        for j in range(9):
            e = Entry(guestTable, width=24, fg='blue') 
            e.grid(row=i, column=j)
            if guest[j] is None:
                e.insert(END, 'null')
            else:
                e.insert(END, guest[j])
        i=i+1
    button3 = Button(guestTable, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=guestTable.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    guestTable.mainloop()
    
def showHotelStaff():
    def addNewHotelStaffWin():
        dict1 = {"Receptionist":111, "Cleaner":222, "Guard":333, "DBA":666, "Hotel Manager":999, "Cleaner Manager":999}
        def insertNewStaff():
            cursor.execute("select * from hotel_staff where hotel_staff_id = '%s'" % (hotel_staff_id.get()))
            existName = ''
            for row in cursor:
                existName = row[0]
            if existName == '' or len(existName.strip()) == 0:
                if len(hotel_staff_name.get()) == 0 or len(hotel_staff_surname.get())==0 or len(hotel_staff_phone.get()) == 0 or len(hotel_staff_join_date.get())==0 or len(hotel_staff_work_floor.get())==0 or len(hotel_staff_work_floor.get())==0 or len(hotel_staff_prev_workplace.get()) == 0 or len(hotel_staff_prev_job.get())==0 or len(hotel_staff_job_exp.get())==0 or len(hotel_staff_birthday.get())==0 or len(hotel_staff_start_time.get())==0 or len(hotel_staff_end_time.get())==0 or len(hotel_staff_salary.get())==0:
                    messagebox.showerror('Error', 'Some fields cannot be empty')
                    newHotelStaff.destroy()
                    hotelStaff.destroy()
                    showHotelStaff()
                else:
                    if isdate(hotel_staff_birthday.get()) and isdate(hotel_staff_join_date.get()):
                        cursor.execute("INSERT INTO hotel_staff VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s' ,'%s', '%s' ,'%s', '%s','%s', '%s','%s', '%s','%s', '%s')" % (hotel_staff_id.get(), hotel_staff_name.get(), hotel_staff_surname.get(), dict1.get(hotel_staff_job_title.get()), hotel_staff_job_title.get(), 
                                                                                                                                                                                                hotel_staff_email.get(), hotel_staff_phone.get(), hotel_staff_address.get(), hotel_staff_join_date.get(), 
                                                                                                                                                                                                hotel_staff_work_floor.get(), hotel_staff_gender.get(), hotel_staff_prev_job.get(), hotel_staff_prev_workplace.get(), 
                                                                                                                                                                                                hotel_staff_job_exp.get(), hotel_staff_edu_lvl.get(), hotel_staff_speciality.get(), hotel_staff_birthday.get(), hotel_staff_start_time.get(), 
                                                                                                                                                                                                hotel_staff_end_time.get(), hotel_staff_salary.get()))
                        cursor.execute("select hotel_staff_id from hotel_staff where hotel_staff_id = '%s'" % defineInput(hotel_staff_id.get()))
                        for row in cursor:
                            existName = row[0]
                        if existName == '' or len(existName.strip()) == 0:
                            messagebox.showwarning('Warning', 'Newly inserted hotel staff with ID ' + str(hotel_staff_id.get()) + ' was deleted from database due to definite requirements. For more information look to the Former Staff table')
                        else:
                            messagebox.showinfo('Success', 'Newly inserted hotel staff with ID ' + str(hotel_staff_id.get()) + ' was inserted into Hotel Staff table')
                        conn.commit()
                        newHotelStaff.destroy()
                        hotelStaff.destroy()
                        showHotelStaff()
                    else:
                        messagebox.showerror('Error', 'There is a mistake in dates!')
                        newHotelStaff.destroy()
                        hotelStaff.destroy()
            else:
                messagebox.showerror('Error', 'There is already existing hotel staff with given ID')
                newHotelStaff.destroy()
                hotelStaff.destroy()
        newHotelStaff = Tk()
        newHotelStaff.title('Veyron Sky: Hotel Manager')
        newHotelStaff.geometry(f'{w}x{h}')
        newHotelStaff.configure(bg=bg_color)
        label0 = Label(newHotelStaff, text='Enter information about new hotel Staff', height=10, width=300, bg=bg_color, fg='black', font=("Noto Sans JP", 11, 'bold'))
        label0.place(x = 80, y = 30, width=300, height=20)
        hotel_staff_id = Label(newHotelStaff, text = 'Staff ID', height=10, width=220, bg=bg_color)
        hotel_staff_id.place(x = 80, y = 60, height = 20, width = 220)
        hotel_staff_id = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_id.place(x = 280, y = 60, height = 20, width = 220)
        hotel_staff_name = Label(newHotelStaff, text = 'Staff Name', height=10, width=220, bg=bg_color)
        hotel_staff_name.place(x = 80, y = 90, height = 20, width = 220)
        hotel_staff_name = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_name.place(x = 280, y = 90, height = 20, width = 220)
        hotel_staff_surname = Label(newHotelStaff, text = 'Staff Surname', height=10, width=220, bg=bg_color)
        hotel_staff_surname.place(x = 80, y = 120, height = 20, width = 220)
        hotel_staff_surname = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_surname.place(x = 280, y = 120, height = 20, width = 220)
        hotel_staff_job_title = Label(newHotelStaff, text = 'Job Title', height=10, width=220, bg=bg_color)
        hotel_staff_job_title.place(x = 80, y = 150, height = 20, width = 220)
        hotel_staff_job_title = Combobox(newHotelStaff)  
        hotel_staff_job_title['values'] = ("Receptionist", "Cleaner", "Guard", "DBA", "Hotel Manager", 'Cleaner Manager')  
        hotel_staff_job_title.current(0)
        hotel_staff_job_title.place(x = 280, y = 150, height = 20, width = 220)
        hotel_staff_email = Label(newHotelStaff, text = 'Email', height=10, width=220, bg=bg_color)
        hotel_staff_email.place(x = 80, y = 180, height = 20, width = 220)
        hotel_staff_email = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_email.place(x = 280, y = 180, height = 20, width = 220)
        hotel_staff_phone = Label(newHotelStaff, text = 'Phone Number', height=10, width=220, bg=bg_color)
        hotel_staff_phone.place(x = 80, y = 210, height = 20, width = 220)
        hotel_staff_phone = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_phone.place(x = 280, y = 210, height = 20, width = 220)
        hotel_staff_address = Label(newHotelStaff, text = 'Address', height=10, width=220, bg=bg_color)
        hotel_staff_address.place(x = 80, y = 240, height = 20, width = 220)
        hotel_staff_address = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_address.place(x = 280, y = 240, height = 20, width = 220)
        hotel_staff_join_date = Label(newHotelStaff, text = 'Joining Date', height=10, width=220, bg=bg_color)
        hotel_staff_join_date.place(x = 80, y = 270, height = 20, width = 220)
        hotel_staff_join_date = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_join_date.place(x = 280, y = 270, height = 20, width = 220)
        hotel_staff_work_floor = Label(newHotelStaff, text = 'Work Floor', height=10, width=220, bg=bg_color)
        hotel_staff_work_floor.place(x = 80, y = 300, height = 20, width = 220)
        hotel_staff_work_floor = Spinbox(newHotelStaff, from_=1, to=5, width=5)  
        hotel_staff_work_floor.place(x = 280, y = 300, height = 20, width = 220)
        hotel_staff_gender = Label(newHotelStaff, text = 'Gender', height=10, width=220, bg=bg_color)
        hotel_staff_gender.place(x = 80, y = 330, height = 20, width = 220)
        hotel_staff_gender = Combobox(newHotelStaff)  
        hotel_staff_gender['values'] = ("Male", "Female")  
        hotel_staff_gender.current(0)
        hotel_staff_gender.place(x = 280, y = 330, height = 20, width = 220)
        hotel_staff_prev_job = Label(newHotelStaff, text = 'Previous Job Title', height=10, width=220, bg=bg_color)
        hotel_staff_prev_job.place(x = 80, y = 360, height = 20, width = 220)
        hotel_staff_prev_job = Combobox(newHotelStaff)  
        hotel_staff_prev_job['values'] = ("Receptionist", "Cleaner", "Guard", "DBA", "Hotel Manager", 'Cleaner Manager')  
        hotel_staff_prev_job.current(0)
        hotel_staff_prev_job.place(x = 280, y = 360, height = 20, width = 220)
        hotel_staff_prev_workplace = Label(newHotelStaff, text = 'Previous Workplace', height=10, width=220, bg=bg_color)
        hotel_staff_prev_workplace.place(x = 80, y = 390, height = 20, width = 220)
        hotel_staff_prev_workplace = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_prev_workplace.place(x = 280, y = 390, height = 20, width = 220)
        hotel_staff_job_exp = Label(newHotelStaff, text = 'Job Experience', height=10, width=220, bg=bg_color)
        hotel_staff_job_exp.place(x = 80, y = 420, height = 20, width = 220)
        hotel_staff_job_exp = Spinbox(newHotelStaff, from_=1, to=100, width=5)  
        hotel_staff_job_exp.place(x = 280, y = 420, height = 20, width = 220)
        hotel_staff_edu_lvl = Label(newHotelStaff, text = 'Highest Education Level', height=10, width=220, bg=bg_color)
        hotel_staff_edu_lvl.place(x = 80, y = 450, height = 20, width = 220)
        hotel_staff_edu_lvl = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_edu_lvl.place(x = 280, y = 450, height = 20, width = 220)
        hotel_staff_speciality = Label(newHotelStaff, text = 'Speciality', height=10, width=220, bg=bg_color)
        hotel_staff_speciality.place(x = 80, y = 480, height = 20, width = 220)
        hotel_staff_speciality = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_speciality.place(x = 280, y = 480, height = 20, width = 220)
        hotel_staff_birthday = Label(newHotelStaff, text = 'Birthday', height=10, width=220, bg=bg_color)
        hotel_staff_birthday.place(x = 80, y = 510, height = 20, width = 220)
        hotel_staff_birthday = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_birthday.place(x = 280, y = 510, height = 20, width = 220)
        hotel_staff_start_time = Label(newHotelStaff, text = 'Start Time', height=10, width=220, bg=bg_color)
        hotel_staff_start_time.place(x = 80, y = 540, height = 20, width = 220)
        hotel_staff_start_time = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_start_time.place(x = 280, y = 540, height = 20, width = 220)
        hotel_staff_end_time = Label(newHotelStaff, text = 'End Time', height=10, width=220, bg=bg_color)
        hotel_staff_end_time.place(x = 80, y = 570, height = 20, width = 220)
        hotel_staff_end_time = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_end_time.place(x = 280, y = 570, height = 20, width = 220)
        hotel_staff_salary = Label(newHotelStaff, text = 'Salary per Day', height=10, width=220, bg=bg_color)
        hotel_staff_salary.place(x = 80, y = 600, height = 20, width = 220)
        hotel_staff_salary = Entry(newHotelStaff, width=30, fg='black')
        hotel_staff_salary.place(x = 280, y = 600, height = 20, width = 220)
        button2 = Button(newHotelStaff, text='Insert', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=insertNewStaff)
        button2.place(x=1000, y = 550, width=100, height=30)
        button3 = Button(newHotelStaff, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=newHotelStaff.destroy)
        button3.place(x=1000, y = 600, width=100, height=30)
        newHotelStaff.mainloop()
    i1 = 0
    i = 1
    hotelStaff = Tk()
    hotelStaff.title('Veyron Sky: Hotel Manager')
    hotelStaff.geometry('1500x700')
    hotelStaff.configure(bg=bg_color)
    width_len = [3, 20, 20, 20, 23, 15, 30, 35, 15]
    list1 = cursor.execute("select hotel_staff_id, hotel_staff_name, hotel_staff_surname, hotel_staff_department_id, hotel_staff_job_title, job_experience, highest_education_level, speciality, hotel_staff_salary_per_hour from Hotel_Staff");
    e=Label(hotelStaff,width=width_len[0]+3,text='ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=0)
    e=Label(hotelStaff,width=width_len[1],text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=1)
    e=Label(hotelStaff,width=width_len[2],text='Surname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=2)
    e=Label(hotelStaff,width=width_len[3],text='Department',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=3)
    e=Label(hotelStaff,width=width_len[4],text='Job Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=4)
    e=Label(hotelStaff,width=width_len[5]+1,text='Job Experience',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=5)
    e=Label(hotelStaff,width=width_len[6]-1,text='Highest Education Level',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=6)
    e=Label(hotelStaff,width=width_len[7]-1,text='Speciality',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=7)
    e=Label(hotelStaff,width=width_len[8]+1,text='Salary per Hour',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=8)
    for row in list1:
        for j in range(9):
            e = Entry(hotelStaff, width=width_len[j]+4, fg='blue') 
            e.grid(row=i, column=j)
            if row[j] is None:
                e.insert(END, 'null')
            else:
                e.insert(END, row[j])
        i=i+1
    button1 = Button(hotelStaff, text='Dismiss Staff', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=dismiss_employee)
    button1.place(x=1100, y = 450, width=100, height=30)
    button2 = Button(hotelStaff, text='Add New Staff', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command = addNewHotelStaffWin)
    button2.place(x=1100, y = 500, width=100, height=30)
    button3 = Button(hotelStaff, text='Former Staff', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=former_staff)
    button3.place(x=1100, y = 550, width=100, height=30)
    button3 = Button(hotelStaff, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=hotelStaff.destroy)
    button3.place(x=1100, y = 600, width=100, height=30)
    hotelStaff.mainloop()

def former_staff():
    i1 = 0
    i = 1
    formerHotelStaff = Tk()
    formerHotelStaff.title('Veyron Sky: Hotel Manager')
    formerHotelStaff.geometry(f'{w}x{h}')
    formerHotelStaff.configure(bg=bg_color)
    width_len = [3, 15, 15, 10, 23, 15, 20, 20, 10, 30, 12, 12]
    list1 = cursor.execute("select hotel_staff_id, hotel_staff_name, hotel_staff_surname, hotel_staff_department_id, hotel_staff_job_title, job_experience, highest_education_level, speciality, hotel_staff_salary_per_hour, reasonOfDismissing, remainingSalary, dismiss_date from former_staff");
    e=Label(formerHotelStaff,width=width_len[0]+2,text='ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=0)
    e=Label(formerHotelStaff,width=width_len[1]+1,text='Name',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=1)
    e=Label(formerHotelStaff,width=width_len[2]+1,text='Surname',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=2)
    e=Label(formerHotelStaff,width=width_len[3]+2,text='Department',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=3)
    e=Label(formerHotelStaff,width=width_len[4],text='Job Title',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=4)
    e=Label(formerHotelStaff,width=width_len[5]+1,text='Job Experience',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=5)
    e=Label(formerHotelStaff,width=width_len[6],text='Highest Education Level',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=6)
    e=Label(formerHotelStaff,width=width_len[7],text='Speciality',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=7)
    e=Label(formerHotelStaff,width=width_len[8]+2,text='Salary per Hour',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=8)
    e=Label(formerHotelStaff,width=width_len[9],text='Reason/s of Dismissing',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=9)
    e=Label(formerHotelStaff,width=width_len[10]+2,text='Remaining Salary',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=10)
    e=Label(formerHotelStaff,width=width_len[11]+2,text='Dismissing Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=11)
    for row in list1:
        for j in range(12):
            e = Entry(formerHotelStaff, width=width_len[j]+4, fg='blue') 
            e.grid(row=i, column=j)
            if row[j] is None or str(row[j]).strip()=='':
                e.insert(END, 'null')
            else:
                e.insert(END, row[j])
        i=i+1
    button3 = Button(formerHotelStaff, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=formerHotelStaff.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    formerHotelStaff.mainloop()

def showHotelInvoices():
    i1 = 0
    i = 1
    hotelInvoice = Tk()
    hotelInvoice.title('Veyron Sky: Hotel Manager')
    hotelInvoice.geometry(f'{w}x{h}')
    hotelInvoice.configure(bg=bg_color)
    width_len = [3, 20, 20, 20, 20, 20, 20]
    list1 = cursor.execute("select hotel_invoice_id, hotel_invoice_reservation_id, hotel_invoice_guest_id, hotel_invoice_staff_id, hotel_invoice_total_cost, hotel_invoice_date, invoice_status from Hotel_Invoice");
    e=Label(hotelInvoice,width=width_len[0]+3,text='ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=0)
    e=Label(hotelInvoice,width=width_len[1],text='Reservation ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=1)
    e=Label(hotelInvoice,width=width_len[2],text='Guest ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=2)
    e=Label(hotelInvoice,width=width_len[3],text='Staff ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=3)
    e=Label(hotelInvoice,width=width_len[4],text='Total Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=4)
    e=Label(hotelInvoice,width=width_len[5]+1,text='Invoice Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=5)
    e=Label(hotelInvoice,width=width_len[6],text='Invoice Status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=6)
    for row in list1:
        for j in range(7):
            e = Entry(hotelInvoice, width=width_len[j]+4, fg='blue') 
            e.grid(row=i, column=j)
            if row[j] is None:
                e.insert(END, 'null')
            else:
                e.insert(END, row[j])
        i=i+1
    button3 = Button(hotelInvoice, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=hotelInvoice.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    hotelInvoice.mainloop()
    
def isdate(date_val):
    year,month,day = date_val.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False
    return isValidDate;
res = ''

def rest_table():
    restInv = Tk()
    restInv.title('Veyron Sky: Restaurant Manager')
    restInv.geometry(f'{w}x{h}')
    restInv.configure(bg=bg_color)
    width_len = [15, 15, 10, 10, 10, 18, 10]
    i1 = 0
    i = 1
    list1 = cursor2.execute("select firm_invoice_id, firm_invoice_reservation_id, firm_invoice_guest_id, firm_invoice_staff_id, firm_invoice_total_cost, firm_invoice_date, payment_type from firm_invoice where firm_id in ('R1', 'R2')");
    e=Label(restInv,width=width_len[0]+1,text='Firm Invoice ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=0)
    e=Label(restInv,width=width_len[1]+1,text='Reservation ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=1)
    e=Label(restInv,width=width_len[2]+2,text='Guest ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=2)
    e=Label(restInv,width=width_len[3]+2,text='Staff ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=3)
    e=Label(restInv,width=width_len[4]+2,text='Total Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=4)
    e=Label(restInv,width=width_len[5]+1,text='Date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=5)
    e=Label(restInv,width=width_len[6]+1,text='Payment Type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=i1,column=6)
    for row in list1:
        for j in range(7):
            e = Entry(restInv, width=width_len[j]+4, fg='blue') 
            e.grid(row=i, column=j)
            if row[j] is None or str(row[j]).strip() == '':
                e.insert(END, 'null')
            else:
                e.insert(END, row[j])
        i=i+1
    button3 = Button(restInv, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=restInv.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)

def rest_invoice():
    newRestInvoice = Tk()
    newRestInvoice.title('Veyron Sky: Restaurant Manager')
    newRestInvoice.geometry(f'{w}x{h}')
    newRestInvoice.configure(bg=bg_color)
    RID = Label(newRestInvoice,width=60,text='Choose the Restaurant',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    RID.place(x=600, y = 10, width=250, height=30)
    whichRest = StringVar(newRestInvoice)
    rad1 = Radiobutton(newRestInvoice, text='R1', value='R1', variable = whichRest, command = rest_staff)  
    rad2 = Radiobutton(newRestInvoice, text='R2', value='R2', variable = whichRest, command = rest_staff) 
    rad1.place(x=1200, y = 40)
    rad2.place(x=1200, y = 40)
    # 
    button3 = Button(newRestInvoice, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=newRestInvoice.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    newRestInvoice.mainloop()

def restInvoice():
    def rest_staff():
        def insertRestInvoice():
            if len(guestE.get())== 0 or len(staffE.get()) == 0 or len(payment_type.get()) == 0 or len(foodE.get()) == 0 or len(quanE.get()) == 0:
                messagebox.showerror('Error', 'All fields should be filled')
            else:
                if guestE.get().isdigit():
                    if len(foodE.get().strip().split(' ')) == len(quanE.get().strip().split(' ')):
                        cursor.execute("select res.reservation_id from RESERVATION as res right join Guest_Reservation as g_res on res.reservation_id = g_res.reservation_id where getdate() between res.arrival_date and res.departure_date and g_res.guest_id = '%s'" % int(guestE.get()))
                        res_id = 0
                        for row in cursor:
                            res_id = row[0]
                        if res_id != 0 and res_id is not None:
                            orig_food_list = []
                            cursor.execute("select food_id from restaurant_menu where restaurant_id = '%s'" % whichRest.get())
                            for row in cursor:
                                orig_food_list.append(row[0])
                            cnt = 0
                            for food in foodE.get().strip().split(' '):
                                if food in orig_food_list:
                                    cnt += 1
                            if cnt == len(foodE.get().strip().split(' ')):
                                cnt = 0
                                for q in quanE.get().strip().split(' '):
                                    if q.isdigit():
                                        cnt+=1
                                if cnt == len(quanE.get().strip().split(' ')):
                                    cursor.execute("exec foodBill @guest_id = '%s', @staff_id = '%s', @payment_type = '%s', @firm_id ='%s', @food_list = '%s', @quantity_list = '%s'" % 
                                       (guestE.get(), staffE.get(), payment_type.get(), whichRest.get(), foodE.get(), quanE.get()))
                                    cursor.execute("select top(1) firm_invoice_id from firm_invoice where firm_invoice_guest_id = '%s' order by firm_invoice_id desc" % int(guestE.get()))
                                    current_firm_invoice = 0
                                    for row in cursor:
                                          current_firm_invoice = row[0]
                                    cursor2.execute("select firm_invoice_total_cost from firm_invoice where firm_invoice_id = '%s'" % current_firm_invoice)
                                    total_cost = 0
                                    for row in cursor2:
                                        total_cost = row[0]
                                    messagebox.showinfo('Success', 'Food Invoice was created, total cost is '+ str(total_cost))
                                    newRestInvoice.destroy()
                                    restInvoice()
                                else:
                                    messagebox.showerror('Error', 'Sorry, innapropriate value in Quantity entry')
                            else:
                                messagebox.showerror('Error', 'Sorry, there is no such dish in chosen restaurant')
                        else:
                            messagebox.showerror('Error', 'Sorry, there is no current reservation for given guest ID or reservation already ended')
                    else:
                        messagebox.showerror('Error', 'Number of dishes and quanities are different')
                else:
                    messagebox.showerror('Error', 'Guest ID should be a number')
        guestL = Label(newRestInvoice,width=60,text='Enter Guest ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        guestL.place(x=600, y = 80, width=250, height=30)
        guestE = Entry(newRestInvoice,width=60)
        guestE.place(x=600, y = 110, width=120, height=30)
        staffL = Label(newRestInvoice,width=60,text='Choose Staff ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        staffL.place(x=600, y = 150, width=250, height=30)
        staffE = Combobox(newRestInvoice) 
        cursor.execute("select firm_staff_id from firm_staff where firm_id = '%s' and lower(firm_staff_job_title) = '%s'" % (whichRest.get(), 'waiter'))
        staff_list = []
        for row in cursor:
            staff_list.append(row[0])
        staffE['values'] = staff_list
        staffE.current(0)
        staffE.place(x=600, y = 180, width=120, height=30)
        foodL=Label(newRestInvoice,width=60,text='Enter food IDs(separated by commas)',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        foodL.place(x=600, y = 220, width=250, height=30)
        foodE=Entry(newRestInvoice,width=60)
        foodE.place(x=600, y = 250, width=200, height=30)
        quanL=Label(newRestInvoice,width=60,text='Enter food quantities(separated by commas)',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        quanL.place(x=600, y = 290, width=250, height=30)
        quanE=Entry(newRestInvoice,width=60)
        quanE.place(x=600, y = 320, width=200, height=30)
        payment_type = Label(newRestInvoice,width=60,text='Choose Payment Type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        payment_type.place(x=600, y = 360, width=250, height=30)
        payment_type = Combobox(newRestInvoice) 
        payment_type['values'] = ('cash', 'card')
        payment_type.current(0)
        payment_type.place(x=600, y = 390, width=120, height=30)
        button2 = Button(newRestInvoice, text='Create Invoice', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=insertRestInvoice)
        button2.place(x=600, y = 460, width=100, height=30)
        width_len = [5, 10, 10, 30, 5]
        i1 = 0
        i = 1
        list1 = cursor2.execute("select r.restaurant_id, f.food_id, f.food_type, f.food_description, r.cost from restaurant_menu as r join food as f on f.food_id = r.food_id where r.restaurant_id = '%s'" % whichRest.get());
        e=Label(newRestInvoice,width=width_len[0],text='Restaurant ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=i1,column=0)
        e=Label(newRestInvoice,width=width_len[1]+1,text='Food ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=i1,column=1)
        e=Label(newRestInvoice,width=width_len[2]+1,text='Food Type',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=i1,column=2)
        e=Label(newRestInvoice,width=width_len[3],text='Food Description',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=i1,column=3)
        e=Label(newRestInvoice,width=width_len[4]+1,text='Cost',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
        e.grid(row=i1,column=4)
        for row in list1:
            for j in range(5):
                e = Entry(newRestInvoice, width=width_len[j]+3, fg='blue') 
                e.grid(row=i, column=j)
                if row[j] is None:
                    e.insert(END, 'null')
                else:
                    e.insert(END, row[j])
            i=i+1
    newRestInvoice = Tk()
    newRestInvoice.title('Veyron Sky: Restaurant Manager')
    newRestInvoice.geometry('1500x700')
    newRestInvoice.configure(bg=bg_color)
    RID = Label(newRestInvoice,width=60,text='Choose the Restaurant',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    RID.place(x=600, y = 10, width=250, height=30)
    whichRest = StringVar(newRestInvoice)
    rad1 = Radiobutton(newRestInvoice, text='R1', value='R1', variable = whichRest, command = rest_staff)  
    rad2 = Radiobutton(newRestInvoice, text='R2', value='R2', variable = whichRest, command = rest_staff) 
    rad1.place(x=600, y = 40)
    rad2.place(x=640, y = 40)
    
    button1 = Button(newRestInvoice, text='Invoices', borderwidth=4, height=5, width=80, font=("Noto Sans JP", 10, 'bold'), command=rest_table)
    button1.place(x=1000, y = 550, width=100, height=30)
    button3 = Button(newRestInvoice, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=newRestInvoice.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    newRestInvoice.mainloop()
    
def showRating():
    def deleteFeedbacks(result):
        result.destroy()
    def buttonShowFeedbacks():
        if guest_id.get().strip() == '':
            guest = -1
        else:
            guest = int(guest_id.get().strip())
        if res_id.get().strip() == '':
            reservation = -1
        else:
            reservation = int(res_id.get().strip())
        cursor.execute("exec roomAndStaffRating @res_id = '%s', @guest_id = '%s', @total_rating = '%s', @room_rating = '%s', @staff_rating = '%s'" % 
                   (reservation, guest, float(total_rating.get()), float(room_rating.get()), float(staff_rating.get())))
        cursor.execute("select * from whole_feedback")
        text1 = ''
        for row in cursor:
            text1 += str(row[0]) + '\n'
        text1 = text1.replace('@', '\n')
        text1 = text1.replace('*', '\n')
        if len(text1) == 0:
            text1 = 'There are no ratings according to given options'
        result = Label(showFeedback,width=60,text=text1,borderwidth=2, relief='ridge', bg=bg_color, justify=LEFT)
        result.place(x=20, y = 20)
        true_false = True
        cursor.execute("delete from whole_feedback")
        t = Timer(10, deleteFeedbacks, [result])
        t.start()
    showFeedback = Tk()
    showFeedback.title('Veyron Sky: Hotel Manager')
    showFeedback.geometry(f'{w}x{h}')
    showFeedback.configure(bg=bg_color)
    res_id = Label(showFeedback,width=60,text='Enter Reservation ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    res_id.place(x=1000, y = 80, width=200, height=30)
    res_id = Entry(showFeedback,width=60)
    res_id.place(x=1000, y = 110, width=200, height=30)
    guest_id = Label(showFeedback,width=60,text='Enter Guest ID',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    guest_id.place(x=1000, y = 150, width=200, height=30)
    guest_id = Entry(showFeedback,width=60)
    guest_id.place(x=1000, y = 180, width=200, height=30)
    guest = ''
    reservatoin = ''
    total_rating = Label(showFeedback,width=60,text='Choose Total Rating',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    total_rating.place(x=1000, y = 220, width=200, height=30)
    total_rating = Combobox(showFeedback) 
    total_rating['values'] = (0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
    total_rating.current(10)
    total_rating.place(x=1000, y = 250, width=200, height=30)
    staff_rating = Label(showFeedback,width=60,text='Choose Staff Rating',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    staff_rating.place(x=1000, y = 290, width=200, height=30)
    staff_rating = Combobox(showFeedback) 
    staff_rating['values'] = (0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
    staff_rating.current(10)
    staff_rating.place(x=1000, y = 320, width=200, height=30)
    room_rating = Label(showFeedback,width=60,text='Choose Room Rating',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    room_rating.place(x=1000, y = 360, width=200, height=30)
    room_rating = Combobox(showFeedback) 
    room_rating['values'] = (0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0)
    room_rating.current(10)
    room_rating.place(x=1000, y = 390, width=200, height=30)
    
    button1 = Button(showFeedback, text='Show', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command = buttonShowFeedbacks)
    button1.place(x=1000, y = 550, width=100, height=30)
    button3 = Button(showFeedback, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=showFeedback.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    showFeedback.mainloop()


# In[62]:


def defineInput(variable):
    if(variable == '' or variable == ' '):
        return 'NULL'
    sizeWord = len(variable)
    cnt = 0
    for letter in variable:
        if(ord(letter)>=48 and ord(letter)<=57):
            cnt+=1
    if(cnt == sizeWord):
        return variable
    else:
        newVariable = '\'' + variable + '\''
        return newVariable

def isOkayData(g_id,g_name,g_surname,g_address,g_db,g_fam_stat,g_phone,g_email,g_day_arr,g_day_dep,prep,pet_number,child_number,g_gender):
    if (len(g_id) == 0 or len(g_name) == 0 or len(g_surname) == 0 or len(g_address) == 0 or len(g_db) == 0 or len(g_fam_stat) == 0 or len(g_phone) == 0 or  len(g_email) == 0 or len(g_day_arr) == 0 or len(g_day_dep) == 0 or len(prep) == 0 or len(pet_number) ==0 or len(child_number) == 0 or len(g_gender) == 0):
        return False
    return True

def make_reservation(g_id,g_name,g_surname,g_address,g_db,g_fam_stat,g_phone,g_email,g_des_type,g_des_floor,g_day_arr,g_day_dep,prep,pet_number,child_number,g_gender):
    g_id = defineInput(g_id)
    g_name = defineInput(g_name)
    g_surname = defineInput(g_surname)
    g_address = defineInput(g_address)
    g_db = defineInput(g_db)
    g_fam_stat = defineInput(g_fam_stat)
    g_phone = defineInput(g_phone)
    g_email = defineInput(g_email)
    g_day_arr = defineInput(g_day_arr)
    g_day_dep = defineInput(g_day_dep)
    prep = defineInput(prep)
    pet_number = defineInput(pet_number)
    child_number = defineInput(child_number)
    g_gender = defineInput(g_gender)
    proc_result = ''
    noProb = False
    if(isOkayData(g_id,g_name,g_surname,g_address,g_db,g_fam_stat,g_phone,g_email,g_day_arr,g_day_dep,prep,pet_number,child_number,g_gender) == False):
        messagebox.showerror('Error','You did not fill some of the Info!')
    else:
        if(g_des_type != 'NULL' ):
            if(g_des_type == ''):
                g_des_type = 'NULL'
            else:
                g_des_type = '\'' + g_des_type + '\''
        if(g_des_floor != 'NULL'):
            if(g_des_floor  == ''):
                g_des_floor = 'NULL'
            else:
                g_des_floor = '\'' + g_des_floor + '\'' 
        cursor.execute("""exec registerNewGuest @guestId = {} , @guestName = {} , @guestSurname = {},@guestAddress = {} ,@guestDateOfBirth = {},@guestFamilyStatus = {}, @guestPhoneNumber = {}, @guestEmail = {}, @desiredRoomType = {},  @desiredFloor = {}, @dayOfArrival= {}, @dayOfDeparture = {}, @prepayment = {}, @petNumber = {}, @childNumber = {}, @gender = {}""".format(g_id,g_name,g_surname,g_address,g_db,g_fam_stat,g_phone,g_email,g_des_type,g_des_floor,g_day_arr,g_day_dep,prep,pet_number,child_number,g_gender))
        for l in cursorTwo:
            l = list(l)
            result = str(l[0])
            if('Sorry' in result):
                noProb = True
                messagebox.showerror('Error',result)
            print(result)
        conn.commit()
        if(noProb == False):
            saveReservations()
            saveRoomAudit()
            if(subMain.winfo_exists()==1):
                subMain.destroy()
                showAllReservations()

def showAllReservations():
    #global allReservations_label
    global subMain
    subMain = Tk()
    subMain.geometry(f'{w}x{h}')
    count = 0
    cursor.execute("select count(*) from RESERVATION res join GUEST_RESERVATION g_r on res.reservation_id = g_r.reservation_id;")
    for row in cursor:
        count = row[0]
    listN = cursor.execute("""select res.reservation_id,res.arrival_date,res.departure_date,res.reservation_room_id,
                                            res.reservation_date,res.prepayment,res.reservation_status,g_r.guest_id 
                                            from RESERVATION res join GUEST_RESERVATION g_r 
                                            on res.reservation_id = g_r.reservation_id;""")
    e=Label(subMain,width=15,text='reservation_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=0)
    e=Label(subMain,width=15,text='arrival_date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=1)
    e=Label(subMain,width=15,text='departure_date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=2)
    e=Label(subMain,width=15,text='room_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=3)
    e=Label(subMain,width=15,text='reservation_date',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=4)
    e=Label(subMain,width=15,text='prepayment',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=5)
    e=Label(subMain,width=15,text='reservation_status',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=6)
    e=Label(subMain,width=15,text='guest_id',borderwidth=2, relief='ridge',anchor='w',bg='yellow')
    e.grid(row=0,column=7)
    subWindowOpened = True
    i=1
    for room in listN:
        for j in range(8):
            e = Entry(subMain, width=18, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, room[j])
        i=i+1
    subMain.mainloop()
    conn.commit()
    #output = ''
    
    #for row in cursor:
    #    output+=str(row) + '\n'
    #output = output.replace(',',' , ')
    #allReservations_label = Label(main,text = output)
    #allReservations_label.place(x = 800,y = 200)
    #conn.commit()
    
def do_room_reservation():
    main = Tk()
    main.geometry(f'{w}x{h}')
    global intoLabel_reservation, guest_id_label,guest_id_entry, guest_name_label, guest_name_entry, guest_surname_label, guest_surname_entry,guest_address_label, guest_address_entry, guest_birthday_label, guest_birthday_entry
    global guest_family_status_label, guest_family_status_box, guest_mob_number_label, guest_mob_number_entry, guest_email_label, guest_email_entry 
    global guest_desired_type_room_label, guest_desired_type_room_box, guest_desired_floor_room_label, guest_desired_floor_room_box, guest_arrval_date_label, guest_arrval_date_entry, guest_departure_date_label, guest_departure_date_entry, guest_prep_label, guest_prep_entry, guest_pets_number_label, guest_pets_number_entry
    global guest_children_number_label, guest_children_number_entry, guest_gender_label, guest_gender_entry, book_buttom, currReservations_Button, currDay_label
    intoLabel_reservation = Label(main,text = 'Room Booking')
    guest_id_label = Label(main, text = 'Please, type the Guest\'s ID: ')
    guest_id_entry = Entry(main)
    guest_name_label = Label(main,text = 'Please,type the Guest\'s Name: ')
    guest_name_entry = Entry(main)
    guest_surname_label = Label(main,text = 'Please, type the Guest\'s Surname: ')
    guest_surname_entry = Entry(main)
    guest_address_label = Label(main, text = 'Please, type the Guest\'s Address: ')
    guest_address_entry = Entry(main)
    guest_birthday_label = Label(main, text = 'Please, type the Guest\'s BirthDay: ')
    guest_birthday_entry = Entry(main)
    guest_family_status_label = Label(main,text = 'Please, choose the Guest\'s Family Status: ')
    guest_family_status_box = Combobox(main)
    guest_family_status_box['values'] = ('','single','married','divorced')
    guest_family_status_box.current(0)
    guest_mob_number_label  = Label(main,text = 'Please, type the Guest\'s Mobile number: ')
    guest_mob_number_entry = Entry(main) #???
    guest_email_label = Label(main, text = 'Please, type the Guest\'s e-mail: ')
    guest_email_entry = Entry(main)
    guest_desired_type_room_label = Label(main,text = 'Please, click on the desired Room Type: ') # ОТСЛЕЖИВАТЬ
    guest_desired_type_room_box = Combobox(main)
    guest_desired_type_room_box['values'] = ('','single', 'double', 'family', 'president')
    guest_desired_type_room_box.current(0) 
    guest_desired_floor_room_label = Label(main,text = 'Please, click on the desired Room Floor Location: ') 
    guest_desired_floor_room_box = Combobox(main) 
    guest_desired_floor_room_box['values'] = ('','2', '3', '4', '5')
    guest_desired_floor_room_box.current(0)
    guest_arrval_date_label = Label(main,text = 'Please, type the Guest\'s Arrival Date: ')
    guest_arrval_date_entry = Entry(main)
    guest_departure_date_label = Label(main, text = 'Please, type the Guest\'s Departure Date: ')
    guest_departure_date_entry = Entry(main)
    guest_prep_label = Label(main,text = 'Please, type the Guest\'s Prepayment: ')
    guest_prep_entry = Entry(main)
    guest_pets_number_label = Label(main, text = 'Please, type the Guest\'s Pet Number: ')
    guest_pets_number_entry = Entry(main)
    guest_children_number_label = Label(main,text = 'Please, type the Guest\'s children Number: ')
    guest_children_number_entry = Entry(main)
    guest_gender_label = Label(main, text = 'Please, type the Guest\'s gender: ')
    guest_gender_entry = Combobox(main)
    guest_gender_entry['values'] = ('Male','Female')
    guest_gender_entry.current(0)
    book_buttom = Button(main,text = 'RESERVE',command = lambda:make_reservation(guest_id_entry.get(),guest_name_entry.get(),guest_surname_entry.get(),guest_address_entry.get(),guest_birthday_entry.get(),guest_family_status_box.get(),guest_mob_number_entry.get(),guest_email_entry.get(),guest_desired_type_room_box.get(),guest_desired_floor_room_box.get(),guest_arrval_date_entry.get(),guest_departure_date_entry.get(),guest_prep_entry.get(),guest_pets_number_entry.get(),guest_children_number_entry.get(),guest_gender_entry.get()))
                                                                                                
    currReservations_Button = Button(main,text = 'Show Reservations',command = showAllReservations)
    
    today = datetime.date(datetime.now())

    intoLabel_reservation.pack()
    guest_id_label.pack()
    guest_id_entry.pack()
    guest_name_label.pack()
    guest_name_entry.pack()
    guest_surname_label.pack()
    guest_surname_entry.pack()
    guest_address_label.pack()
    guest_address_entry.pack()
    guest_birthday_label.pack()
    guest_birthday_entry.pack()
    guest_family_status_label.pack()
    guest_family_status_box.pack()
    guest_mob_number_label.pack()
    guest_mob_number_entry.pack()
    guest_email_label.pack()
    guest_email_entry.pack()
    guest_desired_type_room_label.pack()
    guest_desired_type_room_box.pack()
    guest_desired_floor_room_label.pack()
    guest_desired_floor_room_box.pack()
    guest_arrval_date_label.pack()
    guest_arrval_date_entry.pack()
    guest_departure_date_label.pack()
    guest_departure_date_entry.pack()
    guest_prep_label.pack()
    guest_prep_entry.pack()
    guest_pets_number_label.pack()
    guest_pets_number_entry.pack()
    guest_children_number_label.pack()
    guest_children_number_entry.pack()
    guest_gender_label.pack()
    guest_gender_entry.pack()
    book_buttom.pack()
    currReservations_Button.pack()

    sentence = 'Today\'s Date is : ' + str(today)
    currDay_label = Label(main,text = sentence)
    currDay_label.pack()
    main.mainloop()

def get_guest_reservations(guest_id):
    main = Tk()
    guest_id = defineInput(guest_id)
    cursor.execute("""select res.reservation_id,res.arrival_date,res.departure_date,res.reservation_room_id,res.reservation_date,
    res.prepayment,res.reservation_status,g_r.guest_id,g_r.pet_num,g_r.child_num
    from RESERVATION res join GUEST_RESERVATION g_r on res.reservation_id = g_r.reservation_id where g_r.guest_id = {};""".format(guest_id))
    output = ''
    for row in cursor:
        output+=str(row) + '\n'
    output = output.replace(',',' , ')
    allReservations_label = Label(main,text = output)
    allReservations_label.place(x = 800,y = 200)
    conn.commit()

def make_cancelling(guest_id,res_arriv_day,res_dep_day):
    guest_id = defineInput(guest_id)
    res_arriv_day = defineInput(res_arriv_day)
    res_dep_day = defineInput(res_dep_day)
    proc_result = ''
    exist_mistake = False
    cursor.execute("""exec spCancelBooking @guestId = {}, @arrivalGuestDate = {} , @departureGuestDate = {} ;""".format(guest_id,res_arriv_day,res_dep_day))
    for row in cursor:
        row = list(row)
        result = str(row[0])
        if('Sorry' in result):
            exist_mistake = True
            messagebox.showerror('Error',result)
        print(row)
    cursor.commit()
    if exist_mistake == False:
        saveReservations()
        saveRoomAudit()

def cancel_reservation():
    main = Tk()
    main.geometry(f'{w}x{h}')
    into_label_cancel = Label(main,text = 'You have selected the Option  :  ROOM CANCEL')
    guest_id_lab = Label(main, text = 'Please, type the Guest\'s ID: ')
    guest_id_ent = Entry(main)
    guest_id_but = Button(main,text = 'See Reservations',command = lambda:get_guest_reservations(guest_id_ent.get()))
    guest_arrival_d_lab = Label(main, text = 'Please, type the Reservation\'s ARRIVAL DATE: ')
    guest_arrival_d_ent = Entry(main)
    guest_dep_d_lab = Label(main, text = 'Please, type the Reservation\'s DEPARTURE DATE: ')
    guest_dep_d_e = Entry(main)
    can_res_but = Button(main,text = 'CANCEL RESERVATION', command = lambda:make_cancelling(guest_id_ent.get(),guest_arrival_d_ent.get(),guest_dep_d_e.get()))

    today = datetime.now()
    sentence = 'Today\'s day is ' + str(today)
    tod_da_lab = Label(main,text = sentence)

    into_label_cancel.pack()
    guest_id_lab.pack()
    guest_id_ent.pack()
    guest_id_but.pack()
    guest_arrival_d_lab.pack()
    guest_arrival_d_ent.pack()
    guest_dep_d_lab.pack()
    guest_dep_d_e.pack()
    can_res_but.pack()
    tod_da_lab.pack()

def join_guest(owner_id, j_guest_id, j_guest_name,j_guest_surname,j_guest_addr, j_guest_birthday, j_guest_fam_stat,j_guest_phone, j_guest_email,own_day_arrival,numb_pet,child_numb,j_g_gender):
    main = Tk()
    main.geometry(f'{w}x{h}')
    owner_id = defineInput(owner_id)
    j_guest_id = defineInput(j_guest_id)
    j_guest_name = defineInput(j_guest_name)
    j_guest_surname = defineInput(j_guest_surname)
    j_guest_addr = defineInput(j_guest_addr)
    j_guest_birthday = defineInput(j_guest_birthday)
    j_guest_fam_stat = defineInput(j_guest_fam_stat)
    j_guest_phone = defineInput(j_guest_phone)
    j_guest_email = defineInput(j_guest_email)
    own_day_arrival = defineInput(own_day_arrival)
    numb_pet = defineInput(numb_pet)
    child_numb = defineInput(child_numb)
    j_g_gender = defineInput(j_g_gender)
    proc_result = ''
    cursorTwo.execute("""exec joinCurrentGuestRoom @guestFindId = {},@guestId = {},@guestName = {},@guestSurname = {}, 
    @guestAddress= {},@guestDateOfBirth = {},@guestFamilyStatus = {},
    @guestPhoneNumber= {},@guestEmail = {}, @dayOfArrival = {}, @petNumber = {},
    @childNumber = {}, @gender= {};""".format(owner_id,j_guest_id,j_guest_name,j_guest_surname,j_guest_addr,j_guest_birthday,j_guest_fam_stat,j_guest_phone,j_guest_email,own_day_arrival,numb_pet,child_numb,j_g_gender))

    for l in cursorTwo:
        l = list(l)
        result = str(l[0])
        if('Sorry' in result):
            messagebox.showerror('Error',result)
        print(result)

    conn.commit()


def join_procedure():
    main = Tk()
    main.geometry(f'{w}x{h}')
    intro_join_label = Label(main,text = 'You have selected the Option  :  JOIN RESERVATION')
    owner_id_lab = Label(main, text = 'Please, type the OWNER\'S ID:')
    owner_id_ent = Entry(main)
    owner_res_button = Button(main, text = 'SEE RESERVATION', command = lambda:get_guest_reservations(owner_id_ent.get()))
    guest_id_labe = Label(main,text = 'Please, type the Guest\'s ID:')
    guest_id_ent = Entry(main)
    guest_name_labe = Label(main, text = 'Please, type the Guest\'s Name:')
    guest_name_ent = Entry(main)
    guest_surname_lab = Label(main, text = 'Please, type the Guest\'s Surname:')
    guest_surname_ent = Entry(main)
    guest_addr_lab = Label(main, text = 'Please, type the Guest\'s Address:')
    guest_addr_ent = Entry(main)
    guest_birth_lab = Label(main, text = 'Please, type the Guest\'s BirthDay in format "yyyy-mm-dd" :')
    guest_birth_ent = Entry(main)
    guest_fam_stat_lab = Label(main, text = 'Please, type the Guest\'s Family Status:')
    guest_fam_stat_ent = Entry(main)
    guest_mob_numb_lab = Label(main, text = 'Please, type the Guest\'s Mobile number:')
    guest_mob_numb_ent = Entry(main)
    guest_email_lab = Label(main, text = 'Please, type the Guest\'s e-mail:')
    guest_email_ent = Entry(main)
    owner_arriv_date_lab = Label(main, text = 'Please, type the Owner\'s Arrival Date in Reservation: ')
    owner_arriv_date_ent = Entry(main)
    guest_gender_lab =  Label(main, text = 'Please, type the Guest\'s Gender:')
    guest_gender_ent = Entry(main)
    guest_pets_numb_lab = Label(main, text = 'Please, type the number of pets with you: ')
    guest_pets_numb_ent = Entry(main)
    guest_childr_numb_lab = Label(main, text = 'Please, type the number of children with your: ')
    guest_childr_numb_entr = Entry(main)
    join_guest_button = Button(main, text = 'Join Guest', command = lambda:join_guest(owner_id_ent.get(),guest_id_ent.get(),guest_name_ent.get(),guest_surname_ent.get(),guest_addr_ent.get(),guest_birth_ent.get(),guest_fam_stat_ent.get(),guest_mob_numb_ent.get(),guest_email_ent.get(),owner_arriv_date_ent.get(),guest_pets_numb_ent.get(),guest_childr_numb_entr.get(),guest_gender_ent.get()))

    intro_join_label.pack()
    owner_id_lab.pack()
    owner_id_ent.pack()
    owner_res_button.pack()
    guest_id_labe.pack()
    guest_id_ent.pack()
    guest_name_labe.pack()
    guest_name_ent.pack()
    guest_surname_lab.pack()
    guest_surname_ent.pack()
    guest_addr_lab.pack()
    guest_addr_ent.pack()
    guest_birth_lab.pack()
    guest_birth_ent.pack()
    guest_fam_stat_lab.pack()
    guest_fam_stat_ent.pack()
    guest_mob_numb_lab.pack()
    guest_mob_numb_ent.pack()
    guest_email_lab.pack()
    guest_email_ent.pack()
    owner_arriv_date_lab.pack()
    owner_arriv_date_ent.pack()
    guest_gender_lab.pack()
    guest_gender_ent.pack()
    guest_pets_numb_lab.pack()
    guest_pets_numb_ent.pack()
    guest_childr_numb_lab.pack()
    guest_childr_numb_entr.pack()
    join_guest_button.pack()

    today = datetime.now()
    sentence = 'Today\'s day is ' + str(today)
    tod_da_lab = Label(main,text = sentence)
    tod_da_lab.pack()

def evict_guest(guest_id,payment_type):
    main = Tk()
    main.geometry(f'{w}x{h}')
    exist_mistake = False
    guest_id = defineInput(guest_id)
    payment_type = defineInput(payment_type) # PAYMENT_TYPE УКАЗАТЬ
    proc_result = ''
    cursorTwo.execute("""exec spEvictGuest @guestId = {}, @payment_type = {};""".format(guest_id,payment_type))
    for l in cursorTwo:
        l = list(l)
        result = str(l[0])
        if('Sorry' in result):
            messagebox.showerror('Error',result)
            exist_mistake = True
        print(result)
    conn.commit()
    if exist_mistake == False:
        saveReservations()
        saveRoomAudit()

def dismiss_guest():
    main = Tk()
    main.geometry(f'{w}x{h}')
    into_label_dismiss_guest = Label(main, text = ' You have selected the Option : GUEST DISMISSING ')
    guest_id_label = Label(main,text = 'Please, type the Guest\'s ID: ')
    guest_id_entry = Entry(main)
    guest_payment_type_label = Label(main,text = 'Please, type the Guest\'s Payment Type: ')
    guest_payment_type_box = Entry(main)
    guest_see_reservations_button = Button(main, text = 'See Reservations', command = lambda:get_guest_reservations(guest_id_entry.get()))
    guest_button_dissmissing = Button(main,text = 'Evict guest', command = lambda:evict_guest(guest_id_entry.get(),guest_payment_type_box.get()))
    into_label_dismiss_guest.pack()
    guest_id_label.pack()
    guest_id_entry.pack()
    guest_payment_type_label.pack()
    guest_payment_type_box.pack()
    guest_see_reservations_button.pack()
    guest_button_dissmissing.pack()

    today = datetime.now()
    sentence = 'Today\'s day is ' + str(today)
    tod_da_lab = Label(main,text = sentence)
    tod_da_lab.pack()
    main.mainloop()

def finally_dismiss_empl(emp_id,departm_id,reason):
    emp_id = defineInput(emp_id)
    departm_id = defineInput(departm_id)
    reason = defineInput(reason)
    proc_result = ''
    cursor.execute("""exec spDismissEmployee @employeeId = {}, @departmentId = {}, @reason = {};""".format(emp_id,departm_id,reason))
    for l in cursor:
        l = list(l)
        result = str(l[0])
        if('Sorry' in result):
            messagebox.showerror('Error',result)
        print(result)
    conn.commit()

def dismiss_employee():
    main = Tk()
    main.geometry(f'{w}x{h}')
    into_lavel_dis_emp = Label(main, text = 'Employee Dismissing')
    emp_id_label = Label(main,text = 'Please, type the Employee ID: ')
    emp_id_ent = Entry(main)
    emp_department_id_label = Label(main,text = 'Please, type the Department where ID works(optional): ')
    emp_department_id_ent = Entry(main)
    emp_reason_label = Label(main, text = 'Please, type the reason why you dismiss this Employee: ')
    emp_reason_entry = Entry(main)
    into_lavel_dis_emp.pack()
    emp_id_label.pack()
    emp_id_ent.pack()
    emp_department_id_label.pack()
    emp_department_id_ent.pack()
    emp_reason_label.pack()
    emp_reason_entry.pack()
    emp_get_where_works_buttom.pack()
    emp_dism_button.pack()

    today = datetime.now()
    sentence = 'Today\'s day is ' + str(today)
    tod_da_lab = Label(main,text = sentence)
    tod_da_lab.pack()

def menu_options(login):
    pass
    
def exit_system():
    current_user = ''
    cursor1.execute("select login from Accounts where user_status = 'online'")
    for row in cursor1:
        current_user = row[0]
    cursor1.execute("exec spLogOutSystem @login='%s'" % current_user)
    #ADD HERE


# In[63]:


def receptionistWin():
    receptionistRoot = Tk()
    receptionistRoot.title('Veyron Sky: Receptionist')
    receptionistRoot.geometry(f'{w}x{h}')
    receptionistRoot.configure(bg=bg_color)
    label0 = Label(receptionistRoot, text='Welcome Receptionist', height=10, width=30, bg=bg_color, fg='black', font=("Noto Sans JP", 11, 'bold'))
    label0.place(x = 20, y = 30, width=180, height=20)
    button2 = Button(receptionistRoot, text='Registrations', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=reservationWin)
    button2.place(x = 20, y = 150, width=120, height=50)
    button3 = Button(receptionistRoot, text='Guests', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=showGuests)
    button3.place(x = 20, y = 200, width=120, height=50)
    button4 = Button(receptionistRoot, text='Invoices', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=showHotelInvoices)
    button4.place(x = 20, y = 250, width=120, height=50)
    receptionistRoot.mainloop()
    
def reservationWin():
    reservWin = Tk()
    reservWin.title('Veyron Sky: Receptionist')
    reservWin.geometry(f'{w}x{h}')
    reservWin.configure(bg=bg_color)
    label0 = Label(reservWin, text='Reservations', height=10, width=30, bg=bg_color, fg='black', font=("Noto Sans JP", 14, 'bold'))
    label0.place(x = 40, y = 30, width=180, height=20)
    button2 = Button(reservWin, text='New Reservation', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=do_room_reservation)
    button2.place(x = 40, y = 150, width=120, height=50)
    button3 = Button(reservWin, text='Join Guest', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=join_procedure)
    button3.place(x = 40, y = 200, width=120, height=50)
    button4 = Button(reservWin, text='Cancel Booking', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=cancel_reservation)
    button4.place(x = 40, y = 250, width=120, height=50)
    button4 = Button(reservWin, text='Evict Guest', borderwidth=4, height=5, width=50, font=("Noto Sans JP", 10, 'bold'), command=dismiss_guest)
    button4.place(x = 40, y = 300, width=120, height=50)
    button3 = Button(reservWin, text='Back', borderwidth=4, height=5, width=20, font=("Noto Sans JP", 10, 'bold'), command=reservWin.destroy)
    button3.place(x=1000, y = 600, width=100, height=30)
    reservWin.mainloop()
    
def guest_enter_check(res_id,guest_id):
    ans = 0
    if res_id.isdigit() and guest_id.isdigit():
        password = defineInput(password)
        proc_result = ''
        isProblem = False
        cursor.execute("""exec guestEnter @res_id = {}, @guest_id = {};""".format(res_id, guest_id))
        for l in cursor:
            l = list(l)
            result = str(l[0])
            if('Sorry' in result):
                messagebox.showerror('Error',result)
                isProblem = True
            
    else:
        messagebox.showerror('Error','Reservation ID and guest ID should be both numeric!')
def saveReservations():
    cursor.execute("""select * from RESERVATION res join Guest_Reservation g_r on res.reservation_id = g_r.reservation_id""")
    var_fix = []
    for row in cursor:
        var_fix.append(list(map(str,list(row))))
    f = open("pythonReservations.txt","w")
    word = ''
    for k in var_fix:
        for j in k:
            j = j.replace('  ','')
        word +=str(k)
        word +='\n'

    f.write(word)
    f.close()

def saveRoomAudit():
    cursor.execute("""select * from room_audit""")
    var_fix = []
    for row in cursor:
        var_fix.append(list(map(str,list(row))))
    f = open("PythonRoomAudit.txt","w")
    word = ''
    for k in var_fix:
        for j in k:
            j = j.replace('  ','')
        word += str(k)
        word += '\n'
    f.write(word)
    f.close()

def final_enter(login,password):
    login = defineInput(login)
    password = defineInput(password)
    proc_result = ''
    isProblem = False
    cursor.execute("""exec spEnterSystem @login = {}, @password = {};""".format(login,password))
    for l in cursor:
        l = list(l)
        result = str(l[0])
        if('Sorry' in result):
            messagebox.showerror('Error',result)
            isProblem = True
        if (result=='Receptionist'):
            receptionistWin()
        if (result == 'Hotel Manager'):
            hotelManagerWin()
        if (result == 'Cleaner Manager'):
            hotel_invoice()
        if (result == 'SPA Manager'):
            spa_invoice()
        if (result == 'Gym Manager'):
            gym_invoice()
        if (result == 'Restaurant Manager'):
            restInvoice()
    if(isProblem == False):
        menu_options(login)
    conn.commit()

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
	enter_button = Button(main, bg='#05081a', image=ent_pic, borderwidth=0, command = lambda:final_enter(login.get(),password.get()))
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
	contacts = Label(main, bg='#05081a', image=con_pic)
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