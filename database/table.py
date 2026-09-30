from database.db import get_connection
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(100) NOT NULL,
account_number VARCHAR(100) UNIQUE NOT NULL,
card_number VARCHAR(100) UNIQUE NOT NULL,
balance DECIMAL(10,2) NOT NULL DEFAULT 0,
is_locked BOOLEAN DEFAULT FALSE,
pin VARCHAR(10) NOT NULL DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions(
id INT AUTO_INCREMENT PRIMARY KEY,
user_id INT NOT NULL,
transaction_type VARCHAR(20) NOT NULL,
amount DECIMAL(10,2),
transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
""")

conn.commit()

print("✅ User table is created successfully")
cursor.close()
