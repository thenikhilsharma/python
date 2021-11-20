import mysql.connector as c
con = c.connect(host="localhost", user="root", password="Nikhil2004*#", database="DB1")
if con.is_connected():
    print("Successfully Connected...")