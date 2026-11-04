class ATM:
    def __init__(self, account_no, holder_name, balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def check_balance(self):
        print(f"Current balance: Rs. {self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
        else:
            self.balance += amount
            print(f"Rs. {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs. {amount:.2f} withdrawn successfully.")

    def display_details(self):
        print(f"Account No  : {self.account_no}")
        print(f"Holder Name : {self.holder_name}")
        print(f"Balance     : Rs. {self.balance:.2f}")


atm = ATM(123456789, "Anjali", 5000)

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        atm.deposit(float(input("Enter amount to deposit: ")))
    elif choice == "3":
        atm.withdraw(float(input("Enter amount to withdraw: ")))
    elif choice == "4":
        atm.display_details()
    elif choice == "5":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Try again.")
