from connection import mydb,mycursor


id=input("ENter id whose city to be updated:")
city=input("Enter city to be updated:")
query="update players set city=%s where id=%s"
mycursor.execute(query,(city,id))
mydb.commit()