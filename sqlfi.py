f = open ("12.txt","r")
for x in f:
    print(x)
f = open ("12.txt","r")
f.write(" The best way we learn anything is by practice and exercise questions")
f.close()
f = open("12.txt","r")
print(f.read())
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Hafsaabbas123",
    port= "3305",
    database= "myEmployee")
mycursor = mydb.cursor()
sql="DELETE FROM Employee WHERE 'Age = 34' "
mycursor.execute(sql)
mydb.commit()
myresult =mycursor.setchall()
for x in myresult:
    print(x)