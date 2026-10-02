from database.db import get_connection
from database.models.transaction import create_transactions,get_transactions


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

def locked_account(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """UPDATE users SET is_locked = TRUE WHERE id = %s"""

    cursor.execute(query,(user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Account Locked")


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

    