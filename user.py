from tkinter import *
from tkcalendar import *
from tkinter import ttk
from dbms import *
import os
from functools import partial

pa=os.environ["dbpass"]
mycon=setup("localhost","root",pa,"bus_demo")

def start():
    root=Tk()
    root.geometry("1000x750")
    root.title(" "*150+"bus")
    return root

def login(root):
    def log():
        res=get_user(mycon,username.get(),passw.get()) 
        if res:
            print(res[0][0])    
    def reg():
        mf.destroy()
        register(root)
    mf=Frame(root,padx=240,pady=150,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=100,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="LOGIN",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=500,height=500,relief=RIDGE,padx=43,pady=50)
    lf.grid(row=1,column=0)
    l1=Label(lf,font=("Times",20,'bold'),text="User name :",bd=7,width=8,pady=15)
    l1.grid(row=0,column=0)
    username=StringVar()
    e1=Entry(lf,font=("Times",20,'bold'),textvariable=username,show="*",bd=5,width=15,bg='powder blue',relief=RIDGE)
    e1.grid(row=0,column=1)
    l2=Label(lf,font=("Times",20,'bold'),text="Password :",bd=7,width=8,pady=25)
    l2.grid(row=1,column=0)
    passw=StringVar()
    e2=Entry(lf,font=("Times",20,'bold'),show="*",textvariable=passw,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e2.grid(row=1,column=1)
    but1=Button(lf,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=2,column=0)
    but2=Button(lf,bd=4,width=10,height=1,bg='white',command=reg,text="register",font=("Times",20,'bold'))
    but2.grid(row=2,column=1)
    root.mainloop()
def register(root):
    a=["uname","pas","fname","phno","emphno","doorno","address","city","district","state","sex","mailid","dob","aadhaar"]
    b=[StringVar() for i in a]
    def log():
        mf.destroy()
        login(root)
    def reg():
        insert_user(mycon,b[0].get(),b[1].get(),b[2].get(),int(b[3].get()),int(b[4].get()),int(b[5].get()),b[6].get(),b[7].get(),b[8].get(),b[9].get(),b[10].get(),b[11].get(),b[12].get(),int(b[13].get()))
        mf.destroy()
        login(root)
    mf=Frame(root,padx=260,pady=65,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=100,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="Register",bd=7)
    lbt.grid(row=0,column=0)
    
    rlf=Frame(mf,bd=10,width=400,height=500,relief=RIDGE)
    rlf.configure(height=rlf["height"],width=rlf["width"])
    rlf.grid_propagate(0)

    mycanvas=Canvas(rlf,bd=10,width=400,height=480)
    mycanvas.pack(side=LEFT)

    yscroll=ttk.Scrollbar(rlf,orient="vertical",command=mycanvas.yview)
    yscroll.pack(side=RIGHT,fill="y")

    mycanvas.configure(yscrollcommand=yscroll.set)

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    myframe=Frame(mycanvas,bd=10,width=400,height=500)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=1,column=0)

    for i in range(len(a)):
        lab=Label(myframe,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=0)
        ent=Entry(myframe,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
        ent.grid(row=i,column=1)
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=0)
    but2=Button(myframe,bd=4,width=10,height=1,bg='white',command=reg,text="register",font=("Times",20,'bold'))
    but2.grid(row=len(a),column=1)
    root.mainloop()

root=start()
login(root)