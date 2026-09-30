from database.db import get_connection

# #Insert data
# def create_user(username, pin):

#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """
#     INSERT INTO users (username, pin, balance)
#     VALUES (%s, %s, %s)
#     """

#     values = (username, pin, 0)

#     cursor.execute(query, values)

#     conn.commit()

#     print("User created successfully")

#     cursor.close()
#     conn.close()

# # read data

# def get_user(username):

#     conn = get_connection()
#     cursor = conn.cursor(buffered=True)

#     query = """
#     SELECT id, username, pin, balance
#     FROM users
#     WHERE username = %s
#     """

#     cursor.execute(query, (username,))

#     user = cursor.fetchone()

#     cursor.close()
#     print("User Fetch sucessfully")
#     conn.close()

#     return user

# # update data
# def update_pin(user_id, new_pin):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """UPDATE users SET pin = %s WHERE id = %s"""

#     values = (new_pin, user_id)

#     cursor.execute(query, values)
#     conn.commit()
#     print("Pin udated sucessfully: ")
#     cursor.close()
#     conn.close()

# def delete(id):
#     conn = get_connection()
#     cursor = conn.cursor()

#     query = """DELETE FROM users WHERE id = %s"""
#     value = (id)
#     cursor.execute(query,value)
    
#     conn.commit()
#     cursor.close()
#     conn.close()

# create user
def create_user(username,account_number, card_number, balance, pin):
    conn = get_connection()
    cursor = conn.cursor()

    query = """INSERT INTO users (customer_name, account_number, card_number, balance, pin) VALUES (%s,%s,%s,%s,%s)"""

    values = (username,account_number, card_number, balance, pin)

    cursor.execute(query, values)

    conn.commit()
    # print("Data inserted")
    cursor.close()
    conn.close()

def get_user_by_card(card_number):
    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM users WHERE card_number = %s"""

    cursor.execute(query,(card_number,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

def pin_verify(card_number, pin):
    user = get_user_by_card(card_number)
    if user is None:
        print("Card not found")
        return False

    if user[6] == pin:
        print("login sucessfully")
        return True

    print("invalid pin")
    return False

# Transactions data

def create_transactions(user_id, transaction_type,amount):
    conn = get_connection()
    cursor = conn.cursor()

    query = """INSERT INTO Transactions(user_id
    transaction_type,
    amount) VALUES (%s,%s,%s,%s,%s)
    """

    values = (
    user_id, 
    transaction_type,
    amount
    )

    cursor.execute(query, values)
    conn.commit()
    print("Transaction saved successfully:")
    cursor.close()
    conn.close()