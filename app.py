import random

balance = 0
User_Pin = None
# Generate ATM PIN
def generate_pin():
    global User_Pin
    User_Pin = random.randint(100000, 999999)
    return User_Pin

# Withdraw Amount
def withdraw():
    global balance

    PIN = int(input("Enter PIN:"))
    if PIN != User_Pin:
        print("Incorrect Pin")
        return
    else:
        if balance == 0:
            print("Account Balance is 0")
            return

    user_withdraw = int(input("Enter Your Amount: "))

    if user_withdraw > balance:
        print("Insufficient Balance!")
    else:
        balance -= user_withdraw
        print("Amount Withdrawn Successfully!")


while True:

    print("\n--------Welcome To 24x7 ATM------------")
    print("Generate PIN press 1")
    print("Deposit Amount press 2")
    print("Withdraw Amount press 3")
    print("View Balance press 4")
    print("Exit press 0")
    print("---------------------------------------")

    user_input = input("Enter Your Choice: ")
    #Generate Pin
    if user_input == "1":
        print(f"Your PIN:{generate_pin()}")
        pass

    #Deposite Function
    elif user_input == "2":
        print(User_Pin)
        if User_Pin is None:
            print("Please generate a PIN first.")
            continue
        PIN = int(input("Enter PIN:"))
        if PIN != User_Pin:
            print("Incorrect Pin")
        else:
            user_dep = int(input("Enter Your Amount: "))
            if user_dep <= 0:
                print("Please enter a valid amount.")
            else:
                balance += user_dep
                print("Deposit Successful!")
    #Withdraw function        
    elif user_input == "3":
        withdraw()
    #View Balance
    elif user_input == "4":
        PIN = int(input("Enter PIN:"))
        if PIN != User_Pin:
            print("Incorrect Pin")
        else:
            print("Available Balance:", balance)
    #Exit
    elif user_input == "0":
        print("Exit")
        break

    else:
        print("Invalid Choice!")
