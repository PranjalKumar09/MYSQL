import mysql.connector
import random 
from datetime import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Admin@123",
    database="bank_db"
)
cursor = db.cursor()
""" 
first_names = ["John", "Jane", "Alex", "Emily", "Michael"]
decimal_list = [482.56, 725.93, 254.31, 698.45, 875.21, 312.78, 946.10, 581.34, 743.88, 659.42, 192.57, 838.14, 479.90, 267.66, 914.23]



for _ in range(15):
    name = random.choice(first_names)
    price = random.choice(decimal_list)
    sql = "INSERT INTO orders (name, email) VALUES (%s, %s)"
    values = (name, name.lower()+"@gmail.com")
    cursor.execute(sql, values)
    
db.commit()

cursor.close()
db.close()
print("Done") """


ord_values = sorted(random.sample(range(1, 100), 20))  
cust_ids = list(range(1, 18))  
random.shuffle(cust_ids)  

cust_ids = list(range(1, 18)) 
random.shuffle(cust_ids)  

while len(cust_ids) < 20:
    cust_ids.append(random.randint(1, 17))

for i in range(20):
    ord_value = ord_values[i]
    date_value = datetime.now().strftime('%Y-%m-%d')  
    amount_value = round(random.uniform(100.00, 990.00), 2)
    cust_id_value = cust_ids[i]
    
    sql = "INSERT INTO orders (ord_id, date, amount, cust_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (ord_value, date_value, amount_value, cust_id_value))

db.commit()

cursor.close()
db.close()
print("Done")
