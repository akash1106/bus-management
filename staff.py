from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import *
from tkinter import ttk
from dbms import *
import os

pa=os.environ["dbpass"]
mycon=setup("localhost","root",pa,"bus_demo")
def start():
    root=Tk()
    root.geometry("1000x750")
    root.title(" "*150+"bus")
    return root
def login(root):
    image=Image.open("image.jpg")
    render = ImageTk.PhotoImage(image)
    def log():
        try:
            res=check_staff(mycon,username.get(),passw.get())
            if res:
                mf.destroy()
                mainui(root,res[0][1])
            else:
                messagebox.showwarning("login","no data match")
        except Exception as e:
            messagebox.showerror("Error",e)
    mf=Frame(root,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    img = Label(mf, image=render)
    img.image = render
    img.place(anchor="nw")
    tf=Frame(mf,bd=10,width=300,height=100,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0,padx=350,pady=(150,50))
    lbt=Label(tf,font=("Times",30,'bold'),text="LOGIN",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=500,height=500,relief=RIDGE,padx=43,pady=50,takefocus=True)
    lf.grid(row=1,column=0,padx=260,pady=(0,100))
    l1=Label(lf,font=("Times",20,'bold'),text="User name :",bd=7,width=8,pady=15)
    l1.grid(row=0,column=0)
    username=StringVar()
    e1=Entry(lf,font=("Times",20,'bold'),textvariable=username,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e1.grid(row=0,column=1)
    l2=Label(lf,font=("Times",20,'bold'),text="Password :",bd=7,width=8,pady=25)
    l2.grid(row=1,column=0)
    passw=StringVar()
    e2=Entry(lf,font=("Times",20,'bold'),show="*",textvariable=passw,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e2.grid(row=1,column=1)
    but1=Button(lf,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=2,column=0,columnspan=2)
    root.mainloop()
def mainui(root,bid):
    try:
        res=get_person_on_bus(mycon,bid)
        print(res)
    except Exception as e:
        messagebox.showerror("Error",e)
    select=[]
    def atten():
        try:
            for i in select:
                set_active(mycon,1,i)
        except Exception as e:
            messagebox.showerror("Error",e)
    def attendance():
        pass
    def change_loc():
        mf.destroy()
        change_l(root,bid)
    def logout():
        mf.destroy()
        login(root)
    mf=Frame(root,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=200,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="Company",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=980,height=627,relief=RIDGE)
    lf.grid(row=1,column=0)
    llf=Frame(lf,bd=10,width=225,height=627,pady=50,relief=RIDGE)
    llf.grid(row=0,column=0)
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=attendance,text="attendance",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=change_loc,text="location",font=("Times",20,'bold'))
    but2.grid(row=1,column=0,pady=56,padx=15)
    but3=Button(llf,bd=4,width=10,height=1,bg='white',command=logout,text="logout",font=("Times",20,'bold'))
    but3.grid(row=2,column=0,pady=56,padx=15)

    rlf=Frame(lf,bd=10,width=700,height=600,relief=RIDGE)
    rlf.configure(height=rlf["height"],width=rlf["width"])
    rlf.grid_propagate(0)

    mycanvas=Canvas(rlf,bd=10,width=675,height=580)
    mycanvas.pack(side=LEFT)

    yscroll=ttk.Scrollbar(rlf,orient="vertical",command=mycanvas.yview)
    yscroll.pack(side=RIGHT,fill="y")

    mycanvas.configure(yscrollcommand=yscroll.set)

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    myframe=Frame(mycanvas,bd=10,width=700,height=600)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)
    if res:
        a=0
        for i in res:
            l = Checkbutton(myframe, text=i[0], variable=i[2],command=lambda x=i[2]:select.append(x),font=("Times",20,'bold'))
            l.grid(row=a,column=0,pady=25)
            a+=1
        but=Button(myframe,bd=4,width=10,height=1,bg='white',command=atten,text="submit",font=("Times",20,'bold'))
        but.grid(row=len(res),column=0)
    mainloop()       
def change_l(root,bid):
    def change():
        try:
            change_location(mycon,loc.get(),bid)
        except Exception as e:
            messagebox.showerror("Error",e)
    def attendance():
        mf.destroy()
        mainui(root,bid)
    def change_loc():
        pass
    def logout():
        mf.destroy()
        login(root)
    mf=Frame(root,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=200,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="Company",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=980,height=627,relief=RIDGE)
    lf.grid(row=1,column=0)
    llf=Frame(lf,bd=10,width=225,height=627,pady=50,relief=RIDGE)
    llf.grid(row=0,column=0)
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=attendance,text="attendance",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=change_loc,text="location",font=("Times",20,'bold'))
    but2.grid(row=1,column=0,pady=56,padx=15)
    but3=Button(llf,bd=4,width=10,height=1,bg='white',command=logout,text="logout",font=("Times",20,'bold'))
    but3.grid(row=2,column=0,pady=56,padx=15)

    rlf=Frame(lf,bd=10,width=700,height=600,relief=RIDGE)
    rlf.configure(height=rlf["height"],width=rlf["width"])
    rlf.grid_propagate(0)

    mycanvas=Canvas(rlf,bd=10,width=675,height=580)
    mycanvas.pack(side=LEFT)

    yscroll=ttk.Scrollbar(rlf,orient="vertical",command=mycanvas.yview)
    yscroll.pack(side=RIGHT,fill="y")

    mycanvas.configure(yscrollcommand=yscroll.set)

    mycanvas.bind('<Configure>',lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

    myframe=Frame(mycanvas,bd=10,width=700,height=600)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)
    l1=Label(myframe,font=("Times",20,'bold'),text="location :",bd=7,width=8,pady=15)
    l1.grid(row=0,column=0)
    loc=StringVar()
    e1=Entry(myframe,font=("Times",20,'bold'),textvariable=loc,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e1.grid(row=0,column=1)
    but3=Button(myframe,bd=4,width=10,height=1,bg='white',command=change,text="submit",font=("Times",20,'bold'))
    but3.grid(row=1,column=0,columnspan=2)

root=start()
login(root)