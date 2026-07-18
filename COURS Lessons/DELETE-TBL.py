import sqlite3

connect = sqlite3.connect('example.db')

c = connect.cursor()

# Drom Table  
c.execute('DROP TABEL TABLE_NAME')


connect.commit()
connect.close()