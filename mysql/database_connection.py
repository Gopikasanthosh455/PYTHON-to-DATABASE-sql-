import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gopika007#",
    database="mysql_class"
)
print(mydb)

x = mydb.cursor()
x.execute("show tables")
for i in x:
    print(i)