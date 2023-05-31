from tkinter import*
from PIL import ImageTk 

class slider():
    def __init__(self,root):
        self.root=root
        self.root.title("Web Application | Developed By Suraj Yadav")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="whitesmoke")
        self.root.focus_force()
        self.root.resizable(False,False)
        

        self.title_lbl1=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
        self.title_lbl1=Label(self.root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

        self.title_lbl1=Label(self.root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

        self.txt_lbl=Label(self.root,text=" Web Application",font=("Impact",35,"bold"),bg="whitesmoke",fg="navy").place(x=100,y=200,)

        
        
        
        self.logo=ImageTk.PhotoImage(file="image/up1.png")
        image_lbl=Label(self.root,image=self.logo,bd=0).place(x=20,y=0)
    
        #self.image=ImageTk.PhotoImage(file="image/side1.png")
        #image_lbl=Label(self.root,image=self.image,bd=0).place(x=0,y=200)

        '''self.txt_lbl1=Label(self.root,text="Rules:-\n",font=("times new roman",15,"bold"),bg="whitesmoke",fg="black").place(x=10,y=465,width=100)
        self.txt_lbl2=Label(self.root,text="Step 1 - First Registration Here",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=500,)
        self.txt_lbl3=Label(self.root,text="Step 2 - Login with Username & Password",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=530,)
        self.txt_lbl4=Label(self.root,text="Step 3 - Application",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=560,)'''

        
        
        
        
        #slider1
        self.img1=ImageTk.PhotoImage(file='image\qr_code1.jpg')
        self.img2=ImageTk.PhotoImage(file='image\qrcode1.jpg')
        self.img3=ImageTk.PhotoImage(file='image\gpm11.jpeg')
        #Frame.....Image....Label
        frame_1=Frame(self.root)
        frame_1.place(x=640,y=200,width=650,height=350)
        
        self.lbl1=Label(frame_1,image=self.img1,bd=0)
        self.lbl1.place(x=0,y=0)
        self.lbl2=Label(frame_1,image=self.img2,bd=0)
        self.lbl2.place(x=0,y=0)
        self.lbl3=Label(frame_1,image=self.img3,bd=0)
        self.lbl3.place(x=0,y=0)
        
        
        self.slider_func()
        
        #............Frame
        self.footer_frame=Frame(self.root,bg='teal')
        self.footer_frame.place(x=0,y=600,width=1300,height=100)

        self.footerlbl6=Label(self.footer_frame,text="Complete Mini Project 2020-21",font=("times new roman",20,"bold"),bg="teal",fg="black").place(x=0,y=10,relwidth=1)
        self.footerlbl1=Label(self.footer_frame,text="Developed By Suraj Yadav",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=0,y=75,relwidth=1)
        self.footerlbl2=Label(self.footer_frame,text="Contact",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=1100,y=5)
        self.footerlbl3=Label(self.footer_frame,text="Mobile No : 9792440259\n Email : surajpatnaghatt@gmail.com",font=("times new roman",15),bg="teal",fg="black").place(x=1000,y=35)
        self.footerlbl4=Label(self.footer_frame,text="(4425)-Government Polytechnic Mau",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=20,y=5)
        
        self.footerlbl5=Label(self.footer_frame,text="Address : Kandheri Mau-275101\nEmail : gpmaunew@gmail.com\n Website : www.gpmau.20m.com ",font=("times new roman",12,"bold")
                              ,bg="teal",fg="black").place(x=20,y=30)
        
        
        #.......Label..
        self.btn=Button(self.root,command=self.qr_code,text="QR Generator",font=("times new roman",17,"bold"),fg="white",bg="deepskyblue",cursor="hand2",bd=0).place(x=70,y=300,width=400,height=40)
        self.btn=Button(self.root,command=self.age,text="Age Calculator",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=70,y=350,width=400,height=40)
        self.btn=Button(self.root,command=self.jumbbled,text="Jumbbled",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=70,y=400,width=400,height=40)
        self.btn=Button(self.root,command=self.Clock,text="DigitalClock",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=70,y=450,width=400,height=40)
        #.........
        self.btn=Button(self.root,command=self.home,text="Home",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=640,y=150,width=200,height=40)
        self.btn=Button(self.root,text="Contact ",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=850,y=150,width=200,height=40)
        self.btn=Button(self.root,text="About",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=1060,y=150,width=200,height=40)
        #self.image11=ImageTk.PhotoImage(file='image/reg21.png')
        #self.btn_lbl=Label(self.root,image=self.image11,cursor="hand2").place(x=340,y=450)

        lblfetch=Label(self.root,text="")
        lblfetch.place(x=100,y=200)

    def slider_func(self):
        

            self.im=self.img1
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.im
            self.lbl3.config(image=self.im)
            self.lbl3.after(2000,self.slider_func)


    #..........Fuction ...........

    def qr_code(self):
        self.root.destroy()
        
        import qr_code_generator
    def age(self):
        self.root.destroy()
        import Age_Calc
        
    def jumbbled(self):
        self.root.destroy()
        import Jumbbled

    def Clock(self):
        self.root.destroy()
        import digital_clock
    
    
    def home(self):
        self.root.destroy()
        import First_Page

        
        

root=Tk()
obj=slider(root)
root.mainloop()
