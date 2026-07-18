import sqlite3

connect = sqlite3.connect('example.db')

c = connect.cursor()

# Here is how to update data
c.execute("UPDATE user SET name = 'Jhon' WHERE name = 'MED'")
 
c.execute("SELECT * FROM user")

items = c.fetchall()

for elem in items:
    print(elem)

connect.commit()
connect.close()