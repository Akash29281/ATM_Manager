from database.db import get_connection


def create_user(username, account_number, card_number, balance, pin):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO users (customer_name, account_number, card_number, balance, pin)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, account_number, card_number, balance, pin))
    conn.commit()
    cursor.close()
    conn.close()


def get_user_by_card(card_number):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE card_number = %s"
    cursor.execute(query, (card_number,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def get_user_by_account(account_number):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE account_number = %s"
    cursor.execute(query, (account_number,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user


def locked_account(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET is_locked = TRUE WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    print("Account Locked")
    return True


def update_balance(user_id, balance):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET balance = %s WHERE id = %s"
    cursor.execute(query, (balance, user_id))
    conn.commit()
    cursor.close()
    conn.close()
    print("Balance updated")
    return True


def update_pin(card_number, old_pin, new_pin):
    user = get_user_by_card(card_number)

    if user is None:
        print("User not found")
        return False, "User not found"

    stored_pin = str(user[6])
    old_pin = str(old_pin)
    new_pin = str(new_pin)

    if stored_pin != old_pin:
        print("Wrong PIN")
        return False, "Current PIN is incorrect"

    if old_pin == new_pin:
        print("New PIN can't be same as old PIN")
        return False, "New PIN cannot be the same as your current PIN"

    if len(new_pin) != 4:
        print("PIN must be 4 digits")
        return False, "PIN must be exactly 4 digits"

    if not new_pin.isdigit():
        print("PIN must contain only numbers")
        return False, "PIN must contain only numbers"

    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET pin = %s WHERE id = %s"
    cursor.execute(query, (new_pin, user[0]))
    conn.commit()
    cursor.close()
    conn.close()
    print("PIN Updated Successfully")
    return True, "PIN changed successfully"
