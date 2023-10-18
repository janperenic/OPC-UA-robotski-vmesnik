import sqlite3

# create a connection
conn = sqlite3.connect('values.db')

# create a table
c = conn.cursor()  # cursor

c.execute("""CREATE TABLE robot (
            name TEXT,
            value INTEGER,
            date TEXT
    )""")

# commit
conn.commit()

# close the connection
conn.close()
