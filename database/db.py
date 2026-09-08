import mysql.connector

def get_connection():
    conn = mysql.connector.connect(host = "localhost",user = "root",password ="1825@Kash",database = "atm_manager")

    return conn