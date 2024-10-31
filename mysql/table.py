import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gopika007#",
    database="mysql_class"
)
print(mydb)

x = mydb.cursor()
x.execute("create table staff(id int primary key,name varchar(20),salary bigint,designation varchar(20))")
x.execute("insert into staff values(1,'gopika',30000,'manager')")
x.execute("insert into staff values(2,'devika',25000,'assistant manager')")
x.execute("insert into staff values(3,'anupama',35000,'hr')")
x.execute("insert into staff values(4,'kiran',15000,'salesman')")
x.execute("insert into staff values(5,'varun',35000,'ceo')")
x.execute("select * from staff")
data=x.fetchall()
for i in data:
    print(i)