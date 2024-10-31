import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gopika007#",
    database="mysql_class"
)
print(mydb)

x = mydb.cursor()
x.execute("insert into customer values(111,'archa','mannampatta',680767,7789876677)")
x.execute("select * from customer")
data=x.fetchall()
for i in data:
    print(i)