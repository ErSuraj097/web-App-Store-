from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql
import datetime
#import 

class Register :
    def __init__(self, root):
        self.root=root
        self.root.title("Registration Window | Developed By Suraj Yadav")
        self.root.geometry("1300x700+0+0")
        self.root.config(bg="wheat")
        self.root.resizable(0,0)
        #bg image
        #self.bg=ImageTk.PhotoImage(file="image/abc.jpeg")
        #bg= Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.title_lbl1=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="wheat",fg="crimson").place(x=0,y=5,width=1100)
        self.title_lbl1=Label(self.root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="wheat",fg="crimson").place(x=900,y=30)

        #self.title_lbl1=Label(self.root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)
       

        
        #bg Left image..........
        self.left=ImageTk.PhotoImage(file="image/sa1.jpg")
        left= Label(self.root,image=self.left,bg="teal").place(x=80,y=100,width=400,height=480)
        title= Label(self.root,text=" BOARD OF TECHNICAL EDUCATION\nUTTAR PRADESH ",font=("Impact",20,"bold"),bg="teal",fg="white").place(x=80,y=140)
        title2= Label(self.root,text="\t\t\tAICTE",font=("times new roman",10,"italic","bold"),bg="teal",fg="white").place(x=85,y=210)


        #.............current_Date_Time...........
        self.time=datetime.datetime.now()
        
        time= Label(self.root,text=self.time.strftime("Date : %d-%m-%Y   "),font=("times new roman",15),bg="wheat",fg="crimson").place(x=10,y=10)
            
        
        
        #frame.......

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=480)

        title =Label(frame1,text="REGISTRATION HERE",font =("times new roman",20,"bold"),bg="white",fg="red").place(x=50,y=30)
        #..............row1
        #self.var_fname=StringVar()
        f_name =Label(frame1,text="First Name",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name =Label(frame1,text="Last Name",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        #------------------row2

        contact=Label(frame1,text="Contact",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email =Label(frame1,text="Email",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        #------------------row3

        question=Label(frame1,text="Security Question",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)  

        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cmb_quest['value']=("select","Your First Pet Name","Your Birth Place","Your Best Friend")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer =Label(frame1,text="Answer",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        #.............row5
        password=Label(frame1,text="Password",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword =Label(frame1,text="Confirm Password",font =("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg ="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        # Check box
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Term & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12),bg="white",cursor="hand2").place(x=50,y=380)

        #..........button
        #self.btn_img=ImageTk.PhotoImage(file="image/reg2.png")
        #btn=Button (frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.reg_data).place(x=50,y=420,height=30,width=180)
        btn_reg=Button (frame1,text="Register Here",font=("times new roman",15),bg="red",fg="white",bd=0,cursor="hand2",command=self.reg_data).place(x=50,y=420,width=180)

        btn_login=Button (self.root,command=self.login_window,text="Sign In",font=("times new roman",15),bg="red",fg="white",cursor="hand2").place(x=180,y=460,width=200)

        btn_home=Button (self.root,command=self.homepage,text="Click Here..Home Page",font=("times new roman",15),bg="teal",fg="white",cursor="hand2",bd=0).place(x=250,y=540,width=200)

        #slider.......

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

        #..........
    def homepage(self):
        root.destroy()
        import First_Page
        
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
    def login_window(self):
        self.root.destroy()
        import login
        #import forget_pass2
    def reg_data(self):
        
                #
                if self.txt_fname.get()==""or self.txt_email.get()==""or self.txt_email.get()=="select"or self.txt_answer.get()=="" or self.txt_password.get()==""or  self.txt_cpassword.get()=="" :
                    messagebox.showerror("error","All Fields Are Required",parent=self.root)
                elif self.txt_password.get()!=  self.txt_cpassword.get():
                    messagebox.showerror("error","Password & Confirm Password should be same",parent=self.root)
                elif self.var_chk.get()==0:
                    messagebox.showerror("error","Please Agree our term & condition",parent=self.root)
                else:
                    try:
                        con=pymysql.connect(host="localhost",user="root",password="",database="employee")
                        cur=con.cursor()
                        cur.execute("select* from employee where email=%s",self.txt_email.get())
                        row=cur.fetchone()
                        #print(row)
                        if row!=None:
                            messagebox.showerror("error","User Already Exist, Please try with another email ",parent=self.root)

                        else:
                            cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) value(%s,%s,%s,%s,%s,%s,%s)",
                                    (self.txt_fname.get(),
                                     self.txt_lname.get(),
                                     self.txt_contact.get(),
                                     self.txt_email.get(),
                                     self.cmb_quest.get(),
                                     self.txt_answer.get(),
                                     self.txt_password.get()
                                     )
                                    )
                            con.commit()
                            con.close()
                            messagebox.showinfo("success","Register Successful",parent=self.root)
                            self.clear()


                    except Exception as es:
                        messagebox.showerror("error",f"Error due to: {str(es)}",parent=self.root)
                        #messagebox.showinfo("success","Register Successful",parent=self.root)

                    '''self.txt_email.get(),
                  self.cmb_quest.get(),
                  self.txt_answer.get(),
                  self.txt_password.get(),
                  self.txt_cpassword.get())'''
        
root=Tk()
obj=Register(root)
root.mainloop()
