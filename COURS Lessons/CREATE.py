# import sqlite3 module
import sqlite3

# connect this python file to the database
connect = sqlite3.connect("__DATABASE_NAME__.db")

# CREATE A CURSOR
cursor = connect.cursor()


# to execute commands on the datbase
cursor.execute(""" CREATE TABLE table_name (
	
	user_name TEXT,
	number_phone INTEGER,
	email TEXT

)""")

# DATA TYPES IN SQLITE are : 
data_types = {
 
    'INTEGER' : '1, 2, 3, 4..',
    'TEXT' : 'STRINGS',
    'REAL' : '0.1 | float',
    'NULL' : 'None | doesn\'t exist',
    'BLOB' : 'Binary object: stores data as it was input (e.g. images, files...)'
    ''
}

# commit your changes
connect.commit()

# stop the connection
connect.close()