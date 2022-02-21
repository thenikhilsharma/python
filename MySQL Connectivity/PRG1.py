import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="mysql", password='root')
mycursor = mydb.cursor()
mycursor.execute("show tables")
for i in mycursor:
    print(i)