import random

deposit_Amt = 0


#Genetate atm pin 
def generate_pin():
    pin = random.randint(100000,999999)
    return pin

while True:
    

    print("--------Welcome To 24x7 ATM------------")
    print("Generate pin press 1: ")
    print("Deposite Amount press 2: ")
    print("Withdraw Amount press 3: ")
    print("View Balance press 4: ")
    print("Exit press 0:")
    print("---------------------------------------")

    user_input = input("Enter Your Choice: ")

    if user_input == "1":
        print(f"Your Pin: {generate_pin()}")

    if user_input == "2":
        user_dep = int(input("Enter Your amount: "))
        deposit_Amt += user_dep
        print("Deposite successfull !")
        print(deposit_Amt)

    elif user_input == "0":
        print("exit")
        break
