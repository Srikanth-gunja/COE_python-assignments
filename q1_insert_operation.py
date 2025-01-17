from connection import mycursor,mydb


sql = "INSERT INTO players (id,name,score,city,is_active) VALUES (%s,%s,%s,%s,%s)"

id=input("Enter id:")
name=input("Enter name:")
score=input("Enter score:")
city=input("Enter city:")
is_active=bool(input("Enter is_active(true/false):"))



val = (id,name,score,city,is_active)
mycursor.execute(sql, val)

mydb.commit()
