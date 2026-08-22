import random


Attempt_count = 0
balance = 0
User_Pin = None

# Generate ATM PIN
def generate_pin():
    global User_Pin
    User_Pin = random.randint(100000, 999999)
    return User_Pin

# Withdraw Function
def withdraw():
    global balance
    global Attempt_count
    user_withdraw = 0
    if User_Pin is None:
        print("Please generate a PIN first.")
        return
    
    PIN = int(input("Enter PIN:"))

    if PIN != User_Pin:
        print("Incorrect Pin")
        Attempt_count += 1
        # print(Attempt_count)
        if Attempt_count == 3:
            print("UnAuthorized Person !")
        return
    else:
        user_withdraw = int(input("Enter Your Amount: "))
        if balance == 0:
            print("Account Balance is 0")
            return
    if user_withdraw <= 0:
        print("Please enter a valid amount.")
        return
    if user_withdraw > balance:
        print("Insufficient Balance!")
    else:
        balance -= user_withdraw
        print("Amount Withdrawn Successfully!")
        print("Remaining Balance:", balance)

while True:

    print("\n--------Welcome To 24x7 ATM------------")
    print("Generate PIN press 1")
    print("Deposit Amount press 2")
    print("Withdraw Amount press 3")
    print("View Balance press 4")
    print("Exit press 0")
    print("-----------------------------------------")

    user_input = input("Enter Your Choice: ")
    #Generate Pin
    if user_input == "1":
        print(f"Your PIN:{generate_pin()}")
    #Deposite Function
    elif user_input == "2":
        if User_Pin is None:
            print("Please generate a PIN first.")
            continue
        PIN = int(input("Enter PIN:"))
        if PIN != User_Pin:
            print("Incorrect Pin")
            Attempt_count += 1
            if Attempt_count == 3:
                print("UnAuthorized Person !")
                break
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
        PIN = int(input("Enter PIN: "))
        if PIN != User_Pin:
            print("Incorrect Pin")
            Attempt_count += 1
            if Attempt_count == 3:
                print("UnAuthorized Person !")
                break
        else:
            print("Available Balance:", balance)
    #Exit
    elif user_input == "0":
        print("Exit")
        break
    else:
        print("Invalid Choice!")
