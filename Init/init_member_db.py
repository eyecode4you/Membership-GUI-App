"""	init_member_db.py - Use schema.sql to create initial member db
	Create a simple database to use with Membership app """
import sqlite3
connection = sqlite3.connect('members.db')
with open('schema.sql') as f:
	"""Open our created sql schema & execute for initial db structure"""
	connection.executescript(f.read())
cur = connection.cursor()
#Fill in the following fields for creation of initial member
cur.execute("INSERT INTO members (name, phone, email, address, nationality, category, company, position, expiry) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
			('Sample User1', '0123456789', 'samu1@gmail.com', 'Resotto', 'Aberdeen', '', 'Tube Men Ltd.', 'Director', 'n/a'))
cur.execute("SELECT * FROM members")
res = cur.fetchall()
for i in res:
	print(i)
connection.commit() #apply changes
connection.close() #end connection
print("Database Successfully Created!")
