from database.db import get_connection

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

#update balance
def update_balance(user_id, balance):
    conn = get_connection()
    cursor = conn.cursor()

    query = """UPDATE users SET balance = %s WHERE id = %s"""
    cursor.execute(query,(balance, user_id))

    conn.commit()
    print("Balance update ")
    cursor.close()
    conn.close()

# Transactions data
def create_transactions(user_id, transaction_type,amount):
    conn = get_connection()
    cursor = conn.cursor()

    query = """INSERT INTO transactions(user_id,transaction_type,
    amount) VALUES (%s,%s,%s)
    """

    values = (
    user_id,transaction_type,amount
    )

    cursor.execute(query, values)
    conn.commit()
    print("Transaction saved successfully:")
    cursor.close()
    conn.close()

def get_transactions(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """ SELECT transaction_type,amount FROM transactions WHERE user_id = %s"""

    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()
    conn.close()
    cursor.close()

    return transactions

def deposite_money(card_number, amount):
    user = get_user_by_card(card_number)

    if user is None:
        print("user not found:")
        return

    user_id = user[0]
    current_balance = float(user[4])
    new_balance = current_balance + amount

    # call update function
    update_balance(user_id, new_balance)
    create_transactions(user_id,"Deposite",amount)
    print("deposite sucessfull")
    print("new_balance",new_balance)

def withdraw_amount(card_number, amount):
    user = get_user_by_card(card_number)
    if user is None:
        print("user not found:")
        return

    user_id = user[0]
    current_balance = float(user[4])
    if current_balance < amount:
        print("insufficient Balance")
        return

    new_balance = current_balance - amount
    
    # calling update function
    update_balance(user_id, new_balance)
    #calling transaction funnction
    create_transactions(user_id, "Withdraw",amount)

    print("Withdraw Successful")
    print("Remaining Balance:", new_balance)

def check_balance(card_number):
    user = get_user_by_card(card_number)

    if user is None:
        print("user not fount")
        return

    print("Current Balance:", user[4])

def update_pin(card_number, old_pin, new_pin):
    user = get_user_by_card(card_number)

    if user is None:
        print("User not found:")
        return

    stored_pin = user[6]
    if stored_pin != old_pin:
        print("Wrong PIN")
        return
    
    if old_pin == new_pin:
        print("new pin can't be same as old pin")
        return

    if len(str(new_pin)) != 4:
        print("PIN must be 4 digit")
        return 

    if not str(new_pin).isdigit():
        print("PIN must be contain only numbers")
        return
    conn = get_connection()
    cursor = conn.cursor()

    query = """UPDATE users SET pin = %s 
    WHERE id = %s"""

    cursor.execute(query , (new_pin,user[0]))

    conn.commit()
    print("PIN Updated:")

    cursor.close()
    conn.close()

    