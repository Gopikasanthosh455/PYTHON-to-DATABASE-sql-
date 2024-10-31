import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gopika007#"
)
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)