class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def calculate_interest(self, years=1):
        return 0


class SavingsAccount(BankAccount):
    def calculate_interest(self, years=1):

        return self.balance * ((1 + 0.04) ** years - 1)


class CurrentAccount(BankAccount):
    def calculate_interest(self, years=1):

        return 0.0


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, years=1):

        return self.balance * ((1 + 0.07) ** years - 1)


accounts = [SavingsAccount(1, 100000),
            CurrentAccount(2, 100000),
            FixedDepositAccount(3, 100000)]

for acc in accounts:
    print(f"{acc.__class__.__name__:<20} Interest for 3 years: "
          f"Rs. {acc.calculate_interest(3):.2f}")
