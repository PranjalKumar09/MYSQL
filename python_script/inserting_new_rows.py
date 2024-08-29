import mysql.connector
import random

db = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database=""
)

cursor = db.cursor()

first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Laura", "James", "Lisa"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
designations = ["Manager", "Clerk", "Analyst", "Executive", "Officer", "Assistant", "Consultant", "Cashier"]
departments = ["Loans", "Accounts", "Credit", "IT", "HR", "Operations", "Sales", "Compliance"]

for _ in range(150):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    desig = random.choice(designations)
    dept = random.choice(departments)
    
    sql = "INSERT INTO employee2 (fname, lname, desig, dept) VALUES (%s, %s, %s, %s)"
    values = (fname, lname, desig, dept)
    
    cursor.execute(sql, values)

db.commit()

cursor.close()
db.close()

print(f"Inserted {cursor.rowcount} rows into the employee2 table.")
