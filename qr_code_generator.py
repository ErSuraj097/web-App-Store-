from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from tkinter import ttk

class Qr_code_Generator:

    def __init__(self,root):

        self.root=root
        self.root.title("QR Generator | Developed By Suraj Yadav")
        self.root.geometry("1300x700+0+0")
        self.root.resizable(False ,False)
        self.root.config(bg='whitesmoke')
        self.root.focus_force()
        self.root.grab_set()

        
        self.title_lbl1=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=0,width=1100)
        self.title_lbl1=Label(self.root,text="UTTAR PRADESH",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=900,y=25)

        self.title_lbl1=Label(self.root,text=" Board Of Technical Education Uttar Pradesh",font=("times new roman",20,"bold"),bg="whitesmoke",fg="crimson").place(x=0,y=65,relwidth=1)

        self.txt_lbl=Label(self.root,text=" QR Code Generator Application",font=("Impact",20),bg="whitesmoke",fg="navy").place(x=200,y=110,)

        self.logo=ImageTk.PhotoImage(file="image/up1.png")
        image_lbl=Label(self.root,image=self.logo,bd=0).place(x=20,y=0)
        self.image=ImageTk.PhotoImage(file="image/bp11.png")
        image_lbl=Label(self.root,image=self.image,bd=0).place(x=20,y=220)

        #==========Student Details window
        self.var_stu_code=StringVar()
        self.var_stu_name=StringVar()
        self.var_stu_age=StringVar()
        self.var_stu_fathername=StringVar()
        
        stu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        stu_Frame.place(x=450,y=160,width=500,height=380)

        stu_title=Label(stu_Frame,text="Student Details",font=("Goudy old style",20),fg="white",bg="#043256").place(x=0,y=0,relwidth=1)


        #.........Label.........
        lbl_stu_id=Label(stu_Frame,text="Enrollment No",font=("times new roman",15),bg="white").place(x=20,y=60)
        lbl_stu_name=Label(stu_Frame,text="Name ",font=("times new roman",15),bg="white").place(x=20,y=100)
    
        lbl_stu_age=Label(stu_Frame,text="Father Name",font=("times new roman",15),bg="white").place(x=20,y=140)
        lbl_stu_fathername=Label(stu_Frame,text="Date of Birth",font=("times new roman",15),bg="white").place(x=20,y=180)

        #==========Entry=====
        txt_stu_id=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_code,bg="lightyellow").place(x=200,y=60)
        txt_stu_name=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_name,bg="lightyellow").place(x=200,y=100)
        txt_stu_fathername=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_fathername,bg="lightyellow").place(x=200,y=140)
        txt_stu_age=Entry(stu_Frame,text="dd/mm/yyyy",font=("times new roman",15),textvariable=self.var_stu_age,bg="lightyellow")
        #txt_stu_age.insert(END,'__/__/____')
        txt_stu_age.place(x=200,y=180)
        
        btn_gen=Button(stu_Frame,text="QR Generate",command=self.generate,font=("times new roman",18),bg="#2196f3",fg="white",cursor="hand2").place(x=90,y=250,width=180,height=30)

        btn_clear=Button(stu_Frame,text="Clear",command=self.clear,font=("times new roman",18),bg="#607d8b",fg="white",cursor="hand2").place(x=282,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(stu_Frame,text=self.msg,font=("times new roman",20),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #==========Student QR code window

        
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=1000,y=160,width=250,height=380)

        qr_title=Label(qr_Frame,text="Student QR Code",font=("Goudy old style",20),fg="white",bg="#043256").place(x=0,y=0,relwidth=1)
        
        self.qr_code=Label(qr_Frame,text="No QR \ Available",font=("times new roman",15),bg="lightyellow",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

        #........footer...
        self.footer_frame=Frame(self.root,bg='teal')
        self.footer_frame.place(x=0,y=600,width=1300,height=100)

        self.footerlbl6=Label(self.footer_frame,text="Complete Mini Project 2020-21",font=("times new roman",20,"bold"),bg="teal",fg="black").place(x=0,y=10,relwidth=1)
        self.footerlbl1=Label(self.footer_frame,text="Developed By Suraj Yadav",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=0,y=75,relwidth=1)
        self.footerlbl2=Label(self.footer_frame,text="Contact",font=("times new roman",15,"bold"),bg="teal",fg="black").place(x=1100,y=5)
        self.footerlbl3=Label(self.footer_frame,text="Mobile No : 9792440259\n Email : surajpatnaghatt@gmail.com",font=("times new roman",15),bg="teal",fg="black").place(x=1000,y=35)
        self.footerlbl4=Label(self.footer_frame,text="(4425)-Government Polytechnic Mau",font=("times new roman",12,"bold"),bg="teal",fg="black").place(x=20,y=5)
        
        self.footerlbl5=Label(self.footer_frame,text="Address : Kandheri Mau-275101\nEmail : gpmaunew@gmail.com\n Website : www.gpmau.20m.com ",font=("times new roman",12,"bold")
                              ,bg="teal",fg="black").place(x=20,y=30)

        #..............Home and Back Button
        btn_gen=Button(root,text="Home Page",command=self.home,font=("times new roman",15),bg="gold",fg="white",cursor="hand2",bd=0).place(x=20,y=160,width=190,height=30)
        btn_gen=Button(root,text="Back",command=self.back,font=("times new roman",15),bg="#2196f3",fg="white",cursor="hand2",bd=0).place(x=230,y=160,width=190,height=30)

    def home(self):
        self.root.destroy()
        import First_Page

    def back(self):
        self.root.destroy()
        import Second_Page

        #...............Generate data......
    def clear(self):
        self.var_stu_code.set('')
        self.var_stu_name.set('')
        self.var_stu_age.set('')
        self.var_stu_fathername.set('')
        
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        
        #...............Generate data......
    def generate(self):
        if self.var_stu_code.get()=="":
            '''or self.var_stu_name.get()=="" or self.var_stu_age.get()=="" or self.var_stu_fathername.get()=="":'''
            self.msg="All Fields Are Required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        
        else:
            qr_data=(f"{self.var_stu_code.get()}\n{self.var_stu_name.get()}\n{self.var_stu_fathername.get()}\n{self.var_stu_age.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student_QR"+str(self.var_stu_code.get())+'.png')
            #...........Qr Code Image Update.....
            self.im=ImageTk.PhotoImage(file="Student_QR"+str(self.var_stu_code.get())+'.png')
            self.qr_code.config(image=self.im)
            
            #............Updati notification.............
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg="green")
        
root=Tk()
obj=Qr_code_Generator(root)
root.mainloop()
