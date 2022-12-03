import mysql.connector
connector=mysql.connector.connect(host='localhost',user='root',password='1234',database='kalpaj')
cursor=connector.cursor()
# cursor.execute('show databases') 
structure="insert into kalpaj(full_name,pincode,contact,roll_no,division) values(%s,%s,%s,%s,%s)"
values=[('kalpaj dunbale','422009',77448929,3,'a'),('kalpaj dunbale','422009',77448929,2,'a')]
cursor.executemany(structure,values)
connector.commit()
for i in cursor:
    print(i)