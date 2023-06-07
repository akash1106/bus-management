import mysql.connector as sql
def setup(host,user,passwd,data):
    mycon=sql.connect(host=host,user=user,passwd=passwd,database=data)
    if not mycon.is_connected():
        print("error while connecting!!")
    else:
        return mycon

def insert_company(mycon,Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms):
    st='''insert into company_details(name,cname,pass,phno,address,city,district,state,noofbus,rating,tandc) values(%s,%s,AES_ENCRYPT(%s,key),%s,%s,%s,%s,%s,0,0,%s)'''
    t=(Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def insert_user(mycon,uname,pas,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar):
    st='''insert into user_details(uname,pass,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar,coin) values('%s,AES_ENCRYPT(%s,'key'),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0);'''
    t=(uname,pas,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def insert_bus(mycon,cid,start,end,btype,atime,dtime,ac_nonac,row1,row2,location,price):
    st='''insert into bus_details(cid,start,end,btype,rating,atime,dtime,ac_nonac,row1,row2,location,price) values(%s,%s,%s,%s,0.0,%s,%s,%s,%s,%s,%s,%s)'''
    t=(cid,start,end,btype,atime,dtime,ac_nonac,row1,row2,location,price)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def insert_staff(mycon,fname,lname,sname,pas,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid):
    st='''insert into staff_details(fname,lname,sname,pass,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid) values(%s,%s,%s,AES_ENCRYPT(%s,"key"),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    t=(fname,lname,sname,pas,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def insert_travel(mycon,bid,uid,dat,seatno,active):
    st='''insert into travel_details(bid,uid,dat,seatno,active) values(%s,%s,%s,%s,%s)'''
    t=(bid,uid,dat,seatno,active)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def insert_busrandr(mycon,bid,uid,review,rating):
    st='''insert into busrandr(bid,uid,review,rating) values(%s,%s,%s,%s)'''
    t=(bid,uid,review,rating)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def check_company(mycon,cname,pas):
    st='''select cid from company_details where cname=%s and pass=AES_ENCRYPT(%s,"key");'''
    t=(cname,pas)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_bus_company(mycon,cid):
    st='''select bid,start,end,btype,bus_details.rating,atime,dtime,ac_nonac,location,price from bus_details where cid=%s;'''
    t=(cid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def update_bus_details(mycon,start,end,atime,dtime,bid,price):
    st='''update bus_details set start= %s , end=%s , atime=%s , dtime=%s,price=%s where bid=%s;'''
    t=(start,end,atime,dtime,price,bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def update_Staff_details(mycon,bid,sid):
    st='''update staff_details set bid=%s where sid=%s;'''
    t=(bid,sid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def check_staff(mycon,sname,pas):
    st='''select sid,bid from staff_details where sname=%s and pass=AES_ENCRYPT(%s,'key');'''
    t=(sname,pas)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_person_on_bus(mycon,bid):
    st='''select fname,uid,tid from travel_details natural join user_Details where bid=%s and dat=curdate();'''
    t=(bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def set_active(mycon,active,tid):
    st='''update  travel_details set active=%s where tid=%s;'''
    t=(active,tid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def get_bus(mycon,start,end):
    st='''select bid,cid,start,end,btype,rating,atime,dtime,ac_nonac,row1,row2,location,price from bus_Details where start=%s and end=%s;'''
    t=(start,end)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_booked(mycon,bid):
    st='''select seatno from travel_details where bid=%s;'''
    t=(bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def change_location(mycon,location,bid):
    st='''update bus_Details set location=%s where bid=%s;'''
    t=(location,bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def update_Rating_bus(mycon,rating,bid):
    st='''update bus_details set rating=(rating+{0})/2 where bid={1};'''.format(rating,bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()

def update_Rating_com(mycon,rating,cid):
    st='''update company_details set rating=(rating+%s)/2 where cid=%s;'''
    t=(rating,cid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    mycon.commit()

def get_bus_company1(mycon,cid,bid):
    st='''select start,end,atime,dtime,price from bus_details where cid=%s and bid=%s;'''
    t=(cid,bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_staff(mycon,cid):
    st='''select fname,lname,phno,job,bid,sid from staff_details where cid=%s;'''
    t=(cid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_staff_bus(mycon,sid):
    st='''select bid from staff_details where sid=%s;'''
    t=(sid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_user(mycon,uname,pas):
    st='''select uid from user_details where uname=%s and pass=AES_ENCRYPT(%s,"key");'''
    t=(uname,pas)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_seatno(mycon,bid,dat):
    st="select seatno from travel_details where bid=%s and dat=%s order by seatno desc;"
    t=(bid,dat)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_booked_bus(mycon,uid):
    st='''select start,end,atime,dtime,location,bid,dat,seatno,active,tid from travel_details natural join bus_Details where uid=%s'''
    t=(uid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_cid(mycon,bid):
    st='''select cid from bus_details where bid=%s'''
    t=(bid)
    cursor=mycon.cursor()
    cursor.execute(st,t)
    data=cursor.fetchall()
    return data

def get_all_bid(mycon,cid):
    st='''select distinct bid from bus_Details where cid=%s;'''
    t=(cid)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data

def get_s(mycon):
    st='''select distinct start from bus_Details'''
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data

def get_e(mycon):
    st='''select distinct end from bus_Details'''
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
