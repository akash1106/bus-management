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

    rlf=LabelFrame(lf,bd=10,width=700,height=600,relief=RIDGE)

    mycanvas = Canvas(rlf)
    mycanvas.pack(side=LEFT)

    scrollbar = ttk.Scrollbar(rlf, orient="vertical", command=mycanvas.yview)
    scrollbar.pack(side="right", fill="y")

    mycanvas.configure(yscrollcommand=scrollbar.set)

    mycanvas.bind('<configure>',lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

    tef=Frame(mycanvas)     
    mycanvas.create_window((0,0),window=tef,anchor="nw")

    rlf.pack(fill="both")
    tef.grid(row=0,column=0)

    for i in range(len(a)):
        lab=Label(rlf,font=("Times",20,'bold'),text=a[i],bd=7)
        lab.grid(row=i,column=1,pady=25)
        ent=Entry(rlf,font=("Times",20,'bold'),textvariable=b[i],bd=5,width=15,bg='powder blue',relief=RIDGE)
        ent.grid(row=i,column=2)
    but1=Button(rlf,bd=4,width=10,height=1,bg='white',command=add,text="login",font=("Times",20,'bold'))
    but1.grid(row=len(a),column=1,columnspan=2)
    