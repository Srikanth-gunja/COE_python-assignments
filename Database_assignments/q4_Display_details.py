from connection import mydb,mycursor

query="select * from players"

mycursor.execute(query)
res=mycursor.fetchall()
for i in res:
    print(i)
