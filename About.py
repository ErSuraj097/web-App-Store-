from tkinter import*
from PIL import ImageTk 

class slider():
    def __init__(self,root):
        self.root=root
        self.root.title("Home | Developed By Suraj Yadav")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="whitesmoke")
        self.root.focus_force()
        self.root.resizable(False,False)

        self.title_lbl1=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
        self.title_lbl1=Label(self.root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

        self.title_lbl1=Label(self.root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

        self.txt_lbl=Label(self.root,text=" Web Application Store",font=("times new roman",30,"bold"),bg="whitesmoke",fg="navy").place(x=170,y=100,)

        
        self.logo=ImageTk.PhotoImage(file="image/up1.png")
        image_lbl=Label(self.root,image=self.logo,bd=0).place(x=20,y=0)
        
        dlp_frame=Frame(self.root,bg='white')
        dlp_frame.place(x=650,y=170,width=600,height=400)
        self.image=ImageTk.PhotoImage(file="image/suraj_img11.png")
        image_lbl=Label(dlp_frame,image=self.image,bd=0).place(x=0,y=0)

        '''self.image=ImageTk.PhotoImage(file="image/side1.png")
        image_lbl=Label(self.root,image=self.image,bd=0).place(x=10,y=200)

        #..............Rules............
        self.txt_lbl1=Label(self.root,text="Rules:-\n",font=("times new roman",15,"bold"),bg="whitesmoke",fg="black").place(x=10,y=465,width=100)
        self.txt_lbl2=Label(self.root,text="Step 1 - First Registration Here",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=500,)
        self.txt_lbl3=Label(self.root,text="Step 2 - Login with Username & Password",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=530,)
        self.txt_lbl4=Label(self.root,text="Step 3 - Access Application",font=("times new roman",15),bg="whitesmoke",fg="black").place(x=40,y=560,)

        
        #..........slider_ Image.............
        self.img1=ImageTk.PhotoImage(file='image\qr_code1.jpg')
        self.img2=ImageTk.PhotoImage(file='image\qrcode1.jpg')

        self.img3=ImageTk.PhotoImage(file='image\gpm11.jpeg')
        self.img4=ImageTk.PhotoImage(file='image\gpm1.jpg')
        #Frame.....Image....Label
        frame_1=Frame(self.root)
        frame_1.place(x=640,y=200,width=650,height=350)
        
        self.lbl1=Label(frame_1,image=self.img1,bd=0)
        self.lbl1.place(x=0,y=0)
        self.lbl2=Label(frame_1,image=self.img2,bd=0)
        self.lbl2.place(x=0,y=0)
        self.lbl3=Label(frame_1,image=self.img3,bd=0)
        self.lbl3.place(x=0,y=0)
        '''
        
        #............Frame..................Label
        self.footer_frame=Frame(self.root,bg='teal')
        self.footer_frame.place(x=0,y=600,width=1300,height=100)

        self.footerlbl6=Label(self.footer_frame,text="Complete Mini Project 2020-21",font=("times new roman",20,"bold"),bg="teal",fg="black").place(x=0,y=10,relwidth=1)
        self.footerlbl1=Label(self.footer_frame,text="Developed By Suraj Yadav",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=0,y=70,relwidth=1)
        self.footerlbl2=Label(self.footer_frame,text="Contact",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=1100,y=5)
        self.footerlbl3=Label(self.footer_frame,text="Mobile No : 9792440259\n Email : surajpatnaghatt@gmail.com",font=("times new roman",15),bg="teal",fg="black").place(x=1000,y=35)
        self.footerlbl4=Label(self.footer_frame,text="(4425)-Government Polytechnic Mau",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=20,y=5)
        
        self.footerlbl5=Label(self.footer_frame,text="Address : Kandheri Mau-275101\nEmail : gpmaunew@gmail.com\n Website : www.gpmau.20m.com ",font=("times new roman",12,"bold")
                              ,bg="teal",fg="black").place(x=20,y=30)
        
        self.footerlbl7=Label(self.footer_frame,text="",font=("times new roman",15),bg="teal",fg="black").place(x=20,y=35)
       

        #................Button...........
        '''self.btn=Button(self.root,command=self.reg,text="Register",font=("times new roman",17,"bold"),fg="white",bg="dodgerblue",cursor="hand2",bd=0).place(x=640,y=150,width=200,height=40)
        self.btn=Button(self.root,command=self.login,text="Login",font=("times new roman",17,"bold"),fg="white",bg="crimson",cursor="hand2",bd=0).place(x=860,y=150,width=200,height=40)
        self.btn=Button(self.root,command=self.game,text="About",font=("times new roman",17,"bold"),fg="white",bg="gold",cursor="hand2",bd=0).place(x=1080,y=150,width=200,height=40)
        
        
        #self.btn=Button(self.root,text="QR Code Generate",font=("times new roman",12,"bold"),fg="white",bg="red",cursor="hand2").place(x=1090,y=150,width=200)

        #self.image11=ImageTk.PhotoImage(file='reg21.png')
        #self.btn_lbl=Label(self.root,image=self.image11).place(x=90,y=480)
        #...........

        
        self.slider_func()
        
    #............Function............

    def slider_func(self):
        

            self.im=self.img1
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.img4
            self.img4=self.im
            
            self.lbl3.config(image=self.im)
            
            self.lbl3.after(2000,self.slider_func)'''


            #....................
    def reg(self):
        self.root.destroy()
        import Register

    def login(self):
        self.root.destroy()
        import login

    def game(self):
        self.root.destroy()
        import About
    

        
        

root=Tk()
obj=slider(root)
root.mainloop()
