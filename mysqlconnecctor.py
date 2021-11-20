import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", database = "practical")
mycursor = mydb.cursor()
mycursor.execute("Show Tables")

for i in mycursor:
    print(i)
mycursor.execute ("select * from STD1")

for i in mycursor:
    print(i)

mycursor.execute("insert into std1 values(1, 'Nikhil', ")