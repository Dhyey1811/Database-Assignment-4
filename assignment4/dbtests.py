# dbtests.py
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)

cursor = conn.cursor()
cursor.execute("SHOW COLUMNS FROM subscribers")
columns = [col[0] for col in cursor.fetchall()]

required_columns = ['id', 'name', 'email', 'subscription_date']

for col in required_columns:
    assert col in columns, f"Missing column: {col}"

print("All required columns found ✅")

cursor.close()
conn.close()
