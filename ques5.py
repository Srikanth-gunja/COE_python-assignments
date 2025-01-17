# diaply by asc order of name

from connection import mycursor,mydb

query="select * from players  order by score asc"

mycursor.execute(query)
res=mycursor.fetchall()
for i in res:
    print(i)