from decimal import Decimal, InvalidOperation

from database.models.user import get_user_by_card, get_user_by_account, update_balance
from database.models.transaction import create_transactions, get_transactions


def _to_money(amount):
    try:
        return Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        return None


def deposit_money(card_number, amount):
    user = get_user_by_card(card_number)
    money = _to_money(amount)

    if user is None:
        print("User not found")
        return False, "User not found"
    if money is None or money <= 0:
        print("Invalid Amount")
        return False, "Enter a valid deposit amount greater than zero"

    user_id = user[0]
    current_balance = Decimal(str(user[4]))
    new_balance = current_balance + money

    update_balance(user_id, new_balance)
    create_transactions(user_id, "Deposit", money)
    print("Deposit successful")
    print("New balance", new_balance)
    return True, f"₹{money:,.2f} deposited successfully"


def withdraw_amount(card_number, amount):
    user = get_user_by_card(card_number)
    money = _to_money(amount)

    if user is None:
        print("User not found")
        return False, "User not found"
    if money is None or money <= 0:
        print("Invalid Amount")
        return False, "Enter a valid withdrawal amount greater than zero"

    user_id = user[0]
    current_balance = Decimal(str(user[4]))

    if current_balance < money:
        print("Insufficient Balance")
        return False, "Insufficient balance for this withdrawal"

    new_balance = current_balance - money
    update_balance(user_id, new_balance)
    create_transactions(user_id, "Withdraw", money)
    print("Withdraw Successful")
    print("Remaining Balance:", new_balance)
    return True, f"₹{money:,.2f} withdrawn successfully"


def check_balance(card_number):
    user = get_user_by_card(card_number)
    if user is None:
        print("User not found")
        return None
    print(f"Current Balance: ₹{user[4]}")
    return user[4]


def pin_verify(card_number, pin):
    user = get_user_by_card(card_number)
    if user is None:
        print("User not found")
        return False
    if user[5]:
        print("Account Locked")
        return False
    if str(user[6]) == str(pin):
        print("Login Successfully")
        return True
    print("Invalid PIN")
    return False


def show_transaction_history(card_number):
    user = get_user_by_card(card_number)
    if user is None:
        print("User not found")
        return []

    transactions = get_transactions(user[0])
    print("\n===== TRANSACTION HISTORY =====")
    for t_type, amount in transactions:
        print(f"{t_type:<15} ₹{amount}")
    return transactions


def transfer_money(sender_card, receiver_account, amount):
    sender = get_user_by_card(sender_card)
    money = _to_money(amount)

    if sender is None:
        print("Sender not found")
        return False, "Sender account not found"

    receiver = get_user_by_account(receiver_account)
    if receiver is None:
        print("Receiver not found")
        return False, "Receiver account not found"

    if sender[0] == receiver[0]:
        print("Cannot transfer to same account")
        return False, "You cannot transfer money to your own account"

    if money is None or money <= 0:
        print("Invalid Amount")
        return False, "Enter a valid transfer amount greater than zero"

    sender_balance = Decimal(str(sender[4]))
    if sender_balance < money:
        print("Insufficient Balance")
        return False, "Insufficient balance for this transfer"

    receiver_balance = Decimal(str(receiver[4]))
    new_sender_balance = sender_balance - money
    new_receiver_balance = receiver_balance + money

    update_balance(sender[0], new_sender_balance)
    update_balance(receiver[0], new_receiver_balance)
    create_transactions(sender[0], "Transfer Out", money)
    create_transactions(receiver[0], "Transfer In", money)

    print("Transfer Successful")
    print(f"Transferred ₹{money}")
    return True, f"₹{money:,.2f} transferred successfully"
