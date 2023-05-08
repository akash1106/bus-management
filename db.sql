create database bus;
use bus;
create table user_details(
uid int auto_increment primary key,
uname varchar(25) not null,
pass varchar(25) not null,
fname varchar(25) not null,
phno bigint not null,
emphno bigint not null,
doorno int not null,
state varchar(25) not null,
sex char(1) not null,
mailid varchar(25) not null,
dob date not null,
aadhaar bigint not null);

create table company_details(
cid int auto_increment primary key,
name varchar(25) not null,
cname varchar(25) not null,
pass varchar(25) not null,
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
pass varchar(25) not null,
phno bigint not null,
doorno int not null,
address varchar(25) not null,
city varchar(25) not null,
district varchar(25) not null,
state varchar(25) not null,
sex char(1) not null,
job varchar(25) not null,
bid int not null,
dob date not null,
aadhaar bigint not null unique,
cid int not null,
foreign key (bid) references bus_details(bid),
foreign key (cid) references company_details(cid));

create table travel_details(
tid int auto_increment primary key,
bid int,
uid int,
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