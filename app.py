from database.models.user import update_pin
# from database.models.transaction import show_transaction_history
from database.models.services.atm_service import (
    pin_verify,
    deposit_money,
    withdraw_amount,
    check_balance,
    transfer_money,show_transaction_history
)

card_number = input("Enter Card Number: ")
pin = input("Enter PIN: ")

if pin_verify(card_number, pin):

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            check_balance(card_number)

        elif choice == "2":
            amount = float(input("Enter Amount: "))
            deposit_money(card_number, amount)

        elif choice == "3":
            amount = float(input("Enter Amount: "))
            withdraw_amount(card_number, amount)

        elif choice == "4":
            receiver_account = input("Enter Receiver Account Number: ")
            amount = float(input("Enter Amount: "))
            transfer_money(card_number, receiver_account, amount)

        elif choice == "5":
            show_transaction_history(card_number)

        elif choice == "6":
            old_pin = input("Enter Old PIN: ")
            new_pin = input("Enter New PIN: ")

            update_pin(
                card_number,
                old_pin,
                new_pin
            )

        elif choice == "7":
            print("Thank You For Using ATM")
            break

        else:
            print("Invalid Choice")