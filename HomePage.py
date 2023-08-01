import mysql .connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Analyzer"
  )
"""mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Analyzer")
print("Database created..")"""

mycursor = mydb.cursor()
mycursor = mydb.cursor()
"""mycursor.execute("CREATE TABLE login(userid VARCHAR(30),password VARCHAR(50))")
print("done")"""

"""sql = "insert into login values('admin', '123');"""""
sql="insert into login values('guest', '123');"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")




