from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Login :
    def __init__(self, root):
        self.root=root
        self.root.title("Login Window | Developed By Suraj Yadav")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="whitesmoke")
        self.root.focus_force()
        self.root.resizable(False,False)
        #bg image
        #self.bg=ImageTk.PhotoImage(file="image/img.jpg")
        #bg= Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        self.title_lbl1=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
        self.title_lbl1=Label(self.root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

        self.title_lbl1=Label(self.root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

        #self.txt_lbl=Label(self.root,text=" QR Code Generator Application",font=("times new roman",30,"bold"),bg="whitesmoke",fg="navy").place(x=20,y=150,)

        self.logo=ImageTk.PhotoImage(file="image/up1.png")
        image_lbl=Label(self.root,image=self.logo,bd=0).place(x=20,y=0)
        self.image=ImageTk.PhotoImage(file="image/side11.png")
        image_lbl=Label(self.root,image=self.image,bd=0).place(x=600,y=200)



        Frame_login=Frame(self.root,bg="white",bd=5,relief=GROOVE)
        Frame_login.place(x=100,y=200,height=340,width=500)

        title=Label(Frame_login,text="Login Here",font=("Impact",30,"bold"),bg="white",fg="red").place(x=90,y=30)
        desc=Label(Frame_login,text="Student Login Area",font=("Goudy old style",15,"bold"),bg="white",fg="red").place(x=90,y=100)
        lbl=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        #............password
        lbl2=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)


        self.img1=ImageTk.PhotoImage(file='image\qr_code1.jpg')
        self.img2=ImageTk.PhotoImage(file='image\qrcode1.jpg')
        self.img3=ImageTk.PhotoImage(file='image\gpm11.jpeg')
             #Frame.....Image....Label
        #frame_1=Frame(self.root)
        #frame_1.place(x=640,y=150,width=640,height=340)
        
        #self.lbl1=Label(frame_1,image=self.img1,bd=0)
        #self.lbl1.place(x=0,y=0)
        #self.lbl2=Label(frame_1,image=self.img2,bd=0)
        #self.lbl2.place(x=0,y=0)
        #self.lbl3=Label(frame_1,image=self.img3,bd=0)
        #self.lbl3.place(x=0,y=0)
        #self.img1=ImageTk.PhotoImage(file='qr_code1.jpg')
        #self.slider_func()
        #button..........
        
        
        newRegister=Button(Frame_login,command=self.Register,text="Register New Account?",bg="white",fg="red",font=("times new roman",12),cursor="hand2",bd=0).place(x=90,y=280)
        
        login=Button(self.root,text="Login",fg="white",bg="red",font=("times new roman",20),command=self.login_fun,cursor="hand2").place(x=250,y=520,width=180,height=40)

        forget=Button(Frame_login,command=self.forget_password_window,text="Forget Password?",bg="white",fg="red",font=("times new roman",12),cursor="hand2",bd=0).place(x=300,y=280)

        #.............Footer
        self.footer_frame=Frame(self.root,bg='teal')
        self.footer_frame.place(x=0,y=600,width=1300,height=100)

        self.footerlbl6=Label(self.footer_frame,text="Complete Mini Project 2020-21",font=("times new roman",20,"bold"),bg="teal",fg="black").place(x=0,y=10,relwidth=1)
        self.footerlbl1=Label(self.footer_frame,text="Developed By Suraj Yadav",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=0,y=75,relwidth=1)
        self.footerlbl2=Label(self.footer_frame,text="Contact",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=1100,y=5)
        self.footerlbl3=Label(self.footer_frame,text="Mobile No : 9792440259\n Email : surajpatnaghatt@gmail.com",font=("times new roman",15),bg="teal",fg="black").place(x=1000,y=35)
        self.footerlbl4=Label(self.footer_frame,text="(4425)-Government Polytechnic Mau",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=20,y=5)
        
        self.footerlbl5=Label(self.footer_frame,text="Address : Kandheri Mau-275101\nEmail : gpmaunew@gmail.com\n Website : www.gpmau.20m.com ",font=("times new roman",12,"bold")
                              ,bg="teal",fg="black").place(x=20,y=30)
        
        self.footerlbl7=Label(self.footer_frame,text="",font=("times new roman",15),bg="teal",fg="black").place(x=20,y=35)

        #.................

        

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_pass.delete(0,END)
        self.txt_user.delete(0,END)
        
    def forget_password(self):
        if self.cmb_quest.get()=="select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="":
            messagebox.showerror("Error","All Fields Are Required",self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and question=%s and answer=%s",(self.txt_user.get(),self.cmb_quest.get(),self.txt_answer.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please Select The Correct Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=%s where email=%s",(self.txt_new_password.get(),self.txt_user.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Password has been set,Please login with new Password",parent=self.root2)
                    #row2=cur.fetchone()
                    self.reset()
                    self.root2.destroy()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)
                

    def forget_password_window(self):
        if self.txt_user.get()=="":
            messagebox.showerror("Error","Please Enter Username to Reset Your Password",parent=self.root)
        else:
             try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s ",self.txt_user.get())
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Please Enter Valid Username to Reset Your Password",parent=self.root)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+600+150")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")
                    self.root2.resizable(False,False)

                    t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
                    #................forget_password
                    question=Label(self.root2,text="Security Question",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=80)  

                    self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cmb_quest['value']=("select","Your First Pet Name","Your Birth Place","Your Best Friend")
                    self.cmb_quest.place(x=50,y=110,width=250)
                    self.cmb_quest.current(0)

                    answer =Label(self.root2,text="Answer",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=160)
                    self.txt_answer=Entry(self.root2,font=("times new roman",15),bg ="lightgray")
                    self.txt_answer.place(x=50,y=190,width=250)

                    new_password =Label(self.root2,text="New Password",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=250)
                    self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg ="lightgray")
                    self.txt_new_password.place(x=50,y=280,width=250)

                    btn_chnage_password=Button(self.root2,command=self.forget_password,text="Reset Password",fg="white",bg="red",font=("times new roman",15),cursor="hand2").place(x=100,y=340)

                    
                    
             except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)
                
            
        
             '''self.root2=Toplevel()
             self.root2.title("Forget Password")
             self.root2.geometry("350x400+600+150")
             self.root2.focus_force()
             self.root2.grab_set()
             self.root2.config(bg="white")

             t=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)
             #................forget_password
             question=Label(self.root2,text="Security Question",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=80)  

             self.cmb_quest=ttk.Combobox(self.root2,font=("times new roman",13),state="readonly",justify=CENTER)
             self.cmb_quest['value']=("select","Your First Pet Name","Your Birth Place","Your Best Friend")
             self.cmb_quest.place(x=50,y=110,width=250)
             self.cmb_quest.current(0)

             answer =Label(self.root2,text="Answer",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=160)
             self.txt_answer=Entry(self.root2,font=("times new roman",15),bg ="lightgray")
             self.txt_answer.place(x=50,y=190,width=250)

             new_password =Label(self.root2,text="New Password",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=250)
             self.txt_new_password=Entry(self.root2,font=("times new roman",15),bg ="lightgray")
             self.txt_new_password.place(x=50,y=280,width=250)

             btn_chnage_password=Button(self.root2,text="Reset Password",fg="white",bg="red",font=("times new roman",15),cursor="hand2").place(x=100,y=340)
                
             '''
             
    def slider_func(self):
            self.im=self.img1
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.im
            #self.lbl1.config(image=self.img1)
            self.lbl3.config(image=self.im)
            
            self.lbl3.after(2000,self.slider_func)



    
    def Register(self):
        self.root.destroy()
        import Register

        
    def login_fun(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        #elif self.txt_pass.get()!="12345"or self.txt_user.get()!="Suraj":
            #messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.txt_user.get(),self.txt_pass.get()))
                row=cur.fetchone()
                #print(row)
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                else:
                    self.root.destroy()
                    import Second_Page
                    #messagebox.showinfo("Success","Welcome",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)
                #messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}")
        
root=Tk()
obj=Login(root)
root.mainloop()
