import sqlite3

conn = sqlite3.connect("beautiful_soup/example.db")

c = conn.cursor()

# Create table
c.execute(
    """CREATE TABLE IF NOT EXISTS stocks
             (date text, trans text, symbol text, qty real, price real)"""
)

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
c.execute("INSERT INTO stocks VALUES ('2007-06-30','HOLD','TTEK',99,68.85)")

# Save (commit) the changes
conn.commit()

for row in c.execute("SELECT * FROM stocks ORDER BY price"):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
