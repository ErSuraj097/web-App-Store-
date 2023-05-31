from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Login :
    def __init__(self, root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="lightsteelblue")
        self.root.resizable(False,False)
        #bg image
        self.bg=ImageTk.PhotoImage(file="image/abc.jpeg")
        bg= Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #self.bg2=ImageTk.PhotoImage(file="image/qr2.jpg")
        #img_lbl=Label(self.root,image=self.bg2,bg="dodgerblue").place(x=110,y=150,height=340,width=500)

         #......ImageFRame
        self.img1=ImageTk.PhotoImage(file='image\qr_code1.jpg')
        self.img2=ImageTk.PhotoImage(file='image\qrcode1.jpg')
        self.img3=ImageTk.PhotoImage(file='image\gpm11.jpeg')
        #Frame.....Image....Label
        frame_1=Frame(self.root)
        frame_1.place(x=110,y=150,width=600,height=340)
        
        self.lbl1=Label(frame_1,image=self.img1,bd=0)
        self.lbl1.place(x=0,y=0)
        self.lbl2=Label(frame_1,image=self.img2,bd=0)
        self.lbl2.place(x=0,y=0)
        self.lbl3=Label(frame_1,image=self.img3,bd=0)
        self.lbl3.place(x=0,y=0)
        
        self.slider_func()
        #.........Frame

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=700,y=150,height=340,width=500)

        lbl2=Label(self.root,text="QR Code",font=("Goudy old style",35,"bold"),bg="lightsteelblue",fg="red").place(x=10,y=0)
        lbl2=Label(self.root,text="GENERATOR",font=("Goudy old style",15,"bold"),bg="lightsteelblue",fg="red").place(x=84,y=50)

        title=Label(Frame_login,text="Login Here",font=("Impact",30,"bold"),bg="white",fg="red").place(x=90,y=30)
        desc=Label(Frame_login,text="Student Login Area",font=("Goudy old style",15,"bold"),bg="white",fg="red").place(x=90,y=100)
        lbl=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)
        #............password
        lbl2=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),bg="white",fg="gray").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

       

        #button..........
        forget=Button(Frame_login,command=self.forget_pass,text="Forget Password?",bg="white",fg="red",font=("times new roman",12),cursor="hand2",bd=0).place(x=300,y=280)
        
        #newRegister=Button(Frame_login,command=self.Register,text="New Register Here?",bg="white",fg="red",font=("times new roman",12),cursor="hand2",bd=0).place(x=90,y=280)
        
        login=Button(self.root,text="Login",fg="white",bg="red",font=("times new roman",20),command=self.login_fun,cursor="hand2").place(x=860,y=470,width=180,height=40)
        login2=Button(self.root,text="QR Code Generator",fg="white",bg="red",font=("times new roman",20),cursor="hand2").place(x=260,y=470,height=40)

        
        foter_Frame=Frame(self.root,bg="black").place(x=0,y=600,width=1350,height=150)

        lbl2=Label(foter_Frame,text="Developed By Suraj Yadav",font=("Goudy old style",10),bg="black",fg="white").place(x=0,y=670,relwidth=1)
        lbl2=Label(foter_Frame,text="Contact",font=("Goudy old style",10,"bold"),bg="black",fg="white").place(x=1180,y=610)
        lbl2=Label(foter_Frame,text="Mobile No : 9792440259\nEmail : surajpatnaghatt@gmail.com\n",font=("Goudy old style",10),bg="black",fg="white").place(x=1100,y=630)
        lbl2=Label(foter_Frame,text="QR Code Generator",font=("Goudy old style",12,"bold"),bg="black",fg="white").place(x=15,y=610)

        
        

    def slider_func(self):
        

            self.im=self.img1
            self.img1=self.img2
            self.img2=self.img3
            self.img3=self.im
            #self.lbl1.config(image=self.img1)
            self.lbl3.config(image=self.im)
            
            self.lbl3.after(2000,self.slider_func)

        
    def forget_pass(self):
        self.root.destroy()
        import forgetPassword



    def Register(self):
        self.root.destroy()
        import Register

    #def qr_code_Generator(self):
        
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
                    import qr_code_generator
                    #messagebox.showinfo("Success","Welcome",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to:{str(es)}",parent=self.root)

        
                #messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}")'''
        
root=Tk()
obj=Login(root)
root.mainloop()
