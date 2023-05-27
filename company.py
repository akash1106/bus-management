from tkinter import *
from tkinter import messagebox
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
        try:
            res=check_company(mycon,username.get(),passw.get())
            if res:
                mf.destroy()
                mainui(root,res[0][0])
            else:
                messagebox.showinfo("login","no data match")
        except  Exception as e:
            messagebox.showerror("Error", e)
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
    a=["Company Name","User Name","Password","Phno","Address","City","District","State","Terms"]
    b=[StringVar() for i in a]
    def log():
        mf.destroy()
        login(root)
    def reg():
        try:
            if b[3].get().isdigit(): 
                lis=[b[0].get(),b[1].get(),b[2].get(),int(b[3].get()),(b[4].get()),b[5].get(),b[6].get(),b[7].get(),tearea.get("1.0","end-1c")]
                if (lis[0] and lis[1] and lis[2] and lis[3] and len(lis[4]==10) and lis[5] and lis[6] and lis[7] and lis[8]):
                    insert_company(mycon,lis[0], lis[1] , lis[2] , lis[3] , len(lis[4]==10) , lis[5] , lis[6] , lis[7] , lis[8])
                else:
                    messagebox.showwarning("warning","plz enter the data correct")
            else:
                messagebox.showwarning("warning","plz enter the data correct")
        except Exception as e:
            messagebox.showerror("Error",e)
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
def mainui(root,cid):
    def bus():
        pass
    def staff():
        mf.destroy()
        main_staff(root,cid)
    def logout():
        mf.destroy()
        login(root)
    def add_bus():
        mf.destroy()
        add_bus_for_company(root,cid)
    def update_bus(bid):
        mf.destroy()
        update_bus_C(root,cid,bid)
    try:
        res=get_bus_company(mycon,cid)
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    mrf=Frame(myframe,bd=10,width=700,height=100)
    mrf.grid(row=0,column=0)
    but4=Button(mrf,bd=4,width=1,height=1,bg='white',command=add_bus,text="+",font=("Times",8,'bold'))
    but4.grid(row=0,column=0)
    for i in range(len(res)):
        fra=Frame(myframe,bd=10,width=685,height=100,relief=RIDGE,padx=35)
        fra.grid(row=i+1,column=0,)
        l1=Label(fra,font=("Times",10,'bold'),text="start: "+str(res[i][1]),bd=7)
        l1.grid(row=0,column=0,padx=35)
        l2=Label(fra,font=("Times",10,'bold'),text="end: "+str(res[i][2]),bd=7)
        l2.grid(row=1,column=0,padx=35)
        l3=Label(fra,font=("Times",10,'bold'),text="arrival: "+str(res[i][5]),bd=7)
        l3.grid(row=0,column=1,padx=50)
        l4=Label(fra,font=("Times",10,'bold'),text="Departure: "+str(res[i][6]),bd=7)
        l4.grid(row=1,column=1,padx=35)
        if res[i][4]==1:
            typ="sleeper"
        elif res[i][4]==2:
            typ="seater"
        else:
            typ="hybrid"
        l5=Label(fra,font=("Times",10,'bold'),text="type: "+typ,bd=7)
        l5.grid(row=0,column=2,padx=35)
        l6=Label(fra,font=("Times",10,'bold'),text="bid: "+str(res[i][0]),bd=7)
        l6.grid(row=1,column=2,padx=35)
        l7=Label(fra,font=("Times",10,'bold'),text="price: "+str(res[i][9]),bd=7)
        l7.grid(row=0,column=3,padx=35)
        b=(res[i][0])
        but=(Button(fra,bd=4,width=1,height=1,bg='white',command=partial(update_bus,b),text="u",font=("Times",8,'bold')))
        but.grid(row=1,column=3,padx=35)
    root.mainloop()
def add_bus_for_company(root,cid):
    a=["start","end","bus type","Arrival time","Departure time","ac_nonac","price"]
    b=[StringVar() for i in a]
    def bus():
        mf.destroy()
        mainui(root,cid)
    def staff():
        mf.destroy()
        main_staff(root,cid)
    def logout():
        mf.destroy()
        login(root)
    def add():
        try:
            if drop1.get().isdigit() and drop.get().isdigit() and b[6].get().isdigit() and b[0].get() and b[1].get():
                ty=int(b[2].get())
                if ty==1:
                    r1,r2=13,15
                elif ty==2:
                    r1=r2=6
                else:
                    r1,r2=13,6
                a=hour_string1.get()+":"+min_string1.get()+":00"
                d=hour_string2.get()+":"+min_string2.get()+":00"
                insert_bus(mycon,cid,b[0].get(),b[1].get(),int(drop1.get()),a,d,int(drop.get()),r1,r2,b[0].get(),int(b[6].get()))
            else:
                messagebox.showwarning("warning","plz enter the data correct")
        except Exception as e:
            messagebox.showerror("Error",e)
        mf.destroy()
        mainui(root,cid)
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    myframe=Frame(mycanvas,bd=10,width=700,height=600,padx=100)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)
    hour_string1=StringVar()
    min_string1=StringVar()
    min_sb = Spinbox(
    myframe,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string1,
        width=2,
        state="readonly",
        font=("Times",20,'bold')
    )
    sec_hour = Spinbox(
        myframe,
        from_=0,
        to=59,
        wrap=True,
        textvariable=min_string1,
        font=("Times",20,'bold'),
        width=2,
    )
    hour_string2=StringVar()
    min_string2=StringVar()
    d_min_sb = Spinbox(
    myframe,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string2,
        width=2,
        state="readonly",
        font=("Times",20,'bold')
    )
    d_sec_hour = Spinbox(
        myframe,
        from_=0,
        to=59,
        wrap=True,
        textvariable=min_string2,
        font=("Times",20,'bold'),
        width=2,
        )

    
    for i in range(len(a)):
        lab=Label(myframe,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=1,pady=25)
        if i==2:
            drop1 = ttk.Combobox(
                myframe,
                state="readonly",
                values=["1", "2", "3"]
            )
            drop1.grid(row=i,column=2)
        elif i==3:
            min_sb.grid(row=i,column=2)
            sec_hour.grid(row=i,column=3)
        elif i==4:
            d_min_sb.grid(row=i,column=2)
            d_sec_hour.grid(row=i,column=3)
        elif i==5:
            drop = ttk.Combobox(
                myframe,
                state="readonly",
                values=["0", "1"]
            )
            drop.grid(row=i,column=2)
        else:
            ent=Entry(myframe,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
            ent.grid(row=i,column=2)
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=add,text="add",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=1,columnspan=2)
    root.mainloop()
def main_staff(root,cid):
    try:
        res=get_staff(mycon,cid)
    except Exception as e:
        messagebox.showerror("Error",e)
    def bus():
        mf.destroy()
        mainui(root,cid)
    def staff():
        pass
    def logout():
        mf.destroy()
        login(root)
    def update_staff(sid):
        mf.destroy()
        update_staff_in_app(root,sid,cid)
    def add_staff():
        mf.destroy()
        add_staff_company(root,cid)


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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    mrf=Frame(myframe,bd=10,width=700,height=100)
    mrf.grid(row=0,column=0)
    but4=Button(mrf,bd=4,width=1,height=1,bg='white',command=add_staff,text="+",font=("Times",8,'bold'))
    but4.pack(side=RIGHT)

    for i in range(len(res)):
        fra=Frame(myframe,bd=10,width=685,height=100,relief=RIDGE,padx=35)
        fra.grid(row=i+1,column=0,)
        l1=Label(fra,font=("Times",10,'bold'),text="first name: "+res[i][0],bd=7)
        l1.grid(row=0,column=0,padx=35)
        l2=Label(fra,font=("Times",10,'bold'),text="last name: "+res[i][1],bd=7)
        l2.grid(row=1,column=0,padx=35)
        l3=Label(fra,font=("Times",10,'bold'),text="phone no: "+str(res[i][2]),bd=7)
        l3.grid(row=0,column=1,padx=35)
        l4=Label(fra,font=("Times",10,'bold'),text="job: "+res[i][3],bd=7)
        l4.grid(row=1,column=1,padx=35)
        l5=Label(fra,font=("Times",10,'bold'),text="bid: "+str(res[i][4]),bd=7)
        l5.grid(row=0,column=2,padx=35)
        b=(res[i][5])
        but=(Button(fra,bd=4,width=1,height=1,bg='white',command=partial(update_staff,b),text="-",font=("Times",8,'bold')))
        but.grid(row=0,column=3,padx=50)
def add_staff_company(root,cid):
    a=["first name","last name","User name","password","phno","doorno","address","city","district","state","sex","job","bid","dob","aadhaar"]
    b=[StringVar() for i in a]
    def bus():
        mf.destroy()
        mainui(root,cid)
    def staff():
        mf.destroy()
        main_staff(root,cid)
    def logout():
        mf.destroy()
        login(root)
    def add():
        try:
            if b[0].get() and b[1].get() and b[2].get() and b[3].get()and b[4].get().isdigit() and b[5].get().isdigit() and b[6].get() and b[7].get() and b[8].get() and b[9].get() and b[10].get() and b[11].get() and b[12].get().isdigit() and b[13].get() and b[14].get().isdigit():
                insert_staff(mycon,b[0].get(),b[1].get(),b[2].get(),b[3].get(),int(b[4].get()),int(b[5].get()),b[6].get(),b[7].get(),b[8].get(),b[9].get(),b[10].get(),b[11].get(),int(b[12].get()),b[13].get(),int(b[14].get()),cid)
            else:
                messagebox.showwarning("warning","plz enter the data correct")
        except Exception as e:
            messagebox.showerror("Error",e)
        mf.destroy()
        main_staff(root,cid)
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    myframe=Frame(mycanvas,bd=10,width=700,height=600,padx=100)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)
    res1=get_all_bid(mycon,cid)
    print(res1)
    for i in range(len(a)):
        lab=Label(myframe,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=1,pady=15)
        if i==10:
            drop=ttk.Combobox(
                myframe,
                state="readonly",
                values=["m", "f"],
                textvariable=b[i]
            )
            drop.grid(row=i,column=2)
        elif i==11:
            drop=ttk.Combobox(
                myframe,
                state="readonly",
                values=["d", "c"],
                textvariable=b[i]
            )
            drop.grid(row=i,column=2)
        elif i==12:
            drop=ttk.Combobox(
                myframe,
                state="readonly",
                values=[str(i[0]) for i in res1],
                textvariable=b[i]
            ).grid(row=i,column=2)
        else:
            ent=Entry(myframe,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
            ent.grid(row=i,column=2)
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=add,text="add",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=1,columnspan=2)
    root.mainloop()
def update_bus_C(root,cid,bid):
    a=["start","end","Arrival time","Departure time","price"]
    b=[StringVar() for i in a]
    try:
        res=get_bus_company1(mycon,cid,bid)
    except Exception as e:
        messagebox.showerror("Error",e)
    for i in range(len(b)):
        b[i].set(str(res[0][i]))
    def bus():
        mf.destroy()
        mainui(root,cid)
    def staff():
        mf.destroy()
        main_staff(root,cid)
    def logout():
        mf.destroy()
        login(root)
    def update():
        try:
            a=hour_string1.get()+":"+min_string1.get()+":00"
            d=hour_string2.get()+":"+min_string2.get()+":00"
            update_bus_details(mycon,b[0].get(),b[1].get(),a,d,bid,int(b[4].get()))
        except Exception as e:
            messagebox.showerror("Error",e)
        mf.destroy()
        mainui(root,cid)
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    myframe=Frame(mycanvas,bd=10,width=700,height=600,padx=100)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)

    hour_string1=StringVar()
    min_string1=StringVar()
    min_sb = Spinbox(
    myframe,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string1,
        width=2,
        state="readonly",
        font=("Times",20,'bold')
    )
    sec_hour = Spinbox(
        myframe,
        from_=0,
        to=59,
        wrap=True,
        textvariable=min_string1,
        font=("Times",20,'bold'),
        width=2,
    )
    hour_string2=StringVar()
    min_string2=StringVar()
    d_min_sb = Spinbox(
    myframe,
        from_=0,
        to=23,
        wrap=True,
        textvariable=hour_string2,
        width=2,
        state="readonly",
        font=("Times",20,'bold')
    )
    d_sec_hour = Spinbox(
        myframe,
        from_=0,
        to=59,
        wrap=True,
        textvariable=min_string2,
        font=("Times",20,'bold'),
        width=2,
        )

    
    for i in range(len(a)):
        lab=Label(myframe,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=1,pady=25)
        if i==2:
            min_sb.grid(row=i,column=2)
            sec_hour.grid(row=i,column=3)
        elif i==3:
            d_min_sb.grid(row=i,column=2)
            d_sec_hour.grid(row=i,column=3)
        else:
            ent=Entry(myframe,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
            ent.grid(row=i,column=2)
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=update,text="update",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=1,columnspan=2)
    root.mainloop()
def update_staff_in_app(root,sid,cid):
    a=["bus"]
    b=[StringVar() for i in a]
    try:
        res=get_staff_bus(mycon,sid)
        res1=get_all_bid(mycon,cid)
        b[0].set(res[0][0])
    except Exception as e:
        messagebox.showerror("Error",e)
    
    # for i in range(len(b)):
    #     b[i].set(str(res[0][i]))
    def bus():
        mf.destroy()
        mainui(root,cid)
    def staff():
        mf.destroy()
        main_staff(root,cid)
    def logout():
        mf.destroy()
        login(root)
    def update():
        update_Staff_details(mycon,int(b[0].get()),sid)
        mf.destroy()
        main_staff(root,cid)
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
    but1=Button(llf,bd=4,width=10,height=1,bg='white',command=bus,text="bus",font=("Times",20,'bold'))
    but1.grid(row=0,column=0,pady=56,padx=15)
    but2=Button(llf,bd=4,width=10,height=1,bg='white',command=staff,text="staff",font=("Times",20,'bold'))
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

    myframe=Frame(mycanvas,bd=10,width=700,height=600,padx=100)
    mycanvas.create_window((0,0),window=myframe,anchor="nw")
    rlf.grid(row=0,column=1)
    

    for i in range(len(a)):
        lab=Label(myframe,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=1,pady=25)
        drop = ttk.Combobox(
                myframe,
                state="readonly",
                values=[i[0] for i in res1],
                textvariable=b[i]
        )
        drop.grid(row=i,column=2)
        
    but1=Button(myframe,bd=4,width=10,height=1,bg='white',command=update,text="update",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=1,columnspan=2)
    root.mainloop()
root=start()
login(root)
