import sqlite3

conn = sqlite3.connect("atm.db") # make connection 
print("Database Connected ")  # line shows db is connected or not
conn.close()