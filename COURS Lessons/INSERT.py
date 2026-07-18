import sqlite3

# Connect to database
connect = sqlite3.connect("example.db")

# Create cursor
cursor = connect.cursor()

# to insert one element :
cursor.execute("INSERT INTO TABLE_NAME (name, email, age) VALUES (?, ?, ?)", 
              ("John Doe", "john.doe@example.com", 25))

cursor.execute("""INSERT INTO TABLE_NAME VALUES (

        'Hamid',
        'Hamid@gmail.com',
        43
        
      )""")

# =====================================================================================

# to insert many elements meanwhile

group = [
  ("Ahmed", "Ahmed@example.com", 32),
  ('Aziz', 'Aziz@gmail.com', 43)
  # ect...
]

cursor.execute('INSERT INTO TABLE_NAME (name, email, age) VALUES (?, ?, ?)', group)


# Commit changes
connect.commit()

# Close connection
connect.close()
