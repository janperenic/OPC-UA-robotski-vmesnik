import sqlite3

# create a connection
conn = sqlite3.connect('values.db')

# create a cursor to execute SQL commands
c = conn.cursor()

# execute the SQL command to delete all content in the table
c.execute("DELETE FROM robot")

# commit changes
conn.commit()

# close the connection
conn.close()