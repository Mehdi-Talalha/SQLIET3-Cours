# TUTORIAL VIDEO : 
# https://youtu.be/byHcYRpMgI4


# import sqlite3 module
import sqlite3

# connect this python file to the database
connect = sqlite3.connect("__DATABASE_NAME__.db")

# CREATE A CURSOR
cursor = connect.cursor()


# to execute commands
cursor.execute(""" 


YOU_SQLITE_COMMAND_SHOULD_BE_HERE


""")

# commit your changes
connect.commit()

# stop the connection
connect.close()