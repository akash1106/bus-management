import mysql.connector as sql
def setup(host,user,passwd,data):
    mycon=sql.connect(host=host,user=user,passwd=passwd,database=data)
    if not mycon.is_connected():
        print("error while connecting!!")
    else:
        return mycon

def insert_company(mycon,Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms):
    st='''insert into company_details(name,cname,pass,phno,address,city,district,state,noofbus,rating,tandc) values('{0}','{1}',AES_ENCRYPT('{2}','key'),{3},'{4}','{5}','{6}','{7}',0,0,'{8}')'''.format(Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()

def insert_user(mycon,uname,pas,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar):
    st='''insert into user_details(uname,pass,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar,coin) values('{0}'',AES_ENCRYPT('{1}','key'),'{2}',{3},{4},{5},"{6}","{7}","{8}","{9}","{10}","{11}","{12}",{13},0);'''.format(uname,pas,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def insert_bus(mycon,cid,start,end,btype,atime,dtime,ac_nonac,row1,row2,location):
    st='''insert into bus_details(cid,start,end,btype,rating,atime,dtime,ac_nonac,row1,row2,location) values({0},"{1}","{2}",{3},0.0,'{4}','{5}',{6},{7},{8},"{9}")'''.format(cid,start,end,btype,atime,dtime,ac_nonac,row1,row2,location)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def insert_staff(mycon,fname,lname,sname,pas,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid):
    st='''insert into staff_details(fname,lname,sname,pass,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid) values("{0}","{1}","{2}",AES_ENCRYPT("{3}","key"),{4},{5},"{6}","{7}","{8}","{9}","{10}","{11}",{12},"{13}",{14},{15});'''.format(fname,lname,sname,pas,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def insert_travel(mycon,bid,uid,dat,seatno,active):
    st='''insert into travel_details(bid,uid,dat,seatno,active) values({0},{1},"{2}","{3}",{4})'''.format(bid,uid,dat,seatno,active)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def insert_busrandr(mycon,bid,uid,review,rating):
    st='''insert into busrandr(bid,uid,review,rating) values({0},{1},"{2}",{3})'''.format(bid,uid,review,rating)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def check_company(mycon,cname,pas):
    st='''select cid from company_details where cname="{0}" and pass=AES_ENCRYPT("{1}","key");'''.format(cname,pas)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def get_bus(mycon,cid):
    st='''select bid,start,end,btype,bus_details.rating,atime,dtime,ac_nonac,location from bus_details where cid={0};'''.format(cid)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def update_bus_details(mycon,start,end,atime,dtime,bid):
    st='''update bus_details set start= "{0}" , end="{1}" , atime="{2}" , dtime="{3}" where bid={4};'''.format(start,end,atime,dtime,bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def update_Staff_details(mycon,bid,sid):
    st='''update staff_details set bid={0} where sid={1};'''.format(bid,sid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def delete_staff(mycon,sid):
    st='''delete from staff_details where sid={0};'''.format(sid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def check_staff(mycon,sname,pas):
    st='''select sid,bid from staff_details where sname="{0}" and pass=AES_ENCRYPT('{1}','key');'''.format(sname,pas)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def get_person_on_bus(mycon,bid):
    st='''select fname,uid,tid from travel_details natural join user_Details where bid={0};'''.format(bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def set_active(mycon,active,tid):
    st='''update  travel_details set active={0} where tid={1};'''.format(active,tid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def get_bus(mycon,start,end):
    st='''select bid,cid,btype,rating,atime,dtime,ac_nonac,row1,row2,location from bus_Details where start="{0}" and end="{1}";'''.format(start,end)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def get_booked(mycon,bid):
    st='''select seatno from travel_details where bid={0};'''.format(bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def get_location(mycon,bid):
    st='''select location from travel_details natural join bus_details where bid={0};'''.format(bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    data=cursor.fetchall()
    return data
def change_location(mycon,location,bid):
    st='''update bus_Details set location="{0}" where bid={1};'''.format(location,bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def update_Rating_bus(mycon,rating,bid):
    st='''update bus_details set rating={0} where bid={1};'''.format(rating,bid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def update_Rating_com(mycon,rating,cid):
    st='''update company_details set rating={0} where cid={1};'''.format(rating,cid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()
def set_coin(mycon,coin,uid):
    st='''update user_details set coin={0} where uid={1};'''.format(coin,uid)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()