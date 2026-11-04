class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(f"Brand   : {self.brand}")
        print(f"Model   : {self.model}")
        print(f"Storage : {self.storage} GB")
        print(f"Price   : Rs. {self.price:.2f}")

    def price_after_discount(self, discount_percent):
        discount = self.price * discount_percent / 100
        return self.price - discount


phone = MobilePhone("Samsung", "Galaxy S24", 256, 74999)
phone.display_specs()

discount = float(input("\nEnter discount percentage: "))
print(f"Price after {discount}% discount: Rs. {phone.price_after_discount(discount):.2f}")
