import mysql.connector

print("connecting...")
cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="test"
    # auth_plugin='mysql_native_password'
)
print("connected to db.")
cursor = cnx.cursor(buffered=True)
cursor.execute("INSERT INTO people VALUES (\'sam\', \'m\', 28)")
cursor.execute("INSERT INTO people VALUES (\'ahmad\', \'m\', 19)")
cursor.execute("INSERT INTO people VALUES (\'ali\', \'m\', 24)")
print(cursor.execute("SELECT * FROM people"))

cnx.commit()
cursor.close()
cnx.close()