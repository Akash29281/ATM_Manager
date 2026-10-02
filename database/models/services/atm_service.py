from database.db import get_connection
from database.models.user import get_user_by_card, update_balance
from database.models.transaction import create_transactions,get_transactions

def deposit_money(card_number, amount):
    user = get_user_by_card(card_number)

    if amount <= 0:
        print("Invalid Amount")
        return
    # if user is None:
    #     print("user not found:")
    #     return

    user_id = user[0]
    current_balance = float(user[4])
    new_balance = current_balance + amount

    # call update function
    update_balance(user_id, new_balance)
    create_transactions(user_id,"Deposit",amount)
    print("deposit sucessfull")
    print("new_balance",new_balance)

def withdraw_amount(card_number, amount):
    user = get_user_by_card(card_number)
    if user is None:
        print("user not found:")
        return

    user_id = user[0]
    current_balance = float(user[4])

    if amount <= 0:
        print("Invalid Amount")
        return
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
    print(f"Current Balance: ₹{user[4]}")

def pin_verify(card_number, pin):
    user = get_user_by_card(card_number)
    if user is None:
        print("user not found")
        return False
    if user[5]:
        print("Account Locked")
        return False

    if user[6]== pin:
        print("Login Sucessfully")
        return True

    print("Invalid PIN")
    return False

def show_transaction_history(card_number):

    user = get_user_by_card(card_number)

    user_id = user[0]
    conn = get_connection()
    cursor = conn.cursor()

    if user is None:
        print("User not found")
        return
    user_id = user[0]

    transactions = get_transactions(user_id)
    
    print("\n===== TRANSACTION HISTORY =====")
    for transaction in transactions:
        print(transaction)

    cursor.close()
    conn.close()