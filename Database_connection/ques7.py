# select details from specfic city

from connection import mydb,mycursor


city=input("Enter city to selct :")
query="select * from players where city=%s"

mycursor.execute(query,(city,))
res=mycursor.fetchall()
for i in res:
    print(i)
