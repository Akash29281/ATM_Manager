from database.db import get_connection
conn = get_connection()
if conn.is_connected():
    print("DB is connected") #checking connection is established or not.

conn.close() #connection closed