from tkinter import *
from tkcalendar import *
import tkinter.messagebox
import datetime
from tkinter import ttk
def start():
    root=Tk()
    root.geometry("1000x750")
    root.title(" "*150+"bus")
    return root

def login(root):
    def log():
        mf.destroy()
        mainui(root)
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
    e1=Entry(lf,font=("Times",20,'bold'),textvariable=username,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e1.grid(row=0,column=1)
    l2=Label(lf,font=("Times",20,'bold'),text="Password :",bd=7,width=8,pady=25)
    l2.grid(row=1,column=0)
    passw=StringVar()
    e2=Entry(lf,font=("Times",20,'bold'),textvariable=passw,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e2.grid(row=1,column=1)
    but1=Button(lf,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=2,column=0)
    but2=Button(lf,bd=4,width=10,height=1,bg='white',command=reg,text="register",font=("Times",20,'bold'))
    but2.grid(row=2,column=1)
    root.mainloop()
def register(root):
    def log():
        mf.destroy()
        login(root)
    def reg():
        mf.destroy()
        login(root)
    mf=Frame(root,padx=240,pady=50,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=100,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="Register",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=500,height=500,relief=RIDGE)
    canvas = Canvas(lf)
    scrollbar = Scrollbar(lf, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    lf.grid(row=1,column=0)
    content = Frame(canvas)
    canvas.create_window((0, 0), window=content, anchor="nw")
    a=["Company Name","User Name","Password","Phno","Address","City","District","State","Terms"]
    b=[StringVar() for i in a]
    tef=Frame(canvas,bd=10,padx=15)     
    tef.grid(row=0,column=0)
    for i in range(len(a)):
        lab=Label(tef,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=0)
        if i!=len(a)-1:
            ent=Entry(tef,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
            ent.grid(row=i,column=1)
        else:
            tearea=Text(tef,font=("Times",20,'bold'),bd=5,width=15,height=2,bg='powder blue',relief=RIDGE)
            tearea.grid(row=i,column=1)
    but1=Button(tef,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=0)
    but2=Button(tef,bd=4,width=10,height=1,bg='white',command=reg,text="register",font=("Times",20,'bold'))
    but2.grid(row=len(a),column=1)
    root.mainloop()
def mainui(root):
    mf=Frame(root,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=200,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="Company",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=980,height=627,relief=RIDGE)
    lf.grid(row=1,column=0)
    llf=Frame(lf,bd=10,width=225,height=627,relief=RIDGE)
    llf.grid(row=0,column=0)
    rlf=Frame(lf,bd=10,width=700,height=600,relief=RIDGE)
    rlf.grid(row=0,column=1)
    rlf.configure(height=rlf["height"],width=rlf["width"])
    rlf.grid_propagate(0)
    canvas = Canvas(rlf)
    scrollbar = Scrollbar(rlf, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    content = Frame(canvas)
    canvas.create_window((0, 0), window=content, anchor="nw")
    tef=Frame(canvas,bd=10)     
    tef.grid(row=0,column=0)
    tef.configure(height=rlf["height"],width=rlf["width"])
    tef.grid_propagate(0)
    
root=start()
login(root)