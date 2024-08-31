import mysql.connector
import random
from datetime import datetime, timedelta

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="bank_db"
)

cursor = db.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS employee (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    dept_name VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
)
"""
cursor.execute(create_table_query)

db.commit()

departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales']
designations = ['Manager', 'Analyst', 'Developer', 'Consultant', 'Clerk']

def generate_random_name():
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'Chris', 'Anna']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names), random.choice(last_names)

def generate_random_date():
    start_date = datetime.now() - timedelta(days=365*10)
    end_date = datetime.now()
    return start_date + (end_date - start_date) * random.random()

def insert_random_data(num_records):
    for _ in range(num_records):
        fname, lname = generate_random_name()
        dept_name = random.choice(departments)
        designation = random.choice(designations)
        salary = round(random.uniform(30000, 120000), 2)
        hire_date = generate_random_date().strftime('%Y-%m-%d')

        insert_query = """
        INSERT INTO employee (fname, lname, dept_name, designation, salary, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (fname, lname, dept_name, designation, salary, hire_date))

    db.commit()

insert_random_data(100)

cursor.close()
db.close()

print("Random data inserted successfully.")
