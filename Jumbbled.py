
from tkinter import *
import random
from tkinter import messagebox
from PIL import Image ,ImageTk

root = Tk()
root.geometry("1300x700+0+0")
root.title("Jumbbled | Developed By Suraj Yadav")
root.configure(background = "whitesmoke")

# you can add more words as per your requirement
answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
    "polytechnic",
    "mau",
    "government"
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
    "techpolynic",
    "aum",
    "mentgover"
]

# I have improvised the code by using len(words)
num =  random.randrange(0, len(words), 1)

#.....................Function ....................
def default():
    global words,answers,num
    lbl.config(text = words[num])

def res():
    global words,answers,num
    num = random.randrange(0, len(words), 1)
    lbl.config(text = words[num])
    e1.delete(0, END)


def checkans():
    global words,answers,num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is a correct answer")
        res()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)
def slider_func():
        
            global img1,img2,img3,img4
            im=img1
            img1=img2
            img2=img3
            img3=img4
            img4=im
            #self.lbl1.config(image=self.img1)
            lbl3.config(image=im)
            
            lbl3.after(2000,slider_func)
def home():
    root.destroy()
    import First_Page
def back():
    root.destroy()
    import Second_Page

'''  #..........slider_ Image.............
img1=ImageTk.PhotoImage(file='image\qr_code1.jpg')
img2=ImageTk.PhotoImage(file='image\qrcode1.jpg')

img3=ImageTk.PhotoImage(file='image\gpm11.jpeg')
img4=ImageTk.PhotoImage(file='image\gpm1.jpg')
        #Frame.....Image....Label
frame_1=Frame(root)
frame_1.place(x=100,y=200,width=650,height=350)
        
lbl1=Label(frame_1,image=img1,bd=0)
lbl1.place(x=0,y=0)
lbl2=Label(frame_1,image=img2,bd=0)
lbl2.place(x=0,y=0)
lbl3=Label(frame_1,image=img3,bd=0)
lbl3.place(x=0,y=0)
        #self.img1=ImageTk.PhotoImage(file='qr_code1.jpg')

        
slider_func()'''
#............Title_Label.....................
title_lbl1=Label(root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
title_lbl1=Label(root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

title_lbl1=Label(root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

txt_lbl=Label(root,text="Guess Text Game Application",font=("times new roman",30,"bold"),bg="whitesmoke",fg="navy").place(x=50,y=140,)

#............Logo_Image..........        
logo=ImageTk.PhotoImage(file="image/up1.png")
image_lbl=Label(root,image=logo,bd=0).place(x=20,y=0)
#............Side_Image............
photo=ImageTk.PhotoImage(file="image/side11.png")
label_image=Label(root,image=photo)
label_image.place(x=50,y=250)

#...............Frame_Guess_The_Text.....
que_Frame=Frame(root,bg="white",bd=5,relief=RIDGE)
que_Frame.place(x=700,y=200,width=500,height=350)

lbl = Label( que_Frame, text = "Your here",  font = ("Verdana", 20), bg = "white",  fg = "black",)
lbl.place(x=0,y=20,relwidth=1)

ans1 = StringVar()
e1 = Entry(que_Frame,font = ("Verdana", 20),bg="whitesmoke",textvariable = ans1,)
e1.place(x=100,y=60,width=300)

btncheck = Button( que_Frame, text = "Check", font = ("Comic sans ms", 16), width = 16, bg = "dodgerblue", fg = "white",bd=5, relief = RIDGE, command = checkans,)
btncheck.place(x=140,y=130)

btnreset = Button( que_Frame, text = "Reset", font = ("Comic sans ms", 16), width = 16, bg = "red", fg = "white", bd=5,relief = RIDGE, command = res,)
btnreset.place(x=140,y=200)
#......................End_Frame...............

button=Button(root,text="Home Page",font=("times new roman",15,"bold"),command=home,bg="gold",fg="white",bd=0,cursor="hand2")
button.place(x=50,y=190,width=280,height=40)
button=Button(root,text="Back",font=("times new roman",15,"bold"),command=back,bg="dodgerblue",fg="white",bd=0,cursor="hand2")
button.place(x=370,y=190,width=280,height=40)
#.............Footer_Label..............
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

default()
root.mainloop()
