from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
root = Tk()

root.title('GetData Graph Digitizer')
root.configure(bg = 'PeachPuff')
# root.iconbitmap('C:\\Users\\User\\Documents\\Python\\GetData Graph Digitizer\\mcm.ico')
root.geometry()
root.resizable(width=True, height=True)


class GetDataDigitizer:
    states = ["free", "scale", "coordinates", "free2"]
    state = states[0]
    kx = 1
    ky = 1
    states_of_coordinates = ["x minimum", "x maximum", "y minimum", "y maximum"]
    coordinate_state = states_of_coordinates[0]
    x_min = 0
    x_max = 1
    x_min_pixel = (1, 1)
    x_max_pixel = (1, 1)
    y_min = 0
    y_max = 1
    y_min_pixel = (1, 1)
    y_max_pixel = (1, 1) 
    x0 = 0
    y0 = 0
    old_x = 0
    old_y = 0
    is_first_click = True
    canvas = None
    imagesprite2 = None
    pilImage = None
    imagetk = None
    image2 = None
    def __init__(self):
        self.root = root
    @staticmethod
    def point_capture():
        GetDataDigitizer.state = GetDataDigitizer.states[2]
    @staticmethod
    def scale():
        GetDataDigitizer.state = GetDataDigitizer.states[1]
        GetDataDigitizer.zoom()
    @staticmethod
    def coordinates_info(event):
        x, y = event.x, event.y
        label = Label(root, text='Current coordinates', font='System',bg = 'Moccasin',fg='SystemActiveCaption')
        label.pack()
        label['text'] = f'X: {(x - GetDataDigitizer.x0) / GetDataDigitizer.kx + GetDataDigitizer.x_min} , Y: {-(y - GetDataDigitizer.y0) / GetDataDigitizer.ky + GetDataDigitizer.y_min}'
    @staticmethod
    def tracker(event):
        if GetDataDigitizer.imagesprite2:
            GetDataDigitizer.canvas2.delete(GetDataDigitizer.imagesprite2)
        GetDataDigitizer.imagesprite2 = None
        GetDataDigitizer.imagetk = None
        GetDataDigitizer.canvas2.imagetk = None
        new_size = 3000, 1500
        GetDataDigitizer.imagetk = ImageTk.PhotoImage(GetDataDigitizer.pilImage.resize(new_size))
        GetDataDigitizer.imagesprite2 = GetDataDigitizer.canvas2.create_image((GetDataDigitizer.image.width()//2 - event.x)*5 +200,
                                            (GetDataDigitizer.image.height()//2 - event.y)*5+150,
                                            image=GetDataDigitizer.imagetk)
        GetDataDigitizer.canvas2.create_oval(197, 147, 203, 153, fill='red')
    @staticmethod
    def zoom():

        newwin = Toplevel(root)
        # newwin.iconbitmap('C:\\Users\\User\\Documents\\Python\\GetData Graph Digitizer\\mcm.ico')
        newwin.configure(bg = 'PeachPuff')
        GetDataDigitizer.canvas2 = Canvas(newwin)
        GetDataDigitizer.canvas2.pack()
        GetDataDigitizer.image2 = ImageTk.PhotoImage(GetDataDigitizer.pilImage)
        GetDataDigitizer.imagesprite2 = GetDataDigitizer.canvas2.create_image(GetDataDigitizer.image.width()//2, GetDataDigitizer.image.height()//2, image=GetDataDigitizer.image)
        root.bind('<Motion>', GetDataDigitizer.tracker)
    @staticmethod
    def openbutton():
        a = filedialog.askopenfilename(title='open')
        return a
    @staticmethod
    def picture():
        x = GetDataDigitizer.openbutton()
        GetDataDigitizer.open_pic(x)
        return
    @staticmethod
    def open_pic(x):
        GetDataDigitizer.canvas = Canvas(height = 300, width = 600, bg='PeachPuff')
        GetDataDigitizer.canvas.pack()
        GetDataDigitizer.pilImage = Image.open(x)
        GetDataDigitizer.image = GetDataDigitizer.pilImage.resize((600, 300))
        GetDataDigitizer.image = ImageTk.PhotoImage(GetDataDigitizer.image)
        GetDataDigitizer.canvas.create_image(GetDataDigitizer.image.width()//2, GetDataDigitizer.image.height()//2, image=GetDataDigitizer.image)
        root.mainloop()
    @staticmethod
    def save(s, is_first_click):
        if is_first_click:
            with open('Coordinates.txt', 'w') as f:
                f.write(s + '\n')
        else:
            with open('Coordinates.txt' , 'a+') as f:
                f.write(s + '\n')  
    @staticmethod
    def click(event):
        x, y = event.x, event.y
        if GetDataDigitizer.state == GetDataDigitizer.states[2]:
            print(f"Current Coordinates = [X: {(x - GetDataDigitizer.x0) / GetDataDigitizer.kx + GetDataDigitizer.x_min} , Y: {-(y - GetDataDigitizer.y0) / GetDataDigitizer.ky + GetDataDigitizer.y_min}]")
            GetDataDigitizer.save(f"Current Coordinates = [X: {(x - GetDataDigitizer.x0) / GetDataDigitizer.kx + GetDataDigitizer.x_min} , Y: {-(y - GetDataDigitizer.y0) / GetDataDigitizer.ky + GetDataDigitizer.y_min}]", GetDataDigitizer.is_first_click)
            GetDataDigitizer.coordinates_info(event)
            if not GetDataDigitizer.is_first_click:
                GetDataDigitizer.canvas.create_line(GetDataDigitizer.old_x, GetDataDigitizer.old_y, x, y)
            else:
                GetDataDigitizer.is_first_click = False
            GetDataDigitizer.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill='SystemActiveCaption')
            GetDataDigitizer.old_x = x
            GetDataDigitizer.old_y = y
        elif GetDataDigitizer.state == GetDataDigitizer.states[1]:
            newwin = Toplevel(root)
            # newwin.iconbitmap('C:\\Users\\User\\Documents\\Python\\GetData Graph Digitizer\\mcm.ico')
            newwin.configure(bg = 'PeachPuff')
            if GetDataDigitizer.coordinate_state == GetDataDigitizer.states_of_coordinates[0]:
                lbl = Label(newwin, text='x minimum', font='System',bg = 'Moccasin',fg='SystemActiveCaption')
                e = Entry(newwin, width=20)
                lbl.pack()
                e.pack()
                def xminf():
                    GetDataDigitizer.x_min = int(e.get())
                    GetDataDigitizer.x_min_pixel = (x, y)
                    GetDataDigitizer.coordinate_state = GetDataDigitizer.states_of_coordinates[1]
                    GetDataDigitizer.y0 = y
                    newwin.destroy()
                b = Button(newwin, text='ok', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=xminf).pack()
            elif GetDataDigitizer.coordinate_state == GetDataDigitizer.states_of_coordinates[1]: 
                lbl = Label(newwin, text='x maximum', font='System',bg = 'Moccasin',fg='SystemActiveCaption')
                e = Entry(newwin, width=20)
                lbl.pack()
                e.pack()
                def xmaxf():
                    GetDataDigitizer.x_max = int(e.get())
                    GetDataDigitizer.x_max_pixel = (x, y)
                    GetDataDigitizer.coordinate_state = GetDataDigitizer.states_of_coordinates[2]
                    GetDataDigitizer.kx = GetDataDigitizer.x_max_pixel[0] - GetDataDigitizer.x_min_pixel[0]
                    GetDataDigitizer.kx = abs(GetDataDigitizer.kx / (GetDataDigitizer.x_max - GetDataDigitizer.x_min))
                    newwin.destroy()        
                b = Button(newwin, text='ok', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=xmaxf).pack()
            elif GetDataDigitizer.coordinate_state == GetDataDigitizer.states_of_coordinates[2]: 
                lbl = Label(newwin, text='y minimum', font='System',bg = 'Moccasin',fg='SystemActiveCaption')
                e = Entry(newwin, width=20)
                lbl.pack()
                e.pack()
                def yminf():
                    GetDataDigitizer.y_min = int(e.get())
                    GetDataDigitizer.y_min_pixel = (x, y)
                    GetDataDigitizer.coordinate_state = GetDataDigitizer.states_of_coordinates[3]
                    GetDataDigitizer.x0 = x
                    newwin.destroy()
                b = Button(newwin, text='ok', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=yminf).pack()        
            elif GetDataDigitizer.coordinate_state == GetDataDigitizer.states_of_coordinates[3]: 
                lbl = Label(newwin, text='y maximum', font='System',bg = 'Moccasin',fg='SystemActiveCaption')
                e = Entry(newwin, width=20)
                lbl.pack()
                e.pack()    
                def ymaxf():
                    GetDataDigitizer.y_max = int(e.get())
                    GetDataDigitizer.y_max_pixel = (x, y)
                    GetDataDigitizer.coordinate_state = GetDataDigitizer.states_of_coordinates[0]
                    GetDataDigitizer.ky = GetDataDigitizer.y_max_pixel[1] - GetDataDigitizer.y_min_pixel[1]
                    GetDataDigitizer.ky = abs(GetDataDigitizer.ky / (GetDataDigitizer.y_max - GetDataDigitizer.y_min))
                    GetDataDigitizer.state = GetDataDigitizer.states[3]
                    newwin.destroy()
                b = Button(newwin, text='ok', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=ymaxf).pack()



btn1 = Button(root, text='Open Image', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=GetDataDigitizer.picture).pack()
btn3 = Button(root, text='Set the scale', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=GetDataDigitizer.scale).pack()
btn4 = Button(root, text='Point capture mode', font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=GetDataDigitizer.point_capture).pack()
btn2 = Button(root, text="Quit", font='System',bg = 'Moccasin',fg='SystemActiveCaption', command=root.destroy).pack()
root.bind('<Button-3>', GetDataDigitizer.click)
root.mainloop()
get_data_obj = GetDataDigitizer(root)