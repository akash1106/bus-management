import mysql.connector as sql
def setup(host,user,passwd,data):
    mycon=sql.connect(host=host,user=user,passwd=passwd,database=data)
    if not mycon.is_connected():
        print("error while connecting!!")
    else:
        return mycon
print(setup("localhost","root","110akash62003","bus"))

def create_company(mycon,Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms):
    st=f"insert into company_details(name,cname,pass,phno,address,city,district,state,noofbus,rating,tandc) values('{0}','{1}',AES_ENCRYPT('{2}','key'),{3},'{4}','{5}','{6}','{7}',0,0,'{8}')".format(Company_Name,User_Name,Password,Phno,Address,City,District,State,Terms)
    cursor=mycon.cursor()
    cursor.execute(st)
    mycon.commit()