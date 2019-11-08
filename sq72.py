import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hafsaabbas123",
    port= "3305",
    database="mydatabase2"
)
mycursor = mydb.cursor()
sql = "DELET FROM customers WHERE name = 'rashed'"
mycursor.execute(sql)
mydb.commit()
print (mycursor.rowcount, "record(s) deleted")
