class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):


        u = self.units
        if u <= 100:
            bill = u * 1.50
        elif u <= 200:
            bill = 100 * 1.50 + (u - 100) * 2.50
        elif u <= 300:
            bill = 100 * 1.50 + 100 * 2.50 + (u - 200) * 4.00
        else:
            bill = 100 * 1.50 + 100 * 2.50 + 100 * 4.00 + (u - 300) * 6.00
        return bill

    def display(self):
        print("\n----- Electricity Bill -----")
        print(f"Consumer No   : {self.consumer_no}")
        print(f"Consumer Name : {self.consumer_name}")
        print(f"Units Consumed: {self.units}")
        print(f"Total Bill    : Rs. {self.calculate_bill():.2f}")


consumer_no = input("Enter consumer number: ")
consumer_name = input("Enter consumer name: ")
units = int(input("Enter units consumed: "))

bill = ElectricityBill(consumer_no, consumer_name, units)
bill.display()
