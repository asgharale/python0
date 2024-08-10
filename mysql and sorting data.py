import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="learn"
)
cursor = cnx.cursor()

query = "SELECT * FROM people;"
cursor.execute(query)
people = []

for (name, wei, hei) in cursor:
    people.append([name, wei, hei])

# sort
for k in range(len(people)-1):
    for j in range(len(people)-k-1):
        if(people[j][2]<people[j+1][2] or (people[j][2]==people[j+1][2] and people[j][1]>people[j+1][1])):
            people[j+1], people[j] = people[j], people[j+1]

for person in people:
    print(person[0], person[2], person[1])


cursor.close()
cnx.close()