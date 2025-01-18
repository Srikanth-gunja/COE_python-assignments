from connection import mydb,mycursor



id=input("Enter id to Delete:")

query="delete from players where id = %s"

mycursor.execute(query,(id,))
mydb.commit()