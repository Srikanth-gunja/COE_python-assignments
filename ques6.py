# dispaly score b/w 70-90
from connection import mydb,mycursor

query="select * from players where score between 70 and 90"

mycursor.execute(query)
res=mycursor.fetchall()
for i in res:
    print(i)
