class Payment:
    def __init__(self, amount):
        self.amount = amount

    def make_payment(self):
        print(f"Processing payment of Rs. {self.amount:.2f}")


class UPIPayment(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def make_payment(self):
        print(f"UPI: Rs. {self.amount:.2f} paid using UPI ID {self.upi_id}.")


class CardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def make_payment(self):
        masked = "XXXX-XXXX-XXXX-" + self.card_number[-4:]
        print(f"Card: Rs. {self.amount:.2f} paid using card {masked}.")


class WalletPayment(Payment):
    def __init__(self, amount, wallet_name, wallet_balance):
        super().__init__(amount)
        self.wallet_name = wallet_name
        self.wallet_balance = wallet_balance

    def make_payment(self):
        if self.amount > self.wallet_balance:
            print(f"Wallet: Insufficient balance in {self.wallet_name}.")
        else:
            self.wallet_balance -= self.amount
            print(f"Wallet: Rs. {self.amount:.2f} paid from {self.wallet_name}. "
                  f"Balance left: Rs. {self.wallet_balance:.2f}")


def checkout(payment):
    payment.make_payment()


orders = [UPIPayment(1500, "anjali@upi"),
          CardPayment(2999, "4111111111111234"),
          WalletPayment(800, "PayWallet", 2000)]

for order in orders:
    checkout(order)
