import mysql.connector as db

mydb=db.connect(
    host="localhost",
    user="root",
    password="root",
    database="cvr"
)
mycursor =mydb.cursor()