import mysql.connector
import random

# Establishing the connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="****",
    password="****",
    database="bank_db"
)

# Creating a cursor object
cursor = db.cursor()

# Query to select all employee IDs
cursor.execute("SELECT emp_id FROM employee2")
emp_ids = cursor.fetchall()

# Loop through each employee and update their salary with a random value
for emp_id in emp_ids:
    random_salary = random.randint(10000, 99999)
    update_query = "UPDATE employee2 SET salary = %s WHERE emp_id = %s"
    cursor.execute(update_query, (random_salary, emp_id[0]))

# Commit the transaction to save the changes
db.commit()

# Close the cursor and connection
cursor.close()
db.close()

print("Salaries have been randomized successfully!")