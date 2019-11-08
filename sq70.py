import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hafsaabbas123",
    port= "3305",
    database="mydatabase2"
)
mycursor = mydb.cursor()
mycursor.execute= (" CREATE TABLE customers (name VARCHAR (225), address VARCHAR(225))")