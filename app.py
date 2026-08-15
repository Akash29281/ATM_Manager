import random


while True:

    print("--------Welcome To 24x7 ATM------------")
    print("Generate pin press 1: ")
    print("Deposite Amount press 2: ")
    print("Withdraw Amount press 3: ")
    print("View Balance press 4: ")
    print("Exit press 0:")
    print("---------------------------------------")

    user_input = input("Enter Your Choice: ")

    #Genetate atm pin 
    def generate_pin():
        pin = random.randint(100000,999999)
        return pin


    if user_input == "1":
        print(f"Your Pin: {generate_pin()}")



