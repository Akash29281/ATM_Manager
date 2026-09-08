from database.db import get_connection
conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(100) NOT NULL,
pin VARCHAR(10) NOT NULL,
balance DECIMAL(10,2) DEFAULT 0
)
""")

conn.commit()

print("✅ User table is created successfully")
conn.close()