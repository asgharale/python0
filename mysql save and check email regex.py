import mysql.connector
import re

# database info
host = "localhost" #input("enter your host: ")
db_username = input("enter your database username: ")
db_pass = input("enter your database user's password: ")
db_name = input("enter your db name: ")
try:
    cnx = mysql.connector.connect(
        host=host,
        user=db_username,
        password=db_pass,
        database=db_name
        )
    cursor = cnx.cursor(buffered=True)
    cursor.execute("create table user_auth (username varchar(200), password varchar(200));")
except:
    print("somthing went wrong with your db. please try again.")

# data
right_email = "expression@string.string"
email = input("Enter your email: ")
pasword = input("Enter your pasword: ")

email_test = re.search(r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', email)
while(not email_test):
    print(right_email)
    email = input("Enter your email please: ")
    email_test = re.search(r'[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}', email)

cursor.execute(f"insert into user_auth values ('{email}', '{pasword}');")

cnx.commit()
cursor.close()
cnx.close()