from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
from dbms import *
import time
import os
from functools import partial

pa=os.environ["dbpass"]
mycon=setup("localhost","root",pa,"bus_demo")

def start():
    root=Tk()
    root.geometry("1000x750")
    root.title(" "+"bus")
    return root

def login(root):
    def log():
        try:
            res=get_user(mycon,username.get(),passw.get()) 
            if res:
                mf.destroy()
                mainui(root,res[0][0])  
            else:
                messagebox.showinfo("login","no match found")
        except Exception as e:
            messagebox.showerror("Error",e)
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
        try:
            insert_user(mycon,b[0].get(),b[1].get(),b[2].get(),int(b[3].get()),int(b[4].get()),int(b[5].get()),b[6].get(),b[7].get(),b[8].get(),b[9].get(),b[10].get(),b[11].get(),b[12].get(),int(b[13].get()))
            mf.destroy()
            login(root)
        except Exception as e:
            messagebox.showerror("Error",e)
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
        if i==10:
            drop = ttk.Combobox(
                myframe,
                state="readonly",
                values=['m','f'],
                textvariable=b[i]
            )
            drop.grid(row=i,column=1)
        else:
            ent=Entry(myframe,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
            ent.grid(row=i,column=1)
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=log,text="login",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=0)
    but2=Button(myframe,bd=4,width=10,height=1,bg='white',command=reg,text="register",font=("Times",20,'bold'))
    but2.grid(row=len(a),column=1)
    root.mainloop()
def mainui(root,uid):
    def book():
        mf.destroy()
        mainui(root,uid)
    def mybooking():
        mf.destroy()
        mybook(root,uid)
    def logout():
        mf.destroy()
        login(root)
    def sumbit(fro,to,dat):
        try:
            res=get_bus(mycon,fro.get(),to.get())
            dat=dat.get()
            mf.destroy()
            disbus(root,res,dat,uid)
        except Exception as e:
            messagebox.showerror("Error",e)

    def display_time():  
        hour = str(time.strftime("%H"))  
        minute = str(time.strftime("%M"))  
        second = str(time.strftime("%S"))  
        if int(hour) >= 12 and int(hour) < 24 and int (minute) >= 0:  
            meridiem_label.config(text = "PM")    
        else:  
            meridiem_label.config(text = "AM")   
        if int(hour) > 12:  
            hour = str((int(hour) - 12))  
        elif int(hour) == 0:  
            hour = str(12)  
        hour_label.config(text = hour)  
        minute_label.config(text = minute)  
        second_label.config(text = second)  
        hour_label.after(200, display_time)  

    mf=Frame(root,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=200,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="BUS",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=980,height=627,relief=RIDGE)
    lf.grid(row=1,column=0)
    llf=Frame(lf,bd=10,width=250,height=627,pady=50,relief=RIDGE)
    llf.grid(row=0,column=0)
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=book,text="book",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=mybooking,text="my booking",font=("Times",20,'bold'))
    but2.grid(row=1,column=0,pady=56,padx=15)
    but3=Button(llf,bd=4,width=10,height=1,bg='white',command=logout,text="logout",font=("Times",20,'bold'))
    but3.grid(row=2,column=0,pady=56,padx=15)

    myframe=Frame(lf,bd=10,width=730,height=600,relief=RIDGE)
    myframe.configure(height=myframe["height"],width=myframe["width"])
    myframe.grid_propagate(0)
    myframe.grid(row=0,column=1)

    fro=StringVar()
    to=StringVar()
    dat=StringVar()

    fromlab=Label(myframe,font=("Times",20,'bold'),text="From :",bd=7)
    fromlab.grid(row=0,column=0)
    froment=Entry(myframe,font=("Times",20,'bold'),text=fro,bd=5,width=12,bg='powder blue')
    froment.grid(row=0,column=1)


    tolab=Label(myframe,font=("Times",20,'bold'),text="To:",bd=7)
    tolab.grid(row=0,column=2)
    toent=Entry(myframe,font=("Times",20,'bold'),text=to,bd=5,width=12,bg='powder blue')
    toent.grid(row=0,column=3)

    datelab=Label(myframe,font=("Times",20,'bold'),text="Date",bd=7)
    datelab.grid(row=1,column=0)
    doben=DateEntry(myframe,font=("Times",20,'bold'),bd=5,width=10,date_pattern='yyyy-mm-dd',textvariable=dat)
    doben.grid(row=1,column=1)

    body_frame=Frame(myframe)
    body_frame.grid(row=2,column=0,columnspan=2)

    hour_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_one = Label(  
        body_frame,  
        text = ":",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    minute_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    colon_label_two = Label(  
        body_frame,  
        text = ":",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    second_label = Label(  
        body_frame,  
        text = "00",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )  
    meridiem_label = Label(  
        body_frame,  
        text = "AM",  
        font = ("radioland", "15"),  
        bg = "#2C3C3F",  
        fg = "#00D2FF"  
        )   
    hour_label.grid(row = 0, column = 0, padx = 5, pady = 5)  
    colon_label_one.grid(row = 0, column = 1, padx = 5, pady = 5)  
    minute_label.grid(row = 0, column = 2, padx = 5, pady = 5)  
    colon_label_two.grid(row = 0, column = 3, padx = 5, pady = 5)  
    second_label.grid(row = 0, column = 4, padx = 5, pady = 5)  
    meridiem_label.grid(row = 0, column = 5, padx = 5, pady = 5)  
    display_time()  

    left=Frame(myframe)
    left.grid(row=2,column=2,columnspan=3)

    cal=Calendar(left,selectmode="day",date_pattern='dd/mm/yyyy',font=("Times",20,'bold'))
    cal.grid()

    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=partial(sumbit,fro,to,dat),text="book",font=("Times",20,'bold'))
    but1.grid(row=1,column=3,columnspan=2,pady=56)

    


    root.mainloop()
def disbus(root,res,dat,uid):
    def book():
        mf.destroy()
        mainui(root,uid)
    def mybooking():
        mf.destroy()
        mybook(root,uid)
    def logout():
        mf.destroy()
        login(root)
    def conformbook(bid,dat,left,next):
        if left>0:
            try:
                insert_travel(mycon,bid,uid,dat,next+1,0)
                mf.destroy()
                mainui(root,uid)
            except Exception as e:
                messagebox.showerror("Error",e)

    
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=book,text="book",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=mybooking,text="my booking",font=("Times",20,'bold'))
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
    for i in range(len(res)):
        fra=Frame(myframe,bd=10,width=685,height=100,relief=RIDGE,padx=50,pady=25)
        fra.grid(row=i,column=0)
        l1=Label(fra,font=("Times",10,'bold'),text="From:"+res[i][2],bd=7)
        l1.grid(row=0,column=0,padx=25)
        l2=Label(fra,font=("Times",10,'bold'),text="To:"+res[i][3],bd=7)
        l2.grid(row=1,column=0,padx=25)
        l3=Label(fra,font=("Times",10,'bold'),text="Arrival:"+str(res[i][6]),bd=7)
        l3.grid(row=0,column=1,padx=25)
        l4=Label(fra,font=("Times",10,'bold'),text="Departure:"+str(res[i][7]),bd=7)
        l4.grid(row=1,column=1,padx=25)
        if res[i][4]==1:
            typ="sleeper"
        elif res[i][4]==2:
            typ="seater"
        else:
            typ="hybrid"
        l5=Label(fra,font=("Times",10,'bold'),text="type:"+typ,bd=7)
        l5.grid(row=0,column=2,padx=25)
        l6=Label(fra,font=("Times",10,'bold'),text="rating:"+str(res[i][5]),bd=7)
        l6.grid(row=1,column=2,padx=25)
        if res[i][8]==1:
            ac="AC"
        else:
            ac="NON-AC"
        l7=Label(fra,font=("Times",10,'bold'),text=ac,bd=7)
        l7.grid(row=0,column=3,padx=25)
        l8=Label(fra,font=("Times",10,'bold'),text="price : "+str(res[i][12]),bd=7)
        l8.grid(row=1,column=3,padx=25)

        da1=get_seatno(mycon,res[i][0],dat)
        if not da1:
            da1.append([0])
        l8=Label(fra,font=("Times",10,'bold'),text="seat left : "+str(res[i][9]+res[i][10]-da1[0][0]),bd=7)
        l8.grid(row=3,column=1,padx=25)

        but=(Button(fra,bd=4,bg='white',command=partial(conformbook,res[i][0],dat,res[i][9]+res[i][10]-da1[0][0],da1[0][0]),text="book",font=("Times",8,'bold')))
        but.grid(row=3,column=1,columnspan=2,padx=50)
def mybook(root,uid):
    def book():
        mf.destroy()
        mainui(root,uid)
    def mybooking():
        pass
    def logout():
        mf.destroy()
        login(root)
    def review(tid,bid,uid):
        mf.destroy()
        reviewpage(root,uid,bid)

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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=book,text="book",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=mybooking,text="my booking",font=("Times",20,'bold'))
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
    res=get_booked_bus(mycon,uid)

    for i in range(len(res)):
        fra=Frame(myframe,bd=10,width=685,height=100,relief=RIDGE,padx=35)
        fra.grid(row=i+1,column=0,)
        l1=Label(fra,font=("Times",10,'bold'),text="start: "+res[i][0],bd=7)
        l1.grid(row=0,column=0,padx=25)
        l2=Label(fra,font=("Times",10,'bold'),text="end: "+res[i][1],bd=7)
        l2.grid(row=1,column=0,padx=25)
        l3=Label(fra,font=("Times",10,'bold'),text="arrive time: "+str(res[i][2]),bd=7)
        l3.grid(row=0,column=1,padx=25)
        l4=Label(fra,font=("Times",10,'bold'),text="destination time: "+str(res[i][3]),bd=7)
        l4.grid(row=1,column=1,padx=25)
        l5=Label(fra,font=("Times",10,'bold'),text="location: "+str(res[i][4]),bd=7)
        l5.grid(row=0,column=2,padx=25)
        l6=Label(fra,font=("Times",10,'bold'),text="date: "+str(res[i][6]),bd=7)
        l6.grid(row=1,column=2,padx=25)
        l7=Label(fra,font=("Times",10,'bold'),text="seatno: "+str(res[i][7]),bd=7)
        l7.grid(row=0,column=3,padx=25)
        if res[i][8]==1:
            but=Button(fra,bd=4,width=1,height=1,bg='white',command=partial(review,res[i][9],res[i][5],uid),text="+",font=("Times",8,'bold'))
            but.grid(row=1,column=3)
def reviewpage(root,uid,bid):
    def add():
        try:
            if ra.get().isdecimal():
                val=float(ra.get())
                if val>0 and val<5:
                    insert_busrandr(mycon,bid,uid,re.get(),float(ra.get()))
                    update_Rating_bus(mycon,float(ra.get()),bid)
                    res=get_cid(mycon,bid)
                    update_Rating_com(mycon,float(ra.get()),res[0][0])
                    mf.destroy()
                    mainui(root,uid)
                else:
                    messagebox.showwarning("Error","rating must be in range of 0-5")
            else:
                messagebox.showwarning("Error","plz enter data correct")
        except Exception as e:
            messagebox.showerror("Error",e)
    mf=Frame(root,padx=240,pady=150,bd=10,width=995,height=745,relief=RIDGE,bg="cadetblue")     
    mf.grid()
    tf=Frame(mf,bd=10,width=300,height=100,relief=RIDGE,bg="dark gray")
    tf.grid(row=0,column=0)
    lbt=Label(tf,font=("Times",30,'bold'),text="REVIEW",bd=7)
    lbt.grid(row=0,column=0)
    lf=Frame(mf,bd=10,width=500,height=500,relief=RIDGE,padx=43,pady=50)
    lf.grid(row=1,column=0)
    l1=Label(lf,font=("Times",20,'bold'),text="rating :",bd=7,width=8,pady=15)
    l1.grid(row=0,column=0)
    ra=StringVar()
    e1=Entry(lf,font=("Times",20,'bold'),textvariable=ra,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e1.grid(row=0,column=1)
    l2=Label(lf,font=("Times",20,'bold'),text="review :",bd=7,width=8,pady=25)
    l2.grid(row=1,column=0)
    re=StringVar()
    e2=Entry(lf,font=("Times",20,'bold'),textvariable=re,bd=5,width=15,bg='powder blue',relief=RIDGE)
    e2.grid(row=1,column=1)
    but1=Button(lf,bd=4,width=10,height=1,bg='white',command=add,text="sumbit",font=("Times",20,'bold'))
    but1.grid(row=2,column=0)


root=start()
login(root)