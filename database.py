import mysql.connector as MyConn

db = MyConn.connect(host = "localhost",user = "root",password = "1825@Kash",)

print(db,"Connected")