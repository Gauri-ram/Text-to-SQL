import sqlite3

connection= sqlite3.connect("student.db")

cursor= connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values('Gauri','CSE','B',94)''')
cursor.execute('''Insert into STUDENT values('Divya','BIO','A',98)''')
cursor.execute('''Insert into STUDENT values('Ram','CIV','C',80)''')
cursor.execute('''Insert into STUDENT values('Hari','ECE','B',81)''')
cursor.execute('''Insert into STUDENT values('Ravi','ECE','C',92)''')
cursor.execute('''Insert into STUDENT values('Navneet','Civ','B',67)''')
cursor.execute('''Insert into STUDENT values('Advait','CSE','A',70)''')

print("All records are: ")

data= cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()