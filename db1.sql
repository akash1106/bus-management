create database bus_demo;
use bus_demo;
create table user_details(
uid int auto_increment primary key,
uname varchar(25) not null,
pass blob not null,
fname varchar(25) not null,
phno bigint not null,
emphno bigint not null,
doorno int not null,
address varchar(25) not null,
city varchar(25) not null,
district varchar(25) not null,
state varchar(25) not null,
sex char(1) not null,
mailid varchar(25) not null,
dob date not null,
aadhaar bigint not null,
coin int not null);


create table company_details(
cid int auto_increment primary key,
name varchar(25) not null,
cname varchar(25) not null,
pass blob not null,
phno bigint not null unique,
address varchar(25) not null,
city varchar(25) not null,
district varchar(25) not null,
state varchar(25) not null,
noofbus int not null,
rating float not null,
tandc varchar(250) not null);


create table bus_details(
bid int auto_increment primary key,
cid int,
start varchar(25) not null,
end varchar(25) not null,
btype int not null,
rating float not null,
atime time not null,
dtime time not null,
ac_nonac int not null,
row1 int not null,
row2 int not null,
location varchar(25) not null,
foreign key(cid) references company_details(cid));

create table staff_details(
sid int auto_increment primary key,
fname varchar(25) not null,
lname varchar(25) not null,
sname varchar(25) not null,
pass blob not null,
phno bigint not null,
doorno int not null,
address varchar(25) not null,
city varchar(25) not null,
district varchar(25) not null,
state varchar(25) not null,
sex char(1) not null,
job varchar(25) not null,
bid int,
dob date not null,
aadhaar bigint not null unique,
cid int not null,
foreign key (bid) references bus_details(bid),
foreign key (cid) references company_details(cid));

create table traver_details(
tid int auto_increment primary key,
bid int,
uid int,
dat date,
seatno varchar(10) not null,
active  int not null,
foreign key (bid) references bus_details(bid),
foreign key (uid) references user_details(uid));

create table busrandr(
bid int,
uid int,
review varchar(50),
rating float not null,
foreign key (bid) references bus_details(bid),
foreign key (uid) references user_details(uid));

insert into user_details(uname,pass,fname,phno,emphno,doorno,address,city,district,state,sex,mailid,dob,aadhaar,coin)
values("akash",AES_ENCRYPT("pass1","key"),"akash",9876543210,1234567890,31,"renga nagar","ukt","trichy","tamilnadu","m","akashavt001@gmail.com","2003-06-11",9876543210,0),
("sruthi",AES_ENCRYPT("pass1","key"),"sruthi",8462795130,9638527410,19,"ram nagar","ooty","chennai","tamilnadu","f","ram1@gmail.com","2003-01-05",7894561230,0),
("abi",AES_ENCRYPT("pass1","key"),"abi",3216549870,1478523690,12,"sri nagar","sri","coimbatore","tamilnadu","f","abi123@gmail.com","2004-05-12",3698527410,0),
("ranjith",AES_ENCRYPT("pass1","key"),"ranjith",1598746320,9512368740,58,"ram nagar","tech park","trichy","tamilnadu","m","ranjith@gmail.com","2003-05-03",7539861420,0),
("pranesh",AES_ENCRYPT("pass1","key"),"pranesh",167943820,943671820,85,"fire nagar","RS Puram","Coimbatore","tamilnadu","m","pranesh001@gmail.com","2003-08-11",7536492810,0);
select * from user_Details;
insert into company_details(name,cname,pass,phno,address,city,district,state,noofbus,rating,tandc)
values("akash","akash",AES_ENCRYPT("pass2","key"),9876543210,"king road","Nesapakkam","Chennai","tamilnadu",5,3.5,"allcome"),
("ram","ram",AES_ENCRYPT("pass2","key"),4683219705,"sri road","tech park","Chennai","tamilnadu",3,4.8,"allcome"),
("red_bus","red_bus",AES_ENCRYPT("pass2","key"),4568219730,"ranga nagar","manthope colony","Chennai","tamilnadu",1,4.6,"allcome"),
("Alka_Talwar","Alka_Talwar",AES_ENCRYPT("pass2","key"),4568239710,"Cruz Puram","Thoothukudi","Thoothukudi","tamilnadu",3,4.2,"allcome"),
("Chandni_Sankaran","Chandni_Sankaran",AES_ENCRYPT("pass2","key"),7139468250,"V.V.Nagar","Tisaiyanvilai","Tirunelveli","tamilnadu",6,4.7,"allcome");
select * from company_details;
insert into bus_details(cid,start,end,btype,rating,atime,dtime,ac_nonac,row1,row2,location)
values(1,"trichy","chennai",1,4.8,'08:00:00','12:00:00',1,6,6,"trichy"),
(2,"Coimbatore","chennai",2,3.9,'14:00:00','23:00:00',1,13,15,"chennai"),
(3,"Kelambakkam","Coimbatore",3,4.3,'01:00:00','13:00:00',1,13,6,"coimbatore"),
(4,"Vellore","Kelambakkam",2,3.9,'06:00:00','13:00:00',0,13,15,"Vellore"),
(5,"Vellore","trichy",2,4.9,'02:00:00','13:00:00',0,13,15,"trichy");
select * from bus_Details;
insert into staff_details(fname,lname,sname,pass,phno,doorno,address,city,district,state,sex,job,bid,dob,aadhaar,cid)
values("Nishi","Dhingra","Nishi",AES_ENCRYPT("pass3","key"),7896321450,23,"Poonamalle High Rd","Aminjikarai","chennai","tamilnadu","f","d",1,"1998-06-12",9873214650,1),
("David","Sai Pai","David",AES_ENCRYPT("pass3","key"),5678129340,18,"Valluvar Kottam High Rd","Nungambakkam","chennai","tamilnadu","m","c",2,"1965-11-12",7539846210,2),
("Deep ","Chandra Bala","Deep",AES_ENCRYPT("pass3","key"),7845129630,689,"Chennai Tiruvallur","Konnur","chennai","tamilnadu","m","d",3,"1978-08-25",9845237610,3),
("Sameedha","Khalsa","Sameedha",AES_ENCRYPT("pass3","key"),8264791350,45,"Tharamani Rd","Kollam","Thanjavur","tamilnadu","f","c",4,"1996-05-01",8739654120,4),
("Jayshree","Dutt","Jayshree",AES_ENCRYPT("pass3","key"),6789321450,86,"Rampart Rd","Thanjavur","Thanjavur","tamilnadu","f","d",5,"1987-12-11",7689543102,5);
select * from staff_Details;
insert into traver_details(bid,uid,dat,seatno,active)
values(1,1,"2023-09-07","a1",0),
(2,2,"2023-09-07","b3",0),
(3,3,"2023-09-08","c5",1),
(4,4,"2023-09-08","d7",1),
(5,5,"2023-09-11","a6",0);
select * from traver_Details;
insert into busrandr(bid,uid,review,rating)
values(1,2,"good",4.5),
(2,3,"poor",3.0),
(3,4,"good",5.0),
(4,5,"poor",2.5),
(5,5,"super",5.0);
select * from busrandr;

-- command 1 
select cid from company_details where cname="akash" and pass=AES_ENCRYPT("pass2","key");

-- command 2
select bid,start,end,btype,bus_details.rating,atime,dtime,ac_nonac,location from bus_details where cid=1;

-- command 3
update bus_details set start= "trichy" , end="chennai" , atime="08:00:00" , dtime="12:00:00" where bid=1;

-- command 4 
update staff_details set bid=null where sid=1;
update staff_details set bid=1 where sid=1;

-- command 5
delete from staff_details where sid=1;

-- command 6
select sid,bid from staff_details where sname="David" and pass=AES_ENCRYPT('pass3','key');

-- command 7
select fname,uid,tid from traver_details natural join user_Details where bid=1;

-- command 8
update  traver_details set active=1 where tid=6;

-- command 9
select bid,cid,btype,rating,atime,dtime,ac_nonac,row1,row2,location from bus_Details where start="trichy" and end="chennai";

-- command 10
select seatno from traver_details where bid=1;

-- command 11
select location from traver_Details natural join bus_details where uid=1;  

-- command 12
update bus_Details set location="trichy" where bid=1;

-- command 13
update bus_details set rating=4.0 where bid=1;

-- command 13
update company_details set rating=4.0 where cid=1;

-- command 14
update user_details set coin=100 where uid=1;
  