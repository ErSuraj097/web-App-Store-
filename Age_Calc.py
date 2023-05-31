import datetime
from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.geometry("1300x700+0+0")
root.title(" Age Calculator App | Developed By Suraj Yadav ")
root.config(bg="whitesmoke")
root.focus_force()
root.resizable(0,0)

def getInput():
    name=nameEntry.get()
    monkey = Person(name,datetime.  date(int(yearEntry.get()),  int(monthEntry.get()),int(dateEntry.get())))
    
    textArea = Text(root,font=("times new roman",18,"bold"),fg="navy",bg="white",bd=0)
    textArea.place(x=700,y=500,height=80, width=490)
    answer = "\tHii.. {monkey}.\n\tYou are {age} years old  !!! ".format(monkey=name,   age=monkey.age())
    textArea.insert(END,answer)

def clear():
    global textArea
    nameEntry.delete(0,END)
    dateEntry.delete(0,END)
    monthEntry.delete(0,END)
    yearEntry.delete(0,END)
    textArea.delete(0,END)

class Person:
    def __init__(self,name,birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age
def slider_func():
        
            global img1
            global img2
            global img3
            global img4
            global img5
            global img6
            im=img1
            img1=img2
            img2=img3
            img3=img4
            img4=img5
            img5=img6
            img6=im
            #self.lbl1.config(image=self.img1)
            lbl3.config(image=im)
            
            lbl3.after(2000,slider_func)
def home():
    root.destroy()
    import First_Page
def back():
    root.destroy()
    import Second_Page


title_lbl1=Label(root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
title_lbl1=Label(root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

title_lbl1=Label(root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

txt_lbl=Label(root,text="Age Calculator Application",font=("times new roman",30,"bold"),bg="whitesmoke",fg="navy").place(x=50,y=140,)

        
logo=ImageTk.PhotoImage(file="image/up1.png")
image_lbl=Label(root,image=logo,bd=0).place(x=20,y=0)
        
photo=ImageTk.PhotoImage(file="image/side11.png")
label_image=Label(root,image=photo)
label_image.place(x=50,y=250)

'''#..........slider_ Image..........
            
img1=ImageTk.PhotoImage(file='image/suraj.jpg')
img2=ImageTk.PhotoImage(file='image/bp1.png')
img3=ImageTk.PhotoImage(file='image/suraj12.jpg')
img4=ImageTk.PhotoImage(file='image/bg10.png')
img5=ImageTk.PhotoImage(file='image/side123.png')
img6=ImageTk.PhotoImage(file='image/a12.jpeg')
        #Frame.....Image....Label
frame_1=Frame(root)
frame_1.place(x=100,y=170,width=550,height=425)
        
lbl1=Label(frame_1,image=img1,bd=0)
lbl1.place(x=0,y=0)
lbl2=Label(frame_1,image=img2,bd=0)
lbl2.place(x=0,y=0)
lbl3=Label(frame_1,image=img3,bd=0)
lbl3.place(x=0,y=0)
        #self.img1=ImageTk.PhotoImage(file='qr_code1.jpg')

slider_func()        
'''

#title_name = Label(root,text = "AGE CALCULATOR APPLICATION",font=("times new roman",30,"bold"),fg="crimson",bg="whitesmoke").place(x=0,y=15,relwidth=1)
#title_name = Label(root,text = "",font=("times new roman",20,"bold"),fg="crimson",bg="wheat").place(x=700,y=40)

lbl_frame=Frame(root,bg="white",bd=1,relief=GROOVE)
lbl_frame.place(x=700,y=170,width=500,height=425)

enter_name =Label(lbl_frame,text = "Age Calculator",font=("Impact",25,"bold"),bg="white",fg="crimson")
enter_name.place(x=0,y=10,relwidth=1)

name =Label(lbl_frame,text = "Name",font=("times new roman",18,"bold"),bg="white")
name.place(x=40,y=80)

date = Label(lbl_frame,text = "Day",font=("times new roman",18,"bold"),bg="white")
date.place(x=40,y=130)


month = Label(lbl_frame,text = "Month",font=("times new roman",18,"bold"),bg="white")
month.place(x=40,y=180)

year = Label(lbl_frame,text = "Year",font=("times new roman",18,"bold"),bg="white")
year.place(x=40,y=230)


nameEntry = Entry(lbl_frame,font=("times new roman",15,),bg="white")
nameEntry.place(x=130,y=80,width=300,height=30)

dateEntry = Entry(lbl_frame,font=("times new roman",15,),bg="white")
dateEntry.place(x=130,y=130,width=300,height=30)


monthEntry = Entry(lbl_frame,font=("times new roman",15,),bg="white")
monthEntry.place(x=130,y=180,width=300,height=30)

yearEntry =Entry(lbl_frame,font=("times new roman",15,),bg="white")
yearEntry.place(x=130,y=230,width=300,height=30)

button=Button(lbl_frame,text="Calculate Age",font=("times new roman",15,"bold"),command=getInput,bg="dodgerblue",fg="white",bd=0,cursor="hand2")
button.place(x=90,y=290,width=150,height=35)

button=Button(lbl_frame,text="Clear",font=("times new roman",15,"bold"),command=clear,bg="orange",fg="white",bd=0,cursor="hand2")
button.place(x=260,y=290,width=150,height=35)

button=Button(root,text="Home Page",font=("times new roman",15,"bold"),command=home,bg="gold",fg="white",bd=0,cursor="hand2")
button.place(x=50,y=190,width=280,height=40)
button=Button(root,text="Back",font=("times new roman",15,"bold"),command=back,bg="dodgerblue",fg="white",bd=0,cursor="hand2")
button.place(x=370,y=190,width=280,height=40)
#button=Button(root,text="About",font=("times new roman",15,"bold"),command=back,bg="dodgerblue",fg="white",bd=0,cursor="hand2")
#button.place(x=450,y=190,width=150,height=35)



footer_frame=Frame(root,bg='teal')
footer_frame.place(x=0,y=600,width=1300,height=100)

footerlbl6=Label(footer_frame,text="Complete Mini Project 2020-21",font=("times new roman",20,"bold"),bg="teal",fg="black").place(x=0,y=10,relwidth=1)
footerlbl1=Label(footer_frame,text="Developed By Suraj Yadav",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=0,y=75,relwidth=1)
footerlbl2=Label(footer_frame,text="Contact",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=1100,y=5)
footerlbl3=Label(footer_frame,text="Mobile No : 9792440259\n Email : surajpatnaghatt@gmail.com",font=("times new roman",15),bg="teal",fg="black").place(x=1000,y=35)
footerlbl4=Label(footer_frame,text="(4425)-Government Polytechnic Mau",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=20,y=5)
        
footerlbl5=Label(footer_frame,text="Address : Kandheri Mau-275101\nEmail : gpmaunew@gmail.com\n Website : www.gpmau.20m.com ",font=("times new roman",12,"bold")
                              ,bg="teal",fg="black").place(x=20,y=30)
footerlbl7=Label(footer_frame,text="",font=("times new roman",15),bg="teal",fg="black").place(x=20,y=35)



root.mainloop()
