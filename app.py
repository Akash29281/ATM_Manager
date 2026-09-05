import random

class ATM_Manager:

    def __init__(self,amount=0, pin=None, attempt=0):
        self.amount = amount
        self.pin = pin
        self.attempt = attempt

    def pin_verify(self):
        if self.pin is None:
            print("Please generate pin first")
            return False
        attempt = 0
        while attempt < 3:

            try:
                user_pin = int(input("Enter Pin: "))
            except ValueError:
                print("Enter only numeric value")
                continue
            if user_pin == self.pin:
                return True
            attempt += 1
            print(f"Invalid PIN! Attempts Left: {3 - self.attempt}")

        print("Account Blocked. try Again later")
        return False
    
    #Withdraw function
    def withdraw(self):
        if not self.pin_verify():
            return
        amount = int(input("Enter Amount To Withdraw: "))
        if amount < 500:
            print("Please withdraw 500 or more: ") #alert msg
            return
        if amount > self.amount:
            print("Insufficient Balance")
            return
        self.amount -= amount
        print(f"₹{amount} Withdraw Successfully")
        return
    
    #Deposite Function
    def deposite(self):
        if not self.pin_verify():
            return
        amount = int(input("Enter Amount To Deposite: "))
        if amount <= 0:
            print("Invalid amount")
            return
        self.amount += amount
        print(f"₹{amount} Deposited Successfully")
        return  

    # Balance function
    def balance(self):
        print(f"Current Balance: ₹{self.amount}")

    def Pin_generate(self):
        pin = random.randint(1000,9999)
        print("pin generated successfully",pin)
        self.pin = pin
        
    def exit(self):
        exit



A1 = ATM_Manager()
 #atm.deposite(500)

while True:
    print("\n-------- Welcome To 24x7 ATM --------")
    print("Deposit Amount press 1")
    print("Withdraw Amount press 2")
    print("View Balance press 3")
    print("Generate Pin press 4")
    print("Exit press 0")
    print("-------------------------------------")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        #amount = int(input("Enter Amount: "))
        A1.deposite()

    elif choice == 2:
        A1.withdraw()

    elif choice == 3:
        A1.balance()

    elif choice == 4:
        A1.Pin_generate()

    elif choice == 0:
        print("Thank You For Using ATM")
        A1.exit()
        break

    else:
        print("Invalid Choice")