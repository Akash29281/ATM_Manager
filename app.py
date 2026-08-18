import random

balance = 0
User_Pin = 0

# Generate ATM PIN
def generate_pin():
    User_Pin = random.randint(100000, 999999)
    return User_Pin

# Withdraw Amount
def withdraw():
    global balance

    PIN = input("Enter PIN:")
    if PIN == User_Pin:
        if balance == 0:
            print("Account Balance is 0")
            return
    else:
        print("Incorrect Pin")    

    user_withdraw = int(input("Enter Your Amount: "))

    if user_withdraw > balance:
        print("Insufficient Balance!")
    else:
        balance -= user_withdraw
        print("Amount Withdrawn Successfully!")
        print("Available Balance:", balance)


while True:

    print("\n--------Welcome To 24x7 ATM------------")
    print("Generate PIN press 1")
    print("Deposit Amount press 2")
    print("Withdraw Amount press 3")
    print("View Balance press 4")
    print("Exit press 0")
    print("---------------------------------------")

    user_input = input("Enter Your Choice: ")

    if user_input == "1":
        print(f"Your PIN: {generate_pin()}")

    elif user_input == "2":
        user_dep = int(input("Enter Your Amount: "))
        balance += user_dep
        print("Deposit Successful!")
        print("Available Balance:", balance)

    elif user_input == "3":
        withdraw()

    elif user_input == "4":
        print("Available Balance:", balance)

    elif user_input == "0":
        print("Exit")
        break

    else:
        print("Invalid Choice!")
