import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hafsaabbas123",
    port= "3305",
    database="mydatabase1"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address Like '%way%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print (x)
